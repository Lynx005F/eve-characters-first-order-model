import imageio
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from skimage.transform import resize
import warnings
import os
import urllib.request, urllib.error
from moviepy.editor import VideoFileClip, concatenate_videoclips



warnings.filterwarnings("ignore")

#Create a model and load checkpoints
from demo import load_checkpoints
generator, kp_detector = load_checkpoints(config_path='config/vox-256.yaml',
                                          checkpoint_path='vox-cpk.pth.tar')

from demo import make_animation
from skimage import img_as_ubyte

#Go trough Files
for filename in os.listdir('input'):
    if filename.endswith(".mp4"):

        # Get Character profile from Filename
        characterId = filename.split('_')[-1].strip(".mp4")
        print(filename)

        # Get Character Portrait from Zkillboard
        try:
            if not os.path.isfile("{}.png".format(characterId)):
                urllib.request.urlretrieve("https://images.evetech.net/characters/{}/portrait?size=256".format(characterId),
                                           os.path.join('profiles', "{}.png".format(characterId)))
            source_image = imageio.imread(os.path.join('profiles', "{}.png".format(characterId)))
        except urllib.error.HTTPError:
            source_image = imageio.imread(os.path.join('profiles', "default.png"))
        source_image = resize(source_image, (256, 256))[..., :3]

        # Split File into small Pieces
        split_size = 10
        input = VideoFileClip(os.path.join("input", filename))
        pieces = int(input.duration/split_size) + 1

        for x in range(0, pieces):
            start = x * split_size
            end = (x + 1) * split_size if (x + 1) * split_size < input.duration else input.duration
            subclip = concatenate_videoclips([input.subclip(0, 1/30), input.subclip(start, end)])
            subclip.write_videofile(os.path.join("input_snips", "{}_{}.mp4".format(filename.strip(".mp4"), x)))

        # Loop trough snips and animate
        for x in range(0, pieces):
            print("Animating", filename, x)
            # Get the snip
            driving_video = imageio.mimread(os.path.join("input_snips", "{}_{}.mp4".format(filename.strip(".mp4"), x)), memtest=False)

            # Resize video to 256x256
            driving_video = [resize(frame, (256, 256))[..., :3] for frame in driving_video]

            # Perform image animation
            predictions = make_animation(source_image, driving_video, generator, kp_detector, relative=True, cpu=False)

            imageio.mimsave(os.path.join("output_snips", "{}_{}.mp4".format(filename.strip(".mp4"), x)), [img_as_ubyte(frame) for frame in predictions], fps=30)

        # Concatenate snips
        video_pieces = []
        for x in range(0, pieces):
            print("Merging", filename, x)
            split = VideoFileClip(os.path.join("output_snips", "{}_{}.mp4".format(filename.strip(".mp4"), x)))
            video_pieces.append(split.subclip(1/30, split.duration))
        concatenate_videoclips(video_pieces).set_audio(input.audio).write_videofile(os.path.join("output", filename))

        # Move the Used Driving Video into the "Used" Folder
        # os.rename(os.path.join('input', filename), os.path.join('used', filename))
