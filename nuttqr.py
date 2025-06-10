# qr_gui_generator.py

import qrcode
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk

def generate_qr():
    data = entry.get()
    if not data:
        messagebox.showwarning("Input Required", "Please enter a URL or text!")
        return

    qr = qrcode.QRCode(
        version=1,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.thumbnail((250, 250))  # Resize for preview

    qr_img = ImageTk.PhotoImage(img)
    qr_label.config(image=qr_img)
    qr_label.image = qr_img

    save_btn.config(state=tk.NORMAL)
    save_btn.image_to_save = img

def save_qr():
    file_path = filedialog.asksaveasfilename(defaultextension=".png",
                                             filetypes=[("PNG files", "*.png")])
    if file_path:
        save_btn.image_to_save.save(file_path)
        messagebox.showinfo("Saved", f"QR Code saved to {file_path}")

# Build the GUI
root = tk.Tk()
root.title("QR Code Generator")

frame = tk.Frame(root, padx=10, pady=10)
frame.pack()

tk.Label(frame, text="Enter URL or text:").pack()
entry = tk.Entry(frame, width=50)
entry.pack(pady=5)

entry.bind("<Return>", lambda event: generate_qr())

generate_btn = tk.Button(frame, text="Generate QR Code", command=generate_qr)
generate_btn.pack(pady=5)

qr_label = tk.Label(frame)
qr_label.pack(pady=5)

save_btn = tk.Button(frame, text="Save QR Code", command=save_qr, state=tk.DISABLED)
save_btn.pack(pady=5)

root.mainloop()
