#TASK NO.1
import tkinter as tk
from tkinter import messagebox

class ToDoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List Application")
        
        self.tasks = []
        
        self.frame = tk.Frame(root)
        self.frame.pack(pady=10)
        
        self.task_listbox = tk.Listbox(self.frame, width=50, height=10)
        self.task_listbox.pack(side=tk.LEFT, fill=tk.BOTH)
        
        self.scrollbar = tk.Scrollbar(self.frame)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.BOTH)
        
        self.task_listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.task_listbox.yview)
        
        self.entry = tk.Entry(root, width=50)
        self.entry.pack(pady=10)
        
        self.button_frame = tk.Frame(root)
        self.button_frame.pack(pady=10)
        
        self.add_button = tk.Button(self.button_frame, text="Add Task", command=self.add_task)
        self.add_button.grid(row=0, column=0, padx=10)
        
        self.update_button = tk.Button(self.button_frame, text="Update Task", command=self.update_task)
        self.update_button.grid(row=0, column=1, padx=10)
        
        self.done_button = tk.Button(self.button_frame, text="Mark as Done", command=self.mark_done)
        self.done_button.grid(row=0, column=2, padx=10)
        
        self.delete_button = tk.Button(self.button_frame, text="Delete Task", command=self.delete_task)
        self.delete_button.grid(row=0, column=3, padx=10)
        
        self.list_tasks()

    def add_task(self):
        task = self.entry.get()
        if task != "":
            self.tasks.append({'task': task, 'done': False})
            self.list_tasks()
            self.entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "You must enter a task.")
    
    def update_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            new_task = self.entry.get()
            if new_task != "":
                index = selected_task_index[0]
                self.tasks[index]['task'] = new_task
                self.list_tasks()
                self.entry.delete(0, tk.END)
            else:
                messagebox.showwarning("Warning", "You must enter a new task description.")
        else:
            messagebox.showwarning("Warning", "You must select a task to update.")
    
    def mark_done(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            index = selected_task_index[0]
            self.tasks[index]['done'] = True
            self.list_tasks()
        else:
            messagebox.showwarning("Warning", "You must select a task to mark as done.")
    
    def delete_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            index = selected_task_index[0]
            self.tasks.pop(index)
            self.list_tasks()
        else:
            messagebox.showwarning("Warning", "You must select a task to delete.")
    
    def list_tasks(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            status = "Done" if task['done'] else "Not done"
            self.task_listbox.insert(tk.END, f"{task['task']} [{status}]")

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoListApp(root)
    root.mainloop()
