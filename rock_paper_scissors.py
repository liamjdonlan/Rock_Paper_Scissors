import tkinter as tk
import random

SIZE = "400x125" 
ANSWERS = {"rock": {"rock": "tie", "paper": "louse", "scissors": "win"},
           "paper": {"rock": "win", "paper": "tie", "scissors": "louse"},
           "scissors": {"rock": "louse", "paper": "win", "scissors": "tie"}}


def display_result(player_guess: str, computer_guess: str, frame: object) -> None:
    frame.destroy()
    answer = ANSWERS[player_guess][computer_guess]
    game_screen = tk.Frame()
    result_text = tk.Label(text=f"You {answer}", master=game_screen)
    # play_again_button = tk.Button(text="Play again?", master=game_screen, command= lambda player_answer(game_screen))

    result_text.pack(fill = tk.BOTH)
    # play_again_button.pack(fill = tk.BOTH)
    game_screen.pack(fill = tk.BOTH)

def computer_answer(player_guess: str, frame: object) -> None:
    frame.destroy()
    computer_guess = random.choice(["rock", "paper", "scissors"])
    
    game_screen = tk.Frame()
    choice_text = tk.Label(text=f"I choose {computer_guess}.", master=game_screen)
    continue_button = tk.Button(text="continue", master=game_screen, command = lambda: display_result(player_guess, computer_guess, game_screen))
    
    game_screen.pack(fill=tk.BOTH)
    choice_text.pack(fill=tk.BOTH)
    continue_button.pack(fill=tk.BOTH)
    


def player_answer(frame=None) -> None:
    """
    Makes a window that will ask player wheather they choose rock paper or scissors
    """
    if frame != None:
        frame.destory()

    game_screen = tk.Frame()
    game_text = tk.Label(text="Please choose Rock, Paper, or Scissors:", master=game_screen)
    rock_button = tk.Button(text="Rock", master=game_screen, command= lambda: computer_answer("rock", game_screen))
    paper_button = tk.Button(text="Paper", master=game_screen, command= lambda: computer_answer("paper", game_screen))
    scissors_button = tk.Button(text="Scissors", master=game_screen, command= lambda: computer_answer("scissors", game_screen))

    game_text.pack(fill=tk.BOTH)
    rock_button.pack(fill=tk.BOTH)
    paper_button.pack(fill=tk.BOTH)
    scissors_button.pack(fill=tk.BOTH)
    game_screen.pack(fill=tk.BOTH)

    tk.mainloop()


window = tk.Tk()
window.geometry(SIZE)

player_answer()
