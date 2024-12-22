from tkinter import *
from tkinter import messagebox
import base64
import os

#Decryption (converting cipher text to plain text)
def decrypt():
    choice=code.get()
    if choice=="1234":
        screen2=Toplevel(screen)
        screen2.title("DECRYPTION")
        screen2.geometry("400x200")
        screen2.configure(bg="black")

        Message=text1.get(1.0,END)
        decode_msg=Message.encode("ascii")
        base64_bytes=base64.b64decode(decode_msg)
        decrypt=base64_bytes.decode("ascii")

        Label(screen2,text="DECRYPT",font="arial",fg="white",bg="black").place(x=10,y=0)
        text2=Text(screen2,font="Robote 10",bg="white",relief=GROOVE,wrap=WORD,bd=0)
        text2.place(x=10,y=40,width=380,height=150)

        text2.insert(END,decrypt )
    elif choice==" ":
        messagebox.showerror("decryption","Input your choice")
    elif choice!="1234":
        messagebox.showerror("decryption","Invalid choice")        


#Encryption ( Converting plain text to cipher text )
def encrypt():
    choice=code.get()
    if choice=="1234":
        screen1=Toplevel(screen)
        screen1.title("ENCRYPTION")
        screen1.geometry("400x200")
        screen1.configure(bg="black")

        Message=text1.get(1.0,END)
        encode_msg=Message.encode("ascii")
        base64_bytes=base64.b64encode(encode_msg)
        encrypt=base64_bytes.decode("ascii")

        Label(screen1,text="ENCRYPT",font="arial",fg="white",bg="black").place(x=10,y=0)
        text2=Text(screen1,font="Robote 10",bg="white",relief=GROOVE,wrap=WORD,bd=0)
        text2.place(x=10,y=40,width=380,height=150)

        text2.insert(END,encrypt )
    elif choice==" ":
        messagebox.showerror("encryption","Input your choice")
    elif choice!="1234":
        messagebox.showerror("encryption","Invalid choice")        
    


def main_screen():
    # Declare global variables
    global screen
    global code
    global text1
    
    # Initialize the main window
    screen=Tk()
    screen.geometry("375x398")
    screen.title("Kruptos")
     # Function to reset the input fields
    def reset():
        code.set("")
        text1.delete(1.0,END)
        
    # Label for text input
    Label(text="Enter text for encryption and decryption",fg="black",font=("calbri",13)).place(x=10,y=10)
     # Text widget for entering the text to be encrypted/decrypted
    text1=Text(font="Robote 20",bg="white",relief=GROOVE,wrap=WORD,bd=0)
    text1.place(x=10,y=50,width=355,height=100)
    # Label for secret key input
    Label(text="Enter secret key for  encryption and decryption",fg="black",font=("calibri",12)).place(x=10,y=170)
    
    # Entry widget for entering the secret key
    code=StringVar()
    Entry(textvariable=code,width=19,bd=0,font=("arial",25),show="*").place(x=10,y=200)
    
    
    Button(text="ENCRYPT",height="2",width=23,bg="red",fg="white",bd=0,command=encrypt).place(x=10,y=250)# Button to trigger encryption
    Button(text="DECRYPT",height="2",width=23,bg="green",fg="white",bd=0,command=decrypt).place(x=200,y=250) # Button to trigger decryption
    Button(text="RESET",height="2",width=50,bg="#1089ff",fg="white",bd=0,command=reset).place(x=10,y=300)# Button to reset the input fields
    screen.mainloop()
    
main_screen()