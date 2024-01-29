import tkinter as tk

class GUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("To-Do List")
        self.root.geometry("750x550")

        # Configure column weights for centering
        self.root.columnconfigure(0, weight=1)
        self.root.columnconfigure(1, weight=1)
        self.root.columnconfigure(2, weight=1)

        # Label centered across all columns
        self.label = tk.Label(self.root, text="To-Do", font=("Arial", 18))
        self.label.grid(row=0, column=0, columnspan=3, padx=20, pady=20)

        # "+ Add To-do" button centered across all columns
        self.buttonadd = tk.Button(self.root, text="+ Add To-do", font=("Arial", 18), command=self.todo_addition)
        self.buttonadd.grid(row=1, column=0, columnspan=3, pady=10)

        self.root.mainloop()

    def todo_addition(self):
        # Create a new Toplevel window for adding a to-do
        self.add_todo_window = tk.Toplevel(self.root)

        # Entry widget for entering the to-do task
        self.textbox = tk.Entry(self.add_todo_window, font=("Arial", 14))
        self.textbox.pack(padx=10, pady=10)

        # Submit button to add the to-do
        self.submit_button = tk.Button(self.add_todo_window, text="Submit", font=("Arial", 14), command=self.add_todo)
        self.submit_button.pack(padx=10, pady=10)
        

    def add_todo(self):
        # Get the task from the Entry widget
        todo_task = self.textbox.get()
        
        self.textbox.destroy()
        self.submit_button.destroy()
        self.add_todo_window.destroy()
        
        # Center the check button, label, and delete button in a new row using grid
        self.check_state = tk.IntVar()
        self.check = tk.Checkbutton(self.root, variable=self.check_state)
        self.check.grid(row=2, column=0, pady=10)

        self.Addlabel = tk.Label(self.root, text=todo_task)
        self.Addlabel.grid(row=2, column=1, pady=10)
        
        self.delete_button = tk.Button(self.root, text="Delete", font=("Arial", 14), command=self.delete_todo)
        self.delete_button.grid(row=2, column=2, pady=10)
        
    def delete_todo(self):
        self.Addlabel.destroy()
        self.delete_button.destroy()
        self.check.destroy()
        
GUI()
