# mail application with graphical user interface in python 

import tkinter as tk
from tkinter import messagebox
import smtplib

# Create a function to send an email
def send_email():
    recipient = to_entry.get()
    subject = subject_entry.get()
    message = message_text.get("1.0", "end")

    try:
        server = smtplib.SMTP('smtp.your-email-provider.com', 587)
        server.starttls()
        server.login('your_email@gmail.com', 'your_password')
        server.sendmail('your_email@gmail.com', recipient, f'Subject: {subject}\n{message}')
        server.quit()
        messagebox.showinfo("Success", "Email sent successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

# Create the main window
window = tk.Tk()
window.title("Mail Application")

# Create and arrange GUI elements
to_label = tk.Label(window, text="To:")
to_label.pack()
to_entry = tk.Entry(window)
to_entry.pack()

subject_label = tk.Label(window, text="Subject:")
subject_label.pack()
subject_entry = tk.Entry(window)
subject_entry.pack()

message_label = tk.Label(window, text="Message:")
message_label.pack()
message_text = tk.Text(window, height=5, width=30)
message_text.pack()

send_button = tk.Button(window, text="Send Email", command=send_email)
send_button.pack()

# Start the main loop
window.mainloop()
