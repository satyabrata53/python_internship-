import tkinter as tk
from tkinter import messagebox, simpledialog

# Function to add a student
def add_student():
    roll_number = simpledialog.askstring("Input", "Enter Roll Number:")
    if roll_number:
        name = simpledialog.askstring("Input", "Enter Name:")
        marks = {}
        while True:
            subject = simpledialog.askstring("Input", "Enter Subject (or type 'done' to finish):")
            if subject.lower() == 'done':
                break
            score = simpledialog.askfloat("Input", f"Enter Marks for {subject}:")
            marks[subject] = score
        student_dict[roll_number] = {'name': name, 'marks': marks}
        messagebox.showinfo("Info", "Student added successfully!")

# Function to display student information
def display_student():
    roll_number = simpledialog.askstring("Input", "Enter Roll Number to display:")
    if roll_number in student_dict:
        student = student_dict[roll_number]
        student_info = f"Roll Number: {roll_number}\nName: {student['name']}\nMarks:\n"
        for subject, marks in student['marks'].items():
            student_info += f"  {subject}: {marks}\n"
        messagebox.showinfo("Student Information", student_info)
    else:
        messagebox.showerror("Error", "Student not found.")

# Main Tkinter application
def main():
    global student_dict
    student_dict = {}

    root = tk.Tk()
    root.geometry('400x350')
    colour1='#202f12'
    colour2='#05d7ff'
    colour3='#65e7ff'
    colour4='BLACK'
    main_frame=tk.Frame(root, bg=colour1, pady=50)
    main_frame.pack(fill=tk.BOTH, expand=True)
    main_frame.columnconfigure(0, weight=1)
    main_frame.rowconfigure(0, weight=1)
    main_frame.rowconfigure(1, weight=1)
    
    root.title("Student Management System")

    add_button = tk.Button(root,text="Add Student",command=add_student)
    add_button = tk.Button(
        main_frame,
        background=colour2,
        foreground=colour4,
        activebackground=colour3,
        activeforeground=colour4,
        highlightthickness=2,
        highlightbackground=colour2,
        highlightcolor='WHITE',
        width=13,
        height=2,
        border=0,
        cursor='hand1',
        text='Add Student',
        font=('Arial',16,'bold'),
        command=add_student
    )
    add_button.grid(column=0, row=0)
    display_button = tk.Button(
        main_frame,
        background=colour2,
        foreground=colour4,
        activebackground=colour3,
        activeforeground=colour4,
        highlightthickness=2,
        highlightbackground=colour2,
        highlightcolor='WHITE',
        width=13,
        height=2,
        border=0,
        cursor='hand1',
        text='Display student',
        font=('Arial',16,'bold'),
        command=display_student
    )
    display_button.grid(column=0,row=1)
    
    exit_button = tk.Button(
        main_frame,
        background=colour2,
        foreground=colour4,
        activebackground=colour3,
        activeforeground=colour4,
        highlightthickness=2,
        highlightbackground=colour2,
        highlightcolor='WHITE',
        width=13,
        height=2,
        border=0,
        cursor='hand1',
        text='Exit',
        font=('Arial',16,'bold'),
        command=root.quit
    )
    exit_button.grid(column=0,row=2)
    #exit_button.pack(pady=50)

    root.mainloop()

if __name__ == "__main__":
    main()