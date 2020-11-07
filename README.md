# First Order Motion Model for Image Animation

This repository contains an adpated version of the source code for the paper [First Order Motion Model for Image Animation](https://papers.nips.cc/paper/8935-first-order-motion-model-for-image-animation) for character animation in eve online. The original Paper was published by Aliaksandr Siarohin, [Stéphane Lathuilière](http://stelat.eu), [Sergey Tulyakov](http://stulyakov.com), [Elisa Ricci](http://elisaricci.eu/) and [Nicu Sebe](http://disi.unitn.it/~sebe/). If you are not an eve player, then please look at the [Original Repo](https://github.com/AliaksandrSiarohin/first-order-model). 

### Installation

This is meant for ```python3```. This means you need [python](https://www.python.org/) installed on your system to use any of it.

After you have installed python you are then able to download any required packages. I suggest you use a virtual enviroment for this.
Also one of the key requirements is "Torch" which can use GPU-Support. As such you should probably install torch with CUDA-Support, which requires you to have the corresponting [Toolkit](https://developer.nvidia.com/cuda-zone) preinstalled
If you don't want to use GPU-Acceleration, then set ``cpu = True`` in the `make_animation()` function call on Line 62 of `eve.py`. 
```
pip install -r requirements.txt
```


### Pre-trained checkpoint
So far there is a pretrained neural network for pictures of 256x256 Pixels by the original Repo. Ideally there would be options for bigger resolutions, but I did not come around to create some.


### Image animation

 In order to animate your own characters, follow these steps.
 
 1. Create a video with you talking your desired text in person, you should be in the center of the picture.
 2. Put that video into the `input` folder. In the name you should add `_{picture to animate}` at the end. If you put If you out `_{characterID}` at the end then the current profile picture of that character wil automatically be downloaded and you can skip the next step.
 3. Put the picture that should be animated into the `profiles` folder. 
 4. run `eve.py`
 5. collect the animated character from `òutput`. You might have to do some retouching, neural networks aren't perfect ;)


#### Additional notes

Citation of the Original Paper:

```
@InProceedings{Siarohin_2019_NeurIPS,
  author={Siarohin, Aliaksandr and Lathuilière, Stéphane and Tulyakov, Sergey and Ricci, Elisa and Sebe, Nicu},
  title={First Order Motion Model for Image Animation},
  booktitle = {Conference on Neural Information Processing Systems (NeurIPS)},
  month = {December},
  year = {2019}
}
```

