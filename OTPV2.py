from twilio.rest import Client
import random
import time
from tkinter import *
from tkinter import messagebox




class otp_verifier(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("1000x580+200+80")
        self.configure(bg = "#008080")
        self.resizable(False, False)
        self.n = str(self.OTP())
        self.client = Client("ACf80cc12da6288dc5df128a77585f120e", "9606d3f69eeaf30a4d78225b2d721015")
        self.client.messages.create(to=("+91-8103397255"),
                                    from_ ="+15642224789",
                                    body= self.n
                                    )
                                
    def OTP(self):
        return random. randrange(1000, 10000)  

    def Labels(self):
        self.c = Canvas(self, bg = "#808080", width = 400, height = 280)
        self.c.place(x = 290, y = 120)
        
        
        


        
        self.upper_frame = Frame(self, bg = "#000000", width = 1500, height = 130)
        self.upper_frame.place(x=0, y=0)
        
         
        
        self.picture = PhotoImage (file = "passwordre.png")
        self.k = Label(self.upper_frame, image = self.picture, bg = "#000000").place(x = 100, y = 15)
        
        self.j = Label(self.upper_frame, text = "Verify OTP", font = "TimesNewRoman 32 bold", bg = "#000000", fg="white").place(x=300, y=40)
        
        self.simpli_logo = PhotoImage(file = "parullogor.png")
        self.d = Label(self, image=self.simpli_logo, bg = "#808080", fg = "#808080").place(x= 750, y= 450)
        
    def Entry(self):
        self.User_Name = Text(self, font ="calibri 20", borderwidth = 2, wrap = WORD, width = 23, height = 1)
        self.User_Name.place(x =330, y=200)
        
    def Buttons(self):
        self.submitButtonImage = PhotoImage(file = "submit.png")
        self.submitButton = Button(self, image = self.submitButtonImage, command = self.checkOTP(), border= 0)
        self.submitButton.place(x = 440, y = 330)
        
        self.resendOTPImage = PhotoImage(file = "Get_OTP.png")
        self.resendOTP = Button(self, image = self.resendOTPImage, command = self.resendOTP(), border= 0)
        self.resendOTP.place(x = 420, y = 430)
          
    def resendOTP(self):
        self.n = str(self.OTP())
        self.client = Client("ACf80cc12da6288dc5df128a77585f120e", "9606d3f69eeaf30a4d78225b2d721015")
        self.client.messages.create(to=("+91-8103397255"),
                                    from_ ="+15642224789",
                                    body= self.n)
        
    def checkOTP(self):
        try:
            self.userInput = int(self.User_Name.get(1.0, "end -1c"))
            if self.userInput == int(self.n):
                messagebox.showinfo("showinfo", "Verification Successfull")
                self.n = "done"
            else:
                messagebox.showinfo("showinfo", "wrong OTP")
        except:
            messagebox.showinfo("showinfo", "INVALID OTP")
                
     
    def runTimer(self):
        
        self.clockTime = int(self.miniuteString.get())*60 + int(self.secondString.get())
        
        
        while(self.clockTime > -1):
            
            totalMinutes, totalSeconds = divmod(self.clockTime, 60)

            self.minuteString.set("{0:2d}".format(totalMinutes))
            self.secondString.set("{0:2d}".format(totalSeconds))

            ### Update the interface
            self.update()
            time.sleep(1)

            ### Let the user know if the timer has expired
            if(self.clockTime == 0):
                messagebox.showinfo("", "Your time has expired!")

            self.clockTime -= 1
       
                   
            
                
                
                                 
      
if __name__ == "__main__":
    window = otp_verifier()
    window.Labels()
    window.Entry()
    window.Buttons()
    window.update()
    window.mainloop()        