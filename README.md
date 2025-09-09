# Integer Multiplication and Division Flashcards

This project is a **hybrid Python + React web app** that generates and
displays flashcards for practicing multiplication and division of
integers.

## Overview

-   **Backend (Python + Sympy):**
    -   Generates 200 flashcards covering four cases:
        1.  Multiplying like signs (product positive)
        2.  Multiplying unlike signs (product negative)
        3.  Dividing like signs (quotient positive)
        4.  Dividing unlike signs (quotient negative)
    -   Ensures that:
        -   Multiplicand and multiplier are nonzero integers in \[-15,
            15\].
        -   Division problems always result in integer quotients.
    -   Exports the flashcards as `public/flashcards.json`.
-   **Frontend (React):**
    -   Loads the pre-generated `flashcards.json` file.
    -   Randomly selects 10 flashcards per quiz set.
    -   Displays flashcards with smooth animations and user-friendly UI.
    -   Collects user input and checks answers against the pre-generated
        solution.
    -   Shows score and answer key at the end of the quiz.

## File Structure

    project-root/
    â”‚
    â”œâ”€â”€ generate_flashcards.py     # Python script to generate flashcards JSON
    â”œâ”€â”€ public/
    â”‚   â””â”€â”€ flashcards.json        # Generated flashcards (200 total)
    â”œâ”€â”€ src/
    â”‚   â””â”€â”€ components/Flashcards  # React components for flashcard UI
    â””â”€â”€ README.md

## Usage

### 1. Generate Flashcards

Run the Python script to generate 200 flashcards:

``` bash
python generate_flashcards.py
```

This will create `public/flashcards.json`.

### 2. Run React App

Start the development server:

``` bash
npm start
```

The React app will load `flashcards.json`, select random flashcards, and
render the interactive flashcard quiz.

## Cases Covered

1.  **Multiplying like signs**\
    Example: (-2) Ã— (-4) = 8

2.  **Multiplying unlike signs**\
    Example: 3 Ã— (-5) = -15

3.  **Dividing like signs**\
    Example: (-24) Ã· (-6) = 4

4.  **Dividing unlike signs**\
    Example: 24 Ã· (-6) = -4

## Notes

-   Negatives are always shown in parentheses for clarity.
-   Dividends are guaranteed to be divisible by divisors to ensure
    integer results.
-   Flashcards are pre-generated, ensuring consistent math logic on the
    backend and simple rendering on the frontend.

## License

This project is open-source and available under the MIT License.