# Simple Pygame Interactive App

This is a basic Pygame application designed to demonstrate fundamental Pygame concepts such as event handling, drawing, text rendering, and interactive UI elements. The app features a clickable button that changes the background color, a score tracker, and a theme toggle between light and dark modes.

## Features

-   **Interactive "Click Me" Button**:
    -   Changes the main background color when clicked.
    -   Each click also increments the score.
-   **Score Display**:
    -   Shows the current score in the top-left corner.
    -   The score increases every time the "Click Me" button is pressed.
-   **Dark Mode / Light Mode Toggle**:
    -   A "Toggle Mode" button allows switching between a light theme and a dark theme.
    -   All UI elements (background, buttons, text) adapt to the selected theme.

## How to Run

1.  **Install Pygame**:
    If you don't have Pygame installed, open your terminal or command prompt and run:
    ```bash
    pip install pygame
    ```

2.  **Run the Application**:
    Navigate to the directory containing the `test.py` file and execute:
    ```bash
    python test.py
    ```

## Controls

-   **Click the "Click Me" button** (center of the screen):
    -   Changes the background color of the window.
    -   Increments your score by 1.
-   **Click the "Toggle Mode" button** (top-right of the screen):
    -   Switches the application's theme between light mode and dark mode.
-   **Close the window**:
    -   Clicking the standard window close button (e.g., the 'X') will quit the application.
