import tkinter as tk
from tkinter import simpledialog, messagebox
import time
import random
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from password_checker import check_password_strength
from tic_tac_toe import TicTacToe
from searching_algorithms import linear_search, binary_search
from sorting_algorithms import bubble_sort, quick_sort, merge_sort


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

        self.search_button = tk.Button(
            self.menu_frame, text="Search Algorithms", command=self.search_algorithms
        )
        self.search_button.pack(pady=5)

        self.sort_button = tk.Button(
            self.menu_frame, text="Sort Algorithms", command=self.sort_algorithms
        )
        self.sort_button.pack(pady=5)

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

    def search_algorithms(self):
        self.disable_menu()
        search_window = tk.Toplevel(self.root)
        search_window.title("Search Algorithms")

        tk.Label(search_window, text="Choose a search algorithm:").pack()

        tk.Button(
            search_window,
            text="Linear Search",
            command=lambda: self.run_search_algorithm(search_window, "linear"),
        ).pack(pady=5)
        tk.Button(
            search_window,
            text="Binary Search",
            command=lambda: self.run_search_algorithm(search_window, "binary"),
        ).pack(pady=5)

        search_window.protocol(
            "WM_DELETE_WINDOW", lambda: self.close_search_window(search_window)
        )

    def run_search_algorithm(self, window, algorithm_type):
        window.destroy()

        data_size = 100  # Size of the dataset
        data = random.sample(range(1, 1000), data_size)  # Generate random dataset
        target = random.choice(data)  # Choose a random target from the dataset

        if algorithm_type == "linear":
            start_time = time.time()
            index = linear_search(data, target)
            end_time = time.time()
            complexity = "O(n)"
            algorithm_name = "Linear Search"

        elif algorithm_type == "binary":
            data.sort()  # Binary search requires sorted data
            start_time = time.time()
            index = binary_search(data, target)
            end_time = time.time()
            complexity = "O(log n)"
            algorithm_name = "Binary Search"

        search_time = end_time - start_time

        result_message = f"Algorithm: {algorithm_name}\nTarget: {target}\nIndex: {index}\nTime: {search_time:.6f} seconds\nComplexity: {complexity}"

        result_window = tk.Toplevel(self.root)
        result_window.title(f"{algorithm_name} Result")

        tk.Label(result_window, text=result_message).pack(pady=10)

        fig, ax = plt.subplots()

        if algorithm_type == "linear":
            ax.plot(data, "bo", label="Data")
            ax.plot(index, target, "ro", label="Target")

        elif algorithm_type == "binary":
            ax.plot(data, "bo", label="Data")
            ax.plot(index, target, "ro", label="Target")

        ax.legend()
        plt.xlabel("Index")
        plt.ylabel("Value")

        canvas = FigureCanvasTkAgg(fig, master=result_window)
        canvas.draw()
        canvas.get_tk_widget().pack()

        result_window.protocol(
            "WM_DELETE_WINDOW", lambda: self.close_result_window(result_window)
        )

    def sort_algorithms(self):
        self.disable_menu()
        sort_window = tk.Toplevel(self.root)
        sort_window.title("Sort Algorithms")

        tk.Label(sort_window, text="Choose a sort algorithm:").pack()

        tk.Button(
            sort_window,
            text="Bubble Sort",
            command=lambda: self.run_sort_algorithm(sort_window, "bubble"),
        ).pack(pady=5)

        tk.Button(
            sort_window,
            text="Quick Sort",
            command=lambda: self.run_sort_algorithm(sort_window, "quick"),
        ).pack(pady=5)

        tk.Button(
            sort_window,
            text="Merge Sort",
            command=lambda: self.run_sort_algorithm(sort_window, "merge"),
        ).pack(pady=5)

    def run_sort_algorithm(self, window, algorithm_type):
        window.destroy()

        data_size = 100  # Size of the dataset
        data = random.sample(range(1, 1000), data_size)  # Generate random dataset

        if algorithm_type == "bubble":
            start_time = time.time()
            sorted_data = bubble_sort(data.copy())
            end_time = time.time()
            complexity = "O(n^2)"
            algorithm_name = "Bubble Sort"

        elif algorithm_type == "quick":
            start_time = time.time()
            sorted_data = quick_sort(data.copy())
            end_time = time.time()
            complexity = "O(n log n)"
            algorithm_name = "Quick Sort"

        elif algorithm_type == "merge":
            start_time = time.time()
            sorted_data = merge_sort(data.copy())
            end_time = time.time()
            complexity = "O(n log n)"
            algorithm_name = "Merge Sort"

        sort_time = end_time - start_time

        result_message = f"Algorithm: {algorithm_name}\nTime: {sort_time:.6f} seconds\nComplexity: {complexity}"

        result_window = tk.Toplevel(self.root)
        result_window.title(f"{algorithm_name} Result")

        tk.Label(result_window, text=result_message).pack(pady=10)

        fig, (ax1, ax2) = plt.subplots(2)

        ax1.plot(data, "bo", label="Unsorted Data")
        ax1.legend()
        ax1.set_title("Before Sorting")

        ax2.plot(sorted_data, "go", label="Sorted Data")
        ax2.legend()
        ax2.set_title("After Sorting")

        plt.xlabel("Index")
        plt.ylabel("Value")

        canvas = FigureCanvasTkAgg(fig, master=result_window)
        canvas.draw()
        canvas.get_tk_widget().pack()

        result_window.protocol(
            "WM_DELETE_WINDOW", lambda: self.close_result_window(result_window)
        )

    def close_search_window(self, search_window):
        search_window.destroy()
        self.enable_menu()

    def close_result_window(self, result_window):
        result_window.destroy()
        self.enable_menu()

    def disable_menu(self):
        self.password_button.config(state=tk.DISABLED)
        self.tic_tac_toe_button.config(state=tk.DISABLED)
        self.search_button.config(state=tk.DISABLED)
        self.sort_button.config(state=tk.DISABLED)

    def enable_menu(self):
        self.password_button.config(state=tk.NORMAL)
        self.tic_tac_toe_button.config(state=tk.NORMAL)
        self.search_button.config(state=tk.NORMAL)
        self.sort_button.config(state=tk.NORMAL)

    def close_game(self, game_window):
        game_window.destroy()
        self.enable_menu()

    def show_menu(self):
        self.menu_frame.pack()


if __name__ == "__main__":
    root = tk.Tk()
    app = MainApp(root)
    root.mainloop()
