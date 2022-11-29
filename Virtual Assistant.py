import webbrowser
import random
import pyttsx3

nameofassistant = []

engine = pyttsx3.init()

def start():
    
    global nameofassistant2
    
    engine.say("I need a name. What would you like to call me? Please type it here: ")
    engine.runAndWait()
    nameofassistant=input("I need a name. What would you like to call me? Please type it here: ")
    
    engine.say("Hello! I am " +nameofassistant+ ". Choose a option below: ")
    print("Hello! I am " +nameofassistant+ ". Choose a option below: ")
    
    engine.say("Press '1' to list all options. ")
    print("Press '1' to list all options. ")
    
    engine.say("Press '2' to not list all options. ")
    print("Press '2' to not list all options. ")
    
    engine.runAndWait()
    
    engine.say("Enter option now: ")
    engine.runAndWait()
    listornolist=input("Enter option now: ")
    
    if listornolist == '1':
        optionchoices()
    elif listornolist == '2':
        optionstartshere()
    else:
        engine.say("Invalid Input.")
        print("Invalid Input.")
    
def optionchoices():
    
    engine.say("Listing options now: ")
    print("Listing options now: ")

    engine.say("Press '0' to close Virtual Assistant.")
    print("Press '0' to close Virtual Assistant.")
    engine.say("Press '1' to open Gmail.")
    print("Press '1' to open Gmail.")
    engine.say("Press '2' to open Google Classroom.")
    print("Press '2' to open Google Classroom.")
    engine.say("Press '3' to find out the date.")
    print("Press '3' to find out the date.")
    engine.say("Press '4' to find out the time.")
    print("Press '4' to find out the time.")
    engine.say("Press '5' to open calculator")
    print("Press '5' to open calculator")
    engine.say("Press '6' to toss a coin.")
    print("Press '6' to toss a coin.")
    engine.runAndWait()
    
    optionstartshere()

def optionstartshere():

    engine.say("Enter option now:")
    engine.runAndWait()
    option=input("Enter option now: ")

    if option == '0':
        engine.say("Closed. See you later!")
        print("Closed. See you later!")
        engine.runAndWait()
        quit()
    elif option == '1':
        webbrowser.open("https://mail.google.com/mail/u/0/#inbox")
        print("")
        engine.say("Successfully opened.")
        print("Successfully opened.")
        print("")
        engine.runAndWait()
        optionstartshere()
    elif option == '2':
        webbrowser.open("https://classroom.google.com/h")
        print("")
        engine.say("Successfully opened.")
        print("Successfully opened.")
        print("")
        engine.runAndWait()
        optionstartshere()
    elif option == '3':
        
        from datetime import date

        today = date.today()

        d1 = today.strftime("%d/%m/%Y")
        print("")
        engine.say(d1)
        print(d1)
        engine.runAndWait()
        print("")
        
        optionstartshere()
        
    elif option == '4':
        
        from datetime import datetime

        now = datetime.now()

        current_time = now.strftime("%H:%M:%S")
        print("")
        engine.say(current_time)
        print(current_time)
        engine.runAndWait()
        print("")
        
        optionstartshere()
        
    elif option == '5':

        def add(x, y):
            return x + y

        def subtract(x, y):
            return x - y

        def multiply(x, y):
            return x * y

        def divide(x, y):
            return x / y


        print("Select operation.")
        engine.say("Select operation.")
        print("Press '1' to add.")
        engine.say("Press '1' to add.")
        print("Press '2' to subtract.")
        engine.say("Press '2' to subtract.")
        print("Press '3' to multiply.")
        engine.say("Press '3' to multiply.")
        print("Press '4' to divide.")
        engine.say("Press '4' to divide.")
        engine.runAndWait()

        while True:
            
            engine.say("Enter choice(1/2/3/4): ")
            engine.runAndWait()
            choice = input("Enter choice(1/2/3/4): ")

            if choice in ('1', '2', '3', '4'):
                engine.say("Enter first number: ")
                engine.runAndWait()
                num1 = float(input("Enter first number: "))
                engine.say("Enter second number: ")
                engine.runAndWait()
                num2 = float(input("Enter second number: "))

                if choice == '1':
                    print(num1, "+", num2, "=", add(num1, num2))

                elif choice == '2':
                    print(num1, "-", num2, "=", subtract(num1, num2))

                elif choice == '3':
                    print(num1, "*", num2, "=", multiply(num1, num2))

                elif choice == '4':
                    print(num1, "/", num2, "=", divide(num1, num2))
                    
                engine.say("Another calculation? (yes/no): ")
                engine.runAndWait()
                next_calculation = input("Another calculation? (yes/no): ")
                if next_calculation == "no":
                    
                  optionstartshere()
            
            else:
                
                engine.say("Invalid Input, try again.")
                print("Invalid Input, try again.")
                engine.runAndWait()
                
    elif option == '6':
        
        def coinflip():
        
            result = random.choice(["Heads","Tails"])
            print("")
            engine.say(result)
            print(result)
            engine.runAndWait()
            print("")
            
            engine.say("Flip again? (yes/no) ")
            engine.runAndWait()
            coinflipagain=input("Flip again? (yes/no) ")
        
            if coinflipagain == 'yes':
                coinflip()
            elif coinflipagain == 'no':
                print("")
                engine.say("Coin Flipping stopped.")
                print("Coin Flipping stopped.")
                print("")
                engine.runAndWait()
                
                optionstartshere()
            
        coinflip()
        
start()