import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, root):
        """
        Inicializa el juego de Tic-Tac-Toe.
        """
        self.root = root
        self.root.title("Tic-Tac-Toe")
        self.board = [""] * 9
        self.current_player = "X"
        self.buttons = []
        self.create_board()

    def create_board(self):
        """
        Crea el tablero de Tic-Tac-Toe.
        """
        for i in range(9):
            button = tk.Button(self.root, text="", font="Arial 20", width=5, height=2,
                               command=lambda i=i: self.on_button_click(i))
            button.grid(row=i//3, column=i%3)
            self.buttons.append(button)

    def on_button_click(self, index):
        """
        Maneja el evento de clic en un botón del tablero.
        """
        if self.board[index] == "":
            self.board[index] = self.current_player
            self.buttons[index].config(text=self.current_player)
            if self.check_winner():
                messagebox.showinfo("Tic-Tac-Toe", f"Player {self.current_player} wins!")
                self.reset_board()
            elif "" not in self.board:
                messagebox.showinfo("Tic-Tac-Toe", "It's a tie!")
                self.reset_board()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"

    def check_winner(self):
        """
        Verifica si hay un ganador.
        """
        winning_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],
            [0, 3, 6], [1, 4, 7], [2, 5, 8],
            [0, 4, 8], [2, 4, 6]
        ]
        for combo in winning_combinations:
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] != "":
                return True
        return False

    def reset_board(self):
        """
        Reinicia el tablero de juego.
        """
        self.board = [""] * 9
        for button in self.buttons:
            button.config(text="")
        self.current_player = "X"