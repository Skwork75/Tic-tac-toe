import tkinter as tk
from tkinter import messagebox, simpledialog
import random

class TicTacToeGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Tic Tac Toe - Saurabh Kumar")

        self.current_player = random.choice(["X", "O"])
        self.board_state = ["" for _ in range(9)]
        self.tiles = []

        self.score_x = 0
        self.score_o = 0
        self.total_rounds = 1
        self.current_round = 1

        self.setup_ui()
        self.display_turn()

    def setup_ui(self):
        self.info_label = tk.Label(self.master, text="", font=("Arial", 14))
        self.info_label.pack(pady=10)

        self.grid_frame = tk.Frame(self.master)
        self.grid_frame.pack()

        for pos in range(9):
            btn = tk.Button(self.grid_frame, text="", font=("Arial", 20), width=6, height=3,
                            command=lambda pos=pos: self.on_tile_click(pos))
            btn.grid(row=pos//3, column=pos%3)
            self.tiles.append(btn)

        self.reset_btn = tk.Button(self.master, text="Start New Match", command=self.start_new_match)
        self.reset_btn.pack(pady=10)

    def on_tile_click(self, idx):
        if self.board_state[idx] == "":
            self.board_state[idx] = self.current_player
            self.tiles[idx].config(text=self.current_player)

            if self.check_for_winner():
                self.handle_win(f"{self.current_player} wins Round {self.current_round}!")
                return

            if "" not in self.board_state:
                self.handle_win("This round is a draw!")
                return

            self.current_player = "O" if self.current_player == "X" else "X"
            self.display_turn()

    def check_for_winner(self):
        wins = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                (0, 3, 6), (1, 4, 7), (2, 5, 8),
                (0, 4, 8), (2, 4, 6)]
        for a, b, c in wins:
            if self.board_state[a] == self.board_state[b] == self.board_state[c] != "":
                return True
        return False

    def handle_win(self, msg):
        if self.current_player == "X":
            self.score_x += 1
        else:
            self.score_o += 1

        messagebox.showinfo("Round Result", msg)
        self.current_round += 1

        if self.current_round > self.total_rounds:
            self.declare_final_winner()
        else:
            self.reset_board()

    def reset_board(self):
        self.board_state = ["" for _ in range(9)]
        for btn in self.tiles:
            btn.config(text="")
        self.current_player = random.choice(["X", "O"])
        self.display_turn()

    def start_new_match(self):
        self.score_x = 0
        self.score_o = 0
        self.current_round = 1
        self.total_rounds = self.get_round_count()
        self.reset_board()

    def get_round_count(self):
        try:
            count = int(simpledialog.askstring("Rounds", "Enter number of rounds to play:"))
            return max(1, count)
        except:
            return 1

    def declare_final_winner(self):
        if self.score_x > self.score_o:
            result_msg = "Player X wins the match!"
        elif self.score_o > self.score_x:
            result_msg = "Player O wins the match!"
        else:
            result_msg = "It's a tie match!"

        result_msg += f"\nFinal Score:\nX: {self.score_x}  O: {self.score_o}"
        messagebox.showinfo("Match Result", result_msg)
        self.start_new_match()

    def display_turn(self):
        self.info_label.config(text=f"Round {self.current_round} / {self.total_rounds} - {self.current_player}'s turn")


if __name__ == '__main__':
    window = tk.Tk()
    game_app = TicTacToeGUI(window)
    window.mainloop()
