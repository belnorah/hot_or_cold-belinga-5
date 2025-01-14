# hot_or_cold-belinga-5
# Hot or Cold Game
The **Hot or Cold** game is a fun guessing game where players identify a hidden number within a range using clues. A player picks a number, and the guesser gets "Warmer" if closer or "Colder" if farther from it. The game continues until the number is guessed.

---

## Installation

### Prerequisites
- Python 3.7 or later installed on your machine.

### Steps
1. Clone the repository:
   ```bash
   git clone git@github.com:belnorah/hot_or_cold-belinga-5.git
   cd hot_or_cold-belinga-5
   ```

2. (Optional) Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```


3. Run the game:
   ```bash
   python src/game.py
   ```

---

## How to Play
1. The game randomly selects a target number within a predefined range 1 to 100.
2. Players make guesses and receive feedback:
    - "Hotter": The guess is closer to the target number.
    - "Colder": The guess is farther from the target number.
3. Continue guessing until the target number is correctly identified.
4. The game tracks the number of attempts and displays a summary at the end.

Optional variations:
- Set a maximum number of attempts.
- Use different ranges for difficulty levels.

---

## Contributing
We welcome contributions to improve and extend the game!

### How to Contribute
1. Fork the repository.
2. Clone your forked repository locally:
   ```bash
   git clone https://github.com/{your-username}/hot_or_cold-belinga-5.git
   cd hot_or_cold-belinga-5
   ```
3. Create a new branch for your feature or bugfix:
   ```bash
   git checkout -b my-feature-branch
   ```
4. Make your changes and commit them with a clear message:
   ```bash
   git commit -m "Add feature XYZ"
   ```
5. Push your changes to your forked repository:
   ```bash
   git push origin my-feature-branch
   ```
6. Open a pull request to the main repository.

### Guidelines
- Ensure your code is well-documented and follows Python best practices.
- Write tests for new features or bug fixes.
- Keep pull requests focused and concise.

---

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.
