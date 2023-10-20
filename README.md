
![Logo](https://images.fineartamerica.com/images/artworkimages/mediumlarge/3/stand-with-palestine-tinh-tran-le-thanh.jpg)


# DeepRacer-For-Cloud-Alyamaan619 🚘 

"DeepRacer For Cloud" is an impressive environment dimension instead of training the AWS DeepRacer robot car (https://aws.amazon.com/deepracer) on the console by training on either a cloud virtual machine or a local computer.

Using the Windows sub-system Linux (WSL), this repository was trained locally on Ubuntu.
## Run Locally 💻

Before the following steps, you must install "Docker desktop" for images to be generated and "Ubuntu 20.04" CLI for running on, use the video as guide to install these requirements (https://youtu.be/g-bVnm-6poU?si=Xdqa7mcel1Jdrmj-).

                                  ------ After that ------ 

Clone the project

```bash
  git clone https://github.com/Yousuf-Omran/deepracer-for-cloud-Alyamaan619
```

Go to the project directory

```bash
  cd deepracer-for-cloud-Alyamaan619
```

Activate and run the environment

```bash
  . bin/activate.sh run.env
```

Upload the reward function code and the other related filed located in custom files

```bash
  dr-upload-custom-files
```

Start training

```bash
  dr-start-training -w
```

View your training robot car

```bash
  dr-start-viewer 
```
After finishing, stop the training

```bash
  dr-stop-training 
```

Evaluate your model

```bash
  dr-start-evaluation
```
I recommend you to visit and use "deepracer-analysis" repository (https://github.com/aws-deepracer-community/deepracer-analysis) to evaluate your model performance.

## Contribution ✔️  

- Using two main inputs speed and steering angle to impact on the reward.
- Speed: speed input ranges from 0.5 ~ 1 m/s, to gain highly reward the fifth degree equation (x^5) had been used where x is the speed input.
- Steering angle: it ranges from -30 ~ 30 degrees, using a proper exponential equation (e^-y) to reduce the reward of steering angle increment, where y is the steering angle input.

- Combining two inputs by summing to get the target reward
- Giving a bonus to the car if it stays on the left side of a track.
- Giving a punishment to the car if it dosn't drive on the right side of a track at specific S-shaped curve located on the track.

#### You can see inputs visualization by openning the "2D inputs.ggb" and "3D inputs combination.ggb" files located above on the Geogebra site (https://www.geogebra.org/calculator).

#### You can reach my own code by clicking on "custom_files" then "reward_function.py".




## Limitation 💢
- The hyperparameters at the "AWS DeepRacer Student League" are restricted and identefied to specific values unlike that exist in "AWS DeepRacer" 
- You should have a powerful computer hardware to run smoothly on.

- You should have some knoledge on Linux commands.
- Sometimes the you need to create your own server to mitigate errors.

## Video 🎬 

A brief video of the learning journey will be included soon...
## Achievement 💯 

......................

## Links 🔗 

#### If you have any questions or feedback don't hesitate and reach out to me via email: yousufomran619@gmail.com

#### Or via my LinkedIn account:

[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/yousuf-omran-5b2884243/)



