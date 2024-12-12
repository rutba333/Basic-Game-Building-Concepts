import pygame

# Initialize pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pygame Game Screen")

# Font setup
font = pygame.font.Font(None, 74)  # None for default font, 74 for size

# Game loop variables
running = True

while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False



 # Fill the screen with a background color
    screen.fill(WHITE)

    # Draw a rectangle
    pygame.draw.rect(screen, RED, (150, 200, 200, 100))  # (x, y, width, height)

    # Render text
    text = font.render("This is a rectangle!!", True, BLACK)
    screen.blit(text, (250, 100))  # Position the text

    # Update the display
    pygame.display.flip()

# Quit pygame
pygame.quit()
