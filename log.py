import tkinter as tk

#======================
#   LOGIN WINDOW
#======================
window=tk.Tk()

window.title("LOGIN PAGE")
window.geometry("400x400")
window.minsize(380,300)
window.maxsize(600,700)
window.config(bg="#1e1e1e")

#LOGIN HEADER
tk.Label(
    window,
    text="LOGIN",
    bg="#1e1e1e",
    fg="white",
    font=("Arial",12)
).pack(pady=40)

#LOGIN USERNAME
tk.Label(
    window,
    text="Username",
    fg="white",
    bg="#1e1e1e",
    font=("Arial",12),
    anchor="w"
    
).pack()
Username=tk.Entry(
    window,
    width=30,
  
)
Username.pack(pady=10)


#LOGIN PASSWORD
tk.Label(
    window,
    text="Password",
    fg="white",
    bg="#1e1e1e",
    font=("Arial",12),
   
   
 
    # anchor="w"
).pack( )   
Password=tk.Entry(
    window,
    width=30,
    show="*"
)
Password.pack(pady=10)


#LOGIN BUTTON
login_button=tk.Button(
    window,
    width=15,
    text="login",
    fg="white",
    bg="#1e1e1e",
    font=("Arial",12)
)
login_button.pack()

# def linked_page():
#     window=tk.Tk()
#     window.title=("Home page")
#     window.geometry=("400x400")

# tk.Label(
#     window,
#     text="welcome",
#     font=("Arial",30)
# ).pack(pady=50)
# login_button=tk.Button(
#     window,
#     width=15,
#     text="login",
#     command=linked_page
# ).pack()

window.mainloop()




