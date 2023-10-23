
![Logo](https://images.fineartamerica.com/images/artworkimages/mediumlarge/3/stand-with-palestine-tinh-tran-le-thanh.jpg)


# DeepRacer-For-Cloud-Alyamaan619 🚘 

"DeepRacer For Cloud" is an impressive environment dimension instead of training the AWS DeepRacer robot car (https://aws.amazon.com/deepracer) on the console by training on either a cloud virtual machine or a local computer.

Using the Windows sub-system Linux (WSL), this repository was trained locally on Ubuntu.
## Run Locally 💻

Before the following steps, you must install "Docker desktop" for images to be generated and "Ubuntu 20.04" CLI for running on, use the video as a guide to install these requirements (https://youtu.be/g-bVnm-6poU?si=Xdqa7mcel1Jdrmj-).

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

Upload the reward function code and the other related files located in custom files
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
I recommend you visit and use the "deepracer-analysis" repository (https://github.com/aws-deepracer-community/deepracer-analysis) to evaluate your model performance.

## Contribution ✔️  

- Using two main inputs speed and steering angle to impact the reward.
- Speed: speed input ranges from 0.5 ~ 1 m/s, to gain highly reward the fifth degree equation (x^5) had been used where x is the speed input.
- Steering angle: it ranges from -30 ~ 30 degrees, using a proper exponential equation (e^-y) to reduce the reward of steering angle increment, where y is the steering angle input.

- Combining two inputs by summing to get the target reward
- Giving a bonus to the car if it stays on the left side of a track.
- Punishing the car if it doesn't drive on the right side of a track at a specific S-shaped curve in 67~99 waypoints.

#### You can see inputs visualization by opening the "2D inputs.ggb" and "3D inputs combination.ggb" files located above on the Geogebra site (https://www.geogebra.org/calculator).

#### You can reach my code by clicking on "custom_files" then "reward_function.py".




## Limitation 💢
- The hyperparameters at the "AWS DeepRacer Student League" are restricted and identified to specific values unlike that exist in "AWS DeepRacer" 
- You should have powerful computer hardware to run smoothly on.

- You should have some knowledge of Linux commands.
- Sometimes you need to create your server to mitigate errors.

## Video 🎬 

You can watch my steps in training and evaluating from the beginning till the end in the video on my drive link below: 

https://drive.google.com/drive/folders/1Rbuz_sc2Bda4KIW4eH2rQoFe5X3zYs9a?usp=sharing
## Achievement 💯 
On October 23, 2023, I stand as:
- 1st place in Egypt,
 
- 3rd place in the Middle East and Africa,

- 40th place in the World.
  
![image](https://github.com/Yousuf-Omran/deepracer-for-cloud-Alyamaan619/assets/134161427/f3506a2d-471a-4933-989a-741059978bef)


This race track will be closed in March 2024, so there is a lot of time to join the competition and upscale your skills in reinforcement learning...

## Links 🔗 

#### If you have any questions or feedback don't hesitate and reach out to me via email: yousufomran619@gmail.com

#### Or via my LinkedIn account:

[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/yousuf-omran-5b2884243/)



