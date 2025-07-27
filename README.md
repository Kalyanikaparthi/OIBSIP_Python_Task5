# OIBSIP_Python_Task5 - GUI-Based Chat Application

## 📌 Project Title:
**Graphical Chat Application using Python Sockets and Tkinter**

---

## 🎯 Objective:
To build a multi-user, real-time chat application in Python that allows users to communicate over a local network using a client-server architecture. The application features a graphical interface built with Tkinter and handles communication using socket programming and threading.

---

## 🛠️ Tools and Technologies Used:
- **Python 3**
- **Socket Programming**
- **Tkinter** (for GUI)
- **Threading**
- **Localhost Networking (127.0.0.1)**

---

## 📁 Project Files:
  server.py # The main server-side script
  client.py # The GUI-based client-side application

---

## 🚀 How the Project Works:

### 🖥️ Server:
- Run `server.py` first.
- It listens for incoming client connections on `127.0.0.1:5000`.
- Once a client joins, it handles message broadcasting to all connected clients.
- Each client is managed on a separate thread.

### 👤 Client:
- Run `client.py`.
- Prompts the user for a username.
- Opens a Tkinter window to send and receive messages.
- Supports real-time chat with multiple clients connected to the same server.

---

## 🧠 Features Implemented:
- ✅ Multi-client support (real-time chat)
- ✅ GUI Interface using Tkinter
- ✅ Join/leave notifications
- ✅ Message broadcasting
- ✅ User input handling and threading for responsiveness

---

## 📦 How to Run:

 Open a terminal and start the server:
   ```bash
   python server.py
   python client.py # run in seperate terminals for multiple times, for multiple users.


---

## linkdin post
https://www.linkedin.com/posts/kalyani-kalyani-7a20a4375_oibsip-python-chatapp-activity-7354899970140848128-zkcS?utm_source
