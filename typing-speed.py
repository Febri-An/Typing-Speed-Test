from tkinter import *
import random 

class TypingSpeed:
    def __init__(self):
        self.setup()
        
    def setup(self):
        self.is_on = True
        self.run_count = False
        self.character = 0
        self.canvas = Canvas(width=800, height=500)
        self.img = PhotoImage(file="background.png")
        self.canvas.create_image(400, 250, image=self.img)
        self.timer_text = self.canvas.create_text(400, 50, text="01:00", font=("Arial", 18), tags="time")
        self.canvas.pack()
        self.generate_text()

        window.bind("<KeyPress>", self.on_key_press) #is the letter correct?

        self.button = Button(text="Restart", bg="#2d4b6b", fg="white", padx=30, pady=10, command=self.restart)
        self.button.pack()

    def generate_text(self):
        with open(file="word.txt") as file:
            value = file.read().split("\n")
        self.rand10 = random.choices(value, k=20)
        self.separated_text = list(" ".join(self.rand10)) #made into seperate letter
        self.show_text()

    def show_text(self):
            self.text = self.canvas.create_text(400, 250, text="".join(self.separated_text), font=("Arial", 24), width=650, tags="text")

    def on_key_press(self, event): 
        if (event.keysym == self.separated_text[0]) or (event.keysym == "space" and self.separated_text[0] == " "):
            if self.is_on: #game on
                self.start_countdown()  
                self.character += 1
                self.canvas.delete("text")
                self.separated_text.pop(0)
                self.show_text()
                if self.separated_text == []:
                    self.generate_text()

    def start_countdown(self):
        if not self.run_count:
            self.run_count = True
            self.countdown(60)

    def countdown(self, count):
        mins, secs = divmod(count, 60)
        time_format = '{:02d}:{:02d}'.format(mins, secs)
        self.canvas.itemconfig(self.timer_text, text=time_format)
        if count > 0:
            self.timer = window.after(1000, self.countdown, count - 1) #create timer
        else:
            self.run_count = False
            self.is_on = False
            self.canvas.delete("text")
            self.canvas.create_text(400, 250, text=f"{self.character/5} WPM", font=("Arial", 26))
    
    def restart(self):
        window.after_cancel(self.timer)
        self.canvas.destroy()
        self.button.destroy()
        self.setup()
        

if __name__ == "__main__":
    window = Tk()
    window.title("Typing Speed Test") 
    app = TypingSpeed()
    window.mainloop()

