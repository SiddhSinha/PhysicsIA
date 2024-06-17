import pygame
import sys
import math

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
BACKGROUND_COLOR = (255, 255, 255)
HOT_COLOR = (255, 0, 0)  # Red for hot temperature
MEDIUM_COLOR = (0, 255, 0)  # Green for medium temperature
COLD_COLOR = (0, 0, 255)  # Blue for cold temperature
FPS = 60
SPEED_FACTOR = 0.2  # Increase the speed factor for more noticeable differences
AMPLITUDE = 50  # Amplitude of the waves

# Speed of sound calculation
def speed_of_sound(temp_celsius):
    return 331.3 + 0.6 * temp_celsius

# Wavelength calculation
def calculate_wavelength(speed, frequency):
    return speed / frequency

# Draw sinusoidal wave
def draw_wave(screen, x_start, y_start, wavelength, speed, time_elapsed, color):
    points = []
    for x in range(WIDTH):
        y = int(y_start + AMPLITUDE * math.sin((2 * math.pi / wavelength) * (x - speed * SPEED_FACTOR * time_elapsed)))
        points.append((x, y))
    pygame.draw.lines(screen, color, False, points, 2)

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sound Wave Propagation Simulation")

# Clock for controlling the frame rate
clock = pygame.time.Clock()

# Temperatures and corresponding speeds of sound
temperatures = {'Hot': 30, 'Medium': 20, 'Cold': 10}
speeds = {key: speed_of_sound(temp) for key, temp in temperatures.items()}
frequencies = {'Hot': 262, 'Medium': 262, 'Cold': 262}
wavelengths = {key: calculate_wavelength(speeds[key], frequencies[key]) for key in temperatures}

# Print speed of sound and wavelength for each temperature
for temp in temperatures:
    speed = speeds[temp]
    wavelength = wavelengths[temp]
    print(f"Temperature: {temp}°C")
    print(f"Speed of Sound: {speed:.2f} m/s")
    print(f"Wavelength: {wavelength:.2f} m\n")

# Start position of the sound waves
time_elapsed = 0

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update time
    dt = clock.get_time() / 1000  # Delta time in seconds
    time_elapsed += dt

    # Clear screen
    screen.fill(BACKGROUND_COLOR)

    # Draw the sound waves
    draw_wave(screen, 0, HEIGHT // 4, wavelengths['Hot'], speeds['Hot'], time_elapsed, HOT_COLOR)
    draw_wave(screen, 0, HEIGHT // 2, wavelengths['Medium'], speeds['Medium'], time_elapsed, MEDIUM_COLOR)
    draw_wave(screen, 0, 3 * HEIGHT // 4, wavelengths['Cold'], speeds['Cold'], time_elapsed, COLD_COLOR)

    # Update display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(FPS)

pygame.quit()
sys.exit()