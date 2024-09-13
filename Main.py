import random
from IPython.display import display, clear_output
import ipywidgets as widgets

# Game variables
total_money = 0
score = 0
dice1 = 0
dice2 = 0
bid_amount = 0

# Widgets
money_input = widgets.BoundedIntText(value=100, min=1, description='Total Money:')
bid_input = widgets.BoundedIntText(value=0, min=1, description='Bid Amount:')
dice1_label = widgets.Label(value="?")
dice2_label = widgets.Label(value="?")
score_label = widgets.Label(value="Score: 0")
money_label = widgets.Label(value="Money: 0")
result_label = widgets.Label(value="")
up_button = widgets.Button(description="7 Up")
down_button = widgets.Button(description="7 Down")
seven_button = widgets.Button(description="7")
end_game_button = widgets.Button(description="End Game", button_style='danger')

# Function to roll the dice
def roll_dice():
    global dice1, dice2
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    dice1_label.value = str(dice1)
    dice2_label.value = str(dice2)

# Function to handle button clicks
def on_button_click(button):
    global total_money, score, bid_amount
    clear_output(wait=True)

    # Check if the bid is valid
    bid_amount = bid_input.value
    if bid_amount > total_money:
        result_label.value = "Error: Not enough money to place this bet!"
    else:
        roll_dice()
        total = dice1 + dice2

        # Determine if the guess is correct
        if (button == up_button and total > 7) or (button == down_button and total < 7) or (button == seven_button and total == 7):
            score += 1
            total_money += bid_amount  # Double the bid amount if won
            result_label.value = f"Correct! You won ${bid_amount}. Total money: ${total_money}."
        else:
            score -= 1
            total_money -= bid_amount  # Deduct the bid amount if lost
            result_label.value = f"Wrong! You lost ${bid_amount}. Total money: ${total_money}."

    # Update UI
    score_label.value = "Score: " + str(score)
    money_label.value = "Money: $" + str(total_money)
    if total_money <= 0:
        result_label.value = "Game Over! You're out of money."
        disable_buttons()

    # Display updated components
    display_game()

# Function to end the game
def on_end_game_click(button):
    clear_output(wait=True)
    result_label.value = "Game ended by the user."
    display_game()

# Function to disable buttons. This is called when the user cannot play any more.
def disable_buttons():
    up_button.disabled = True
    down_button.disabled = True
    seven_button.disabled = True
    bid_input.disabled = True

# Function to start the game. This is the actual function to start the game when the user clicks start_button.
def start_game():
    global total_money
    total_money = money_input.value
    money_label.value = "Money: $" + str(total_money)
    result_label.value = "Game started! Place your bid and make a guess."
    display_game()

# Display all the game elements. This display widgets after the start button is clicked.
def display_game():
    display(dice1_label, dice2_label, score_label, money_label, result_label)
    display(bid_input, up_button, down_button, seven_button)
    display(end_game_button)

# Attach click handlers to buttons
up_button.on_click(on_button_click)
down_button.on_click(on_button_click)
seven_button.on_click(on_button_click)
end_game_button.on_click(on_end_game_click)

# Start the game. Initially this are the input text box and button visible
display(money_input)
start_button = widgets.Button(description="Start Game", button_style='success')
display(start_button)

# Attach start game handler
def on_start_click(button):
    clear_output(wait=True) # Clear the output that is present on the screen. That is this clears the start button and input box when money input was taken.
    start_game()

start_button.on_click(on_start_click)

