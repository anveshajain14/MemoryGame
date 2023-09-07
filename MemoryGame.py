import random
import time
import tkinter as tk
from tkinter import messagebox

class MemoryGameApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Memory Sequence Game")
        
        self.sequence_length = 5
        self.seq = self.generate_sequence()
        self.player_sequence = []
        
        self.label = tk.Label(self.root, text="Memorize the sequence:")
        self.label.pack()
        
        self.sequence_label = tk.Label(self.root, text=str(self.seq))
        self.sequence_label.pack()
        
        self.hide_sequence_button = tk.Button(self.root, text="Hide Sequence", command=self.hide_sequence)
        self.hide_sequence_button.pack()
        
        self.entry_label = tk.Label(self.root, text="Enter the sequence:")
        self.entry_label.pack()
        
        self.entry = tk.Entry(self.root)
        self.entry.pack()
        
        self.submit_button = tk.Button(self.root, text="Submit", command=self.check_sequence)
        self.submit_button.pack()
        
        self.play_again_button = tk.Button(self.root, text="Play Again", command=self.play_again)
        self.play_again_button.pack()
        
    def generate_sequence(self):
        return [random.randint(1, 9) for _ in range(self.sequence_length)]
    
    def hide_sequence(self):
        self.sequence_label.config(text="")
        self.root.after(20000, self.show_sequence)
        
    def show_sequence(self):
        self.sequence_label.config(text=str(self.seq))
        
    def check_sequence(self):
        input_text = self.entry.get()
        try:
            self.player_sequence = [int(num) for num in input_text.split()]
        except ValueError:
            messagebox.showerror("Error", "Invalid input. Please enter numbers.")
            return
        
        if self.player_sequence == self.seq:
            messagebox.showinfo("Congratulations", "You remembered the sequence correctly.")
        else:
            messagebox.showinfo("Wrong Sequence", f"The correct sequence was: {self.seq}")
    
    def play_again(self):
        self.seq = self.generate_sequence()
        self.sequence_label.config(text=str(self.seq))
        self.entry.delete(0, tk.END)
        self.player_sequence = []

if __name__ == "__main__":
    root = tk.Tk()
    app = MemoryGameApp(root)
    root.mainloop()
