import googletrans
from googletrans import Translator
from tkinter import *
from tkinter import messagebox

# Translate function to handle translation logic
def translate_function():
    if (len(src_entry.get("1.0", "end-1c")) > 1):
        src_v = src_entry.get("1.0", "end-1c").lower().replace(" ", "")
    else:
        src_v = None

    if (len(dest_entry.get("1.0", "end-1c")) > 1):
        dest_v = dest_entry.get("1.0", "end-1c").lower().replace(" ", "")
    else:
        dest_v = None

    if (len(text_entry.get("1.0", "end-1c")) <= 1):
        messagebox.showerror("Error", "Please enter valid text to translate.")
    else:
        text_v = text_entry.get("1.0", "end-1c")
        if (not src_v) and (not dest_v):
            translated_text = translator_object.translate(text_v)
        elif (not src_v):
            translated_text = translator_object.translate(text_v, dest=dest_v)
        elif (not dest_v):
            translated_text = translator_object.translate(text_v, src=src_v)
        else:
            translated_text = translator_object.translate(text_v, src=src_v, dest=dest_v)
        messagebox.showinfo("Translation", "TRANSLATED TEXT: " + translated_text.text)

# Clear function to reset all input fields
def clear():
    dest_entry.delete("1.0", "end-1c")
    src_entry.delete("1.0", "end-1c")
    text_entry.delete("1.0", "end-1c")

# Main window setup
window = Tk()
window.geometry("550x400")
window.title("PythonGeeks Language Translator")
window.configure(bg="#F7F7F9")

# Translator object
translator_object = Translator()

# Title label
title_frame = Frame(window, bg="#4A4E69", pady=10)
title_frame.pack(fill="x")
title_label = Label(title_frame, text="Language Translator", font=("Helvetica", 18, "bold"), bg="#4A4E69", fg="white")
title_label.pack()

# Input frame for organization
input_frame = Frame(window, bg="#F7F7F9", padx=20, pady=20)
input_frame.pack(pady=20)

# Text input
text_label = Label(input_frame, text="Text to translate:", font=("Helvetica", 12), bg="#F7F7F9")
text_label.grid(row=0, column=0, sticky="w")
text_entry = Text(input_frame, width=40, height=5, font=("Arial", 12), relief="groove", bd=2, wrap="word")
text_entry.grid(row=0, column=1, padx=10, pady=10)

# Source language input
src_label = Label(input_frame, text="Source language (auto-detect if empty):", font=("Helvetica", 12), bg="#F7F7F9")
src_label.grid(row=1, column=0, sticky="w")
src_entry = Text(input_frame, width=20, height=1, font=("Arial", 12), relief="groove", bd=2)
src_entry.grid(row=1, column=1, padx=10, pady=5)

# Destination language input
dest_label = Label(input_frame, text="Target language (English if empty):", font=("Helvetica", 12), bg="#F7F7F9")
dest_label.grid(row=2, column=0, sticky="w")
dest_entry = Text(input_frame, width=20, height=1, font=("Arial", 12), relief="groove", bd=2)
dest_entry.grid(row=2, column=1, padx=10, pady=5)

# Button frame
button_frame = Frame(window, bg="#F7F7F9", pady=10)
button_frame.pack()

# Translate and Clear buttons with styling
button1 = Button(button_frame, text='Translate', bg='#9A8C98', fg="white", font=("Helvetica", 12, "bold"),
                 command=translate_function, relief="flat", width=10, height=2, activebackground="#C9ADA7")
button1.grid(row=0, column=0, padx=15)

button2 = Button(button_frame, text='Clear', bg='#9A8C98', fg="white", font=("Helvetica", 12, "bold"),
                 command=clear, relief="flat", width=10, height=2, activebackground="#C9ADA7")
button2.grid(row=0, column=1, padx=15)

# Close application main loop
window.mainloop()
