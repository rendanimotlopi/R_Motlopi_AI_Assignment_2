# R_Motlopi_AI_Assignment_2
Application of swarm intelligence in boids
## Introduction
The Boids simulation is a computer model of coordinated motion developed by Craig Reynolds in 1986. It simulates the flocking behavior of birds, schooling behavior of fish, and herding behavior of animals by representing them as individual agents, called "boids."

The word "boid" is derived from "bird-oid object," but it's a generic term used to represent any entity in the simulation, not just birds.

The key idea behind the Boids simulation is that complex group behavior can emerge from simple individual rules that each boid follows. These rules are based on three main principles:

1. Separation: Each boid tries to maintain a minimum distance from its neighbors to avoid collisions.
2. Alignment: Each boid tries to align its direction with that of its neighbors.
3. Cohesion: Each boid tries to move towards the center of mass of its neighbors.
## Boids Techniques.
1. Behavioral Rules: Boids rely on simple behavioral rules that each agent follows to achieve complex group behavior. These rules typically include separation, alignment, and cohesion, as described earlier. Additional rules may be added to model specific behaviors or characteristics.

2. Simulation Environment: Boids simulations often take place within a virtual environment that provides boundaries, obstacles, and other spatial features. The environment influences the behavior of the agents and affects their interactions with each other.

3. Agent Representation: Each agent (boid) in the simulation is represented as an individual entity with properties such as position, velocity, and orientation. Agents may have other attributes, such as vision range or communication abilities, depending on the specific application.

4. Spatial Partitioning: To optimize performance in large-scale simulations, techniques such as spatial partitioning may be employed. Spatial partitioning divides the simulation space into smaller regions, allowing for efficient neighbor searches and interactions between agents.

5. Steering Behaviors: In addition to the basic rules of separation, alignment, and cohesion, Boids simulations may incorporate additional steering behaviors to model more complex movements. These behaviors include seeking a target, avoiding obstacles, following paths, and evading predators.

6. Parameter Tuning: Fine-tuning the parameters of the behavioral rules and simulation environment is crucial for achieving realistic and desired collective behaviors. Adjusting parameters such as vision range, speed, and influence weights can significantly impact the outcome of the simulation.

## Implemetation
The program implementation focuses on creating a user-friendly simulation of boids using Python and the pygame library. The simulation adheres to the three fundamental rules of boids: alignment, separation, and cohesion. Graphics and Visualization techniques were utilized to provide users with a visually interactive experience, depicting boids and obstacles using rendered colours, Black and red . The implementation is based on techniques such as the Rule-based approach, Simulation Time Step (STP), and Graphics & Visualization. The code, sourced from Shiffman, was modified to incorporate Steering Behavior for obstacle avoidance and directional movement. Challenges were encountered in implementing circular obstacle walls, but the core game rules were faithfully incorporated. While the dynamic removal of obstacles wasn't fully realized, the simulation effectively captures the essence of the boids game.
## Video simulation-code

[![Watch the video](https://img.shields.io/badge/Watch%20the%20video-Click%20here-red)](https://www.youtube.com/watch?v=L_K1ymxrH2s)
For more information regarding code explanation please check the word document attacked on efundi under implementation sub heading.

## How to run the code
1. Make sure that Python and Pygame are installed on your local machine.
2. You can install pygame via pip: pip install pygame
3. Copy the prodided code on my Github and pasted it on your python IDE, then have fun.

## References

Shiffman, Daniel. "The Coding Train." YouTube channel. Available online: https://www.youtube.com/user/shiffman
