import tkinter as tk
from tkinter import simpledialog, messagebox
from password_checker import check_password_strength
from tic_tac_toe import TicTacToe


class MainApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Main Menu")
        self.create_menu()

    def create_menu(self):
        self.menu_frame = tk.Frame(self.root)
        self.menu_frame.pack(padx=10, pady=10)

        tk.Label(self.menu_frame, text="Choose an option:").pack()

        self.password_button = tk.Button(
            self.menu_frame, text="Check Password Strength", command=self.check_password
        )
        self.password_button.pack(pady=5)

        self.tic_tac_toe_button = tk.Button(
            self.menu_frame, text="Play Tic-Tac-Toe", command=self.play_tic_tac_toe
        )
        self.tic_tac_toe_button.pack(pady=5)

        tk.Button(self.menu_frame, text="Exit", command=self.root.quit).pack(pady=5)

    def check_password(self):
        password = simpledialog.askstring(
            "Password Checker", "Enter a password to check its strength:"
        )
        if password:
            result = check_password_strength(password)
            messagebox.showinfo("Password Strength", result)
        self.show_menu()

    def play_tic_tac_toe(self):
        self.disable_menu()
        game_window = tk.Toplevel(self.root)
        game_window.title("Tic-Tac-Toe")
        TicTacToe(game_window)
        game_window.protocol("WM_DELETE_WINDOW", lambda: self.close_game(game_window))

    def disable_menu(self):
        self.password_button.config(state=tk.DISABLED)
        self.tic_tac_toe_button.config(state=tk.DISABLED)

    def enable_menu(self):
        self.password_button.config(state=tk.NORMAL)
        self.tic_tac_toe_button.config(state=tk.NORMAL)

    def close_game(self, game_window):
        game_window.destroy()
        self.enable_menu()

    def show_menu(self):
        self.menu_frame.pack()


if __name__ == "__main__":
    root = tk.Tk()
    app = MainApp(root)
    root.mainloop()
