# FP8

# Customer Feedback Application

This is a Python application that allows customers to submit feedback, which is stored in a database. The application includes a simple GUI for data input and password-protected retrieval of feedback entries.

## Project Overview

This application was built to provide hands-on experience in:
- Database management (using SQLite)
- Graphical User Interface (GUI) design (using Tkinter)
- Basic security principles in application development

### Features
1. **Customer Feedback Submission**: Users can enter their name, email, and feedback message.
2. **Data Storage**: Feedback is saved in an SQLite database.
3. **Password-Protected Data Retrieval**: Feedback entries can be displayed in the console with password protection to maintain data privacy.

### Submitting Feedback
1. Open the application by running `customer_feedback.py`.
2. Enter your name, email, and feedback in the provided fields.
3. Click the **Submit Feedback** button to save your feedback. A message will confirm successful submission.

### Retrieving Feedback
1. Click the **Retrieve Feedback** button in the GUI.
2. A prompt will appear in the console asking for the password. Enter the password:
   password123
3. If the password is correct, all feedback entries will be displayed in the console. If incorrect, access will be denied.


## Project Structure

- `customer_feedback.py`: The main application file that includes database setup, GUI, and data retrieval functionality.
- `customer_feedback.db`: The SQLite database file (created automatically after the first feedback submission).
- `README.md`: Project documentation.