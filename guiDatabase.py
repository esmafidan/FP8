import sqlite3

# Connect to the database (or create it if it doesn't exist)
conn = sqlite3.connect('customer_feedback.db')
cursor = conn.cursor()

# Create a table for feedback if it doesn't already exist
cursor.execute('''CREATE TABLE IF NOT EXISTS feedback (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    email TEXT NOT NULL,
                    feedback TEXT NOT NULL)''')

conn.commit()
conn.close()

import tkinter as tk
from tkinter import messagebox
import sqlite3

# Function to submit feedback
def submit_feedback():
    name = entry_name.get()
    email = entry_email.get()
    feedback = entry_feedback.get("1.0", tk.END)  # Gets multiline text

    if name and email and feedback.strip():  # Check if all fields are filled
        conn = sqlite3.connect('customer_feedback.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO feedback (name, email, feedback) VALUES (?, ?, ?)", 
                       (name, email, feedback.strip()))
        conn.commit()
        conn.close()

        entry_name.delete(0, tk.END)
        entry_email.delete(0, tk.END)
        entry_feedback.delete("1.0", tk.END)

        messagebox.showinfo("Success", "Feedback submitted successfully!")
    else:
        messagebox.showwarning("Input Error", "Please fill all fields.")

# Function to retrieve feedback with password protection
def retrieve_feedback():
    password = input("Enter the password to retrieve feedback: ")
    if password == "your_password":  # Replace 'your_password' with the actual password
        conn = sqlite3.connect('customer_feedback.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM feedback")
        feedbacks = cursor.fetchall()
        conn.close()

        for feedback in feedbacks:
            print(f"ID: {feedback[0]}, Name: {feedback[1]}, Email: {feedback[2]}, Feedback: {feedback[3]}")
    else:
        print("Incorrect password. Access denied.")

# GUI setup
root = tk.Tk()
root.title("Customer Feedback Application")

tk.Label(root, text="Name").grid(row=0, column=0)
entry_name = tk.Entry(root)
entry_name.grid(row=0, column=1)

tk.Label(root, text="Email").grid(row=1, column=0)
entry_email = tk.Entry(root)

entry_email.grid(row=1, column=1)

tk.Label(root, text="Feedback").grid(row=2, column=0)
entry_feedback = tk.Text(root, height=4, width=30)
entry_feedback.grid(row=2, column=1)

submit_button = tk.Button(root, text="Submit Feedback", command=submit_feedback)
submit_button.grid(row=3, column=0, columnspan=2, pady=10)

retrieve_button = tk.Button(root, text="Retrieve Feedback", command=retrieve_feedback)
retrieve_button.grid(row=4, column=0, columnspan=2, pady=10)

root.mainloop()  