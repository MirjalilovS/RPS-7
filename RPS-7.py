from flask import Flask, render_template, request, redirect, url_for
import random

app = Flask(__name__)

elements = ["Rock", "Paper", "Scissors", "Water", "Fire", "Air", "Sponge"]

# Define the rules
define_rules = {
    "Rock": ["Scissors", "Fire", "Sponge"],
    "Paper": ["Rock", "Air", "Water"],
    "Scissors": ["Paper", "Air", "Sponge"],
    "Water": ["Fire", "Rock", "Scissors"],
    "Fire": ["Scissors", "Paper", "Air"],
    "Air": ["Water", "Rock", "Fire"],
    "Sponge": ["Paper", "Water", "Air"]
}

def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "Tie"
    elif computer_choice in define_rules[player_choice]:
        return "Player Wins"
    else:
        return "Computer Wins"

@app.route("/")
def index():
    return render_template("index.html", elements=elements)

@app.route("/play", methods=["POST"])
def play():
    player_choice = request.form.get("element")
    computer_choice = random.choice(elements)
    result = determine_winner(player_choice, computer_choice)
    return render_template("result.html", player_choice=player_choice, computer_choice=computer_choice, result=result)

if __name__ == "__main__":
    app.run(debug=True)