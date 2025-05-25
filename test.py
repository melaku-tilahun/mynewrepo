import pygame

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Color Palettes
light_mode_colors = {
    "background": (200, 200, 200),  # Light Gray
    "background_alt": (144, 238, 144), # Light Green
    "button": (0, 0, 255),  # Blue
    "button_text": (255, 255, 255),  # White
    "score_text": (0, 0, 0),  # Black
    "toggle_button": (100, 100, 100), # Medium Gray
    "toggle_button_text": (255, 255, 255) # White
}

dark_mode_colors = {
    "background": (50, 50, 50),  # Dark Gray
    "background_alt": (0, 100, 0), # Dark Green
    "button": (173, 216, 230),  # Light Blue
    "button_text": (0, 0, 0),  # Black
    "score_text": (255, 255, 255),  # White
    "toggle_button": (200, 200, 200), # Light Gray
    "toggle_button_text": (0, 0, 0) # Black
}

# Current mode and colors
current_mode = "light"
active_colors = light_mode_colors
background_color = active_colors["background"] # Initial background

# Score
score = 0

# "Click Me" Button properties
CLICK_ME_BUTTON_WIDTH = 200
CLICK_ME_BUTTON_HEIGHT = 50
CLICK_ME_BUTTON_X = (SCREEN_WIDTH - CLICK_ME_BUTTON_WIDTH) // 2
CLICK_ME_BUTTON_Y = (SCREEN_HEIGHT - CLICK_ME_BUTTON_HEIGHT) // 2
# CLICK_ME_BUTTON_COLOR will be from active_colors
CLICK_ME_BUTTON_TEXT = "Click Me"
# CLICK_ME_BUTTON_TEXT_COLOR will be from active_colors

# Create "Click Me" button rectangle
click_me_button_rect = pygame.Rect(CLICK_ME_BUTTON_X, CLICK_ME_BUTTON_Y, CLICK_ME_BUTTON_WIDTH, CLICK_ME_BUTTON_HEIGHT)

# "Toggle Mode" Button properties
TOGGLE_BUTTON_WIDTH = 150
TOGGLE_BUTTON_HEIGHT = 40
TOGGLE_BUTTON_X = SCREEN_WIDTH - TOGGLE_BUTTON_WIDTH - 10 # Top-right
TOGGLE_BUTTON_Y = 10
# TOGGLE_BUTTON_COLOR will be from active_colors
TOGGLE_BUTTON_TEXT = "Toggle Mode"
# TOGGLE_BUTTON_TEXT_COLOR will be from active_colors

# Create "Toggle Mode" button rectangle
toggle_button_rect = pygame.Rect(TOGGLE_BUTTON_X, TOGGLE_BUTTON_Y, TOGGLE_BUTTON_WIDTH, TOGGLE_BUTTON_HEIGHT)

# Font
pygame.font.init() # Initialize font module explicitly, though pygame.init() does this
try:
    font = pygame.font.Font(None, 36) # Use default system font, size 36
except Exception as e:
    print(f"Font loading failed: {e}")
    font = pygame.font.Font(pygame.font.get_default_font(), 36) # Fallback


# Create the game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pygame App with Button")

# Main game loop
running = True
while running:
    # Update active colors based on current mode
    if current_mode == "light":
        active_colors = light_mode_colors
    else:
        active_colors = dark_mode_colors

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button
                mouse_pos = pygame.mouse.get_pos()
                # Check "Click Me" button
                if click_me_button_rect.collidepoint(mouse_pos):
                    background_color = active_colors["background_alt"] # Change background color
                    score += 1 # Increment score
                # Check "Toggle Mode" button
                elif toggle_button_rect.collidepoint(mouse_pos):
                    if current_mode == "light":
                        current_mode = "dark"
                        background_color = dark_mode_colors["background"] # Update bg immediately
                    else:
                        current_mode = "light"
                        background_color = light_mode_colors["background"] # Update bg immediately


    # Fill the screen
    # If background_color hasn't been changed by "Click Me", set it to current mode's default
    if background_color != active_colors["background_alt"]:
        background_color = active_colors["background"]
    screen.fill(background_color)

    # Draw the "Click Me" button
    pygame.draw.rect(screen, active_colors["button"], click_me_button_rect)

    # Render and blit "Click Me" button text
    click_me_text_surface = font.render(CLICK_ME_BUTTON_TEXT, True, active_colors["button_text"])
    click_me_text_rect = click_me_text_surface.get_rect(center=click_me_button_rect.center)
    screen.blit(click_me_text_surface, click_me_text_rect)

    # Draw the "Toggle Mode" button
    pygame.draw.rect(screen, active_colors["toggle_button"], toggle_button_rect)

    # Render and blit "Toggle Mode" button text
    toggle_text_surface = font.render(TOGGLE_BUTTON_TEXT, True, active_colors["toggle_button_text"])
    toggle_text_rect = toggle_text_surface.get_rect(center=toggle_button_rect.center)
    screen.blit(toggle_text_surface, toggle_text_rect)

    # Render and blit score text
    score_surface = font.render(f"Score: {score}", True, active_colors["score_text"])
    score_rect = score_surface.get_rect(topleft=(10, 10)) # Position at top-left
    screen.blit(score_surface, score_rect)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.font.quit() # Uninitialize font module
pygame.quit()
