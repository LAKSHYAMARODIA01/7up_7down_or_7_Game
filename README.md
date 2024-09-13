
# 7up_7down or 7

This is a simple dice betting game called **7up_7down or 7**, where players place bets on the sum of two dice. Players can choose to bet whether the sum will be above, below, or exactly equal to 7. The game starts with a set amount of money, and the player wins or loses based on the outcome of each roll.

## Features
- Players start with a default total money balance (can be changed).
- Players can place a bid amount for each round.
- The game provides three betting options:
  - **7 Up**: Bet that the sum of two dice will be greater than 7.
  - **7 Down**: Bet that the sum of two dice will be less than 7.
  - **7**: Bet that the sum will exactly equal 7.
- Winning a bet doubles the player's bid amount, while losing deducts the bid from the total money.
- The game ends automatically if the player runs out of money or manually by pressing the "End Game" button.

## Prerequisites
- Python 3.x
- `ipywidgets` for interactive UI elements in Jupyter Notebooks.
- `IPython.display` for clearing and updating the output dynamically.

You can install the required package using:
```
pip install ipywidgets
```

## How to Play
1. **Start the Game**:
   - Run the script in a Jupyter Notebook environment.
   - You will be prompted to input the starting amount of money (default is 100).
   - Click the `Start Game` button to begin.

2. **Place a Bid**:
   - Enter your desired bid amount in the `Bid Amount` field.
   - Choose your bet by clicking one of the buttons:
     - **7 Up**: Bet that the sum of the dice will be greater than 7.
     - **7 Down**: Bet that the sum of the dice will be less than 7.
     - **7**: Bet that the sum will exactly equal 7.

3. **Dice Roll**:
   - The dice will roll automatically after placing a bet.
   - If you win, the bid amount is added to your total money. If you lose, the bid amount is subtracted.
   - The game updates your score and total money after each round.

4. **Game End**:
   - The game ends if your total money drops to zero.
   - You can also end the game manually by clicking the `End Game` button.

## UI Elements
- **Total Money**: Displays the player's remaining money.
- **Bid Amount**: Input field where the player sets the bid for each round.
- **Dice Values**: Two labels showing the result of each dice roll.
- **Score**: Displays the player's score, which increases when a bet is won and decreases when a bet is lost.
- **Result Message**: Displays a message indicating whether the player won or lost the round.
- **End Game**: A button to end the game manually at any time.

  ## Screenshot:-
  ![s1](https://github.com/user-attachments/assets/42264ff8-25d3-425b-9e95-5937347fa4ad)
  <br>
  ![s2](https://github.com/user-attachments/assets/3cf59eb8-2e8f-4737-9ca3-c15219bc70fa)
  <br>
  ![s3](https://github.com/user-attachments/assets/fa8cff0b-0ac1-4201-8809-6a8a60acf67e)
  <br>
  ![s4](https://github.com/user-attachments/assets/e2419dd8-a239-4924-a6d5-4c531ecc4620)




  
