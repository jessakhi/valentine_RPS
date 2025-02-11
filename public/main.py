import random
import tkinter as tk
import time

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def get_winner(player, computer):
    if player == computer:
        return "It's a tie! 💕"
    elif (player == "rock" and computer == "scissors") or \
         (player == "scissors" and computer == "paper") or \
         (player == "paper" and computer == "rock"):
        return "You win! ❤️ Here's a Valentine for you! 💌"
    else:
        return "You lose! But I'll still be your Valentine! 😊"

def play_game(player_choice):
    result_label.config(text="Rock...", fg="black")
    root.update()
    time.sleep(0.5)
    
    result_label.config(text="Paper...", fg="black")
    root.update()
    time.sleep(0.5)
    
    result_label.config(text="Scissors...", fg="black")
    root.update()
    time.sleep(0.5)
    
    computer_choice = get_computer_choice()
    result = get_winner(player_choice, computer_choice)
    result_label.config(text=f"Your choice: {player_choice} \nComputer's choice: {computer_choice}\n\n{result}", fg="red")

def create_ui():
    global result_label, root
    root = tk.Tk()
    root.title("Valentine's Rock Paper Scissors")
    root.geometry("333x424")
    
    tk.Label(root, text="Choose Rock, Paper, or Scissors!", font=("Arial", 14)).pack(pady=10)
    
    btn_frame = tk.Frame(root)
    btn_frame.pack()
    
    tk.Button(btn_frame, text="Rock", font=("Arial", 12), command=lambda: play_game("rock")).pack(side=tk.LEFT, padx=10)
    tk.Button(btn_frame, text="Paper", font=("Arial", 12), command=lambda: play_game("paper")).pack(side=tk.LEFT, padx=10)
    tk.Button(btn_frame, text="Scissors", font=("Arial", 12), command=lambda: play_game("scissors")).pack(side=tk.LEFT, padx=10)
    
    result_label = tk.Label(root, text="", font=("Arial", 12), fg="red")
    result_label.pack(pady=20)
    
    root.mainloop()

# Run the UI
create_ui()