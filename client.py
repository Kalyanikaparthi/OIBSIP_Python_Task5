import socket
import threading
import tkinter as tk
from tkinter import scrolledtext, simpledialog, messagebox

HOST = '127.0.0.1'
PORT = 5000

class ChatClient:
    def __init__(self, master):
        self.master = master
        self.master.title("Chat App")
        self.master.geometry("400x500")

        # Chat display area
        self.chat_area = scrolledtext.ScrolledText(master, state='disabled', font=("Arial", 12))
        self.chat_area.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        # Entry field
        self.entry = tk.Entry(master, font=("Arial", 12))
        self.entry.pack(padx=10, pady=5, fill=tk.X)
        self.entry.bind("<Return>", self.send_message)

        # Send button
        self.send_button = tk.Button(master, text="Send", command=self.send_message)
        self.send_button.pack(padx=10, pady=5)

        # Networking
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.username = simpledialog.askstring("Username", "Enter your name", parent=self.master)
        if not self.username:
            self.master.destroy()
            return

        try:
            self.client_socket.connect((HOST, PORT))
            join_msg = f"🔔 {self.username} has joined the chat"
            self.client_socket.send(join_msg.encode('utf-8'))
        except:
            messagebox.showerror("Error", "Unable to connect to server.")
            self.master.destroy()
            return

        # Start receiving thread
        threading.Thread(target=self.receive_messages, daemon=True).start()
        self.master.protocol("WM_DELETE_WINDOW", self.close_connection)

    def send_message(self, event=None):
        msg = self.entry.get()
        if msg:
            full_msg = f"{self.username}: {msg}"
            try:
                self.client_socket.send(full_msg.encode('utf-8'))
                self.entry.delete(0, tk.END)
            except:
                self.client_socket.close()
                self.master.destroy()

    def receive_messages(self):
        while True:
            try:
                msg = self.client_socket.recv(1024).decode('utf-8')
                if msg:
                    self.chat_area.config(state='normal')
                    self.chat_area.insert(tk.END, msg + "\n")
                    self.chat_area.yview(tk.END)
                    self.chat_area.config(state='disabled')
            except:
                break

    def close_connection(self):
        try:
            self.client_socket.send(f"🔕 {self.username} has left the chat".encode('utf-8'))
            self.client_socket.close()
        except:
            pass
        self.master.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = ChatClient(root)
    root.mainloop()