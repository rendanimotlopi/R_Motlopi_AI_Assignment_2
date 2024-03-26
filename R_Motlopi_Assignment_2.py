import pygame
import random
import math

# Constants
WIDTH = 800
HEIGHT = 600
NUM_BOIDS = 50
BOID_SPEED = 2
BOID_SIZE = 5
ALIGNMENT_FACTOR = 0.01
COHESION_FACTOR = 0.01
SEPARATION_FACTOR = 0.1
VIEW_RANGE = 50
AVOID_RADIUS = 20

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Boid class
class Boid:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vx = random.uniform(-BOID_SPEED, BOID_SPEED)
        self.vy = random.uniform(-BOID_SPEED, BOID_SPEED)

    def update(self, flock, obstacles):
        alignment = [0, 0]
        cohesion = [0, 0]
        separation = [0, 0]
        avoid = [0, 0]
        count = 0

        for boid in flock:
            if boid != self:
                d = self.distance(boid)
                if d < VIEW_RANGE:
                    alignment[0] += boid.vx
                    alignment[1] += boid.vy

                    cohesion[0] += boid.x
                    cohesion[1] += boid.y

                    separation[0] += (self.x - boid.x) / d
                    separation[1] += (self.y - boid.y) / d

                    if d < AVOID_RADIUS:
                        avoid[0] += (self.x - boid.x)
                        avoid[1] += (self.y - boid.y)
                        count += 1

        if count > 0:
            avoid[0] /= count
            avoid[1] /= count

        if count > 0:
            separation[0] /= count
            separation[1] /= count

        if len(flock) > 0:
            cohesion[0] /= len(flock)
            cohesion[1] /= len(flock)

        for obstacle in obstacles:
            d = self.distance(obstacle)
            if d < AVOID_RADIUS:
                avoid[0] += (self.x - obstacle[0])
                avoid[1] += (self.y - obstacle[1])
                count += 1

        if count > 0:
            avoid[0] /= count
            avoid[1] /= count

        self.vx += (alignment[0] * ALIGNMENT_FACTOR +
                     cohesion[0] * COHESION_FACTOR +
                     separation[0] * SEPARATION_FACTOR +
                     avoid[0])
        self.vy += (alignment[1] * ALIGNMENT_FACTOR +
                     cohesion[1] * COHESION_FACTOR +
                     separation[1] * SEPARATION_FACTOR +
                     avoid[1])

        speed = math.sqrt(self.vx ** 2 + self.vy ** 2)
        if speed > BOID_SPEED:
            self.vx = (self.vx / speed) * BOID_SPEED
            self.vy = (self.vy / speed) * BOID_SPEED

        self.x += self.vx
        self.y += self.vy

        if self.x > WIDTH:
            self.x = 0
        elif self.x < 0:
            self.x = WIDTH

        if self.y > HEIGHT:
            self.y = 0
        elif self.y < 0:
            self.y = HEIGHT

    def distance(self, obj):
        if isinstance(obj, Boid):
            return math.sqrt((self.x - obj.x) ** 2 + (self.y - obj.y) ** 2)
        elif isinstance(obj, tuple) and len(obj) == 2:
            return math.sqrt((self.x - obj[0]) ** 2 + (self.y - obj[1]) ** 2)
        else:
            raise ValueError("Invalid object type passed to distance method.")

# Initialize pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Rendani Motlopi AI Assignemt 2")

# Lists to hold boids and obstacles
boids = []
obstacles = []

# Main loop
running = True
while running:
    screen.fill(WHITE)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left click for boid
                boids.append(Boid(event.pos[0], event.pos[1]))
            elif event.button == 3:  # Right click for obstacle
                obstacles.append(event.pos)

    # Update and draw boids
    for boid in boids:
        boid.update(boids, obstacles)
        pygame.draw.circle(screen, BLACK, (int(boid.x), int(boid.y)), BOID_SIZE)

    # Draw obstacles
    for obstacle in obstacles:
        pygame.draw.circle(screen, RED, obstacle, BOID_SIZE)

    pygame.display.flip()

    # Cap the frame rate
    pygame.time.Clock().tick(60)

pygame.quit()
