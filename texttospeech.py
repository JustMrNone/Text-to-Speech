import pyttsx3 
import sys

#creatin the converter class
class Converter:
    def __init__(self):
        self.engine = pyttsx3.init()
    #defining a function for saying    
    def Say(self, words):
        self.engine.say(words)
        self.engine.runAndWait() 
    #defining a function for choosing the voice male or female  
    def Choose(self, ID):
        voices = self.engine.getProperty("voices")
        self.engine.setProperty("voice", voices[ID].id)


def main():
    #calling con function 
    con()
    
def con(): 
    #if one argument is passed at the promp 
    if len(sys.argv) == 2: 
        
        convertor = Converter()
        sentence = sys.argv[1]
        convertor.Say(sentence)
    #if two arguments passed at the prompt     
    elif len(sys.argv) == 3:
        
        convertor = Converter()
        sentence = sys.argv[1]
        while True:
            try: 
                voicechoice = int(sys.argv[2])
            except ValueError:
                print("input either 0 or 1")
                sys.exit("you need to use 0 for male or 1 for female as your second passed argument in the function")
            
            if voicechoice not in [1, 0]:
                print()
                sys.exit("input either 0 or 1 for your voice")
            else:
                break
        convertor.Choose(voicechoice)
        return convertor.Say(sentence)
    #if no argument is passed at the prompt
    elif len(sys.argv) == 1:
        convertor = Converter()
        while True:
            try: 
                voicechoice = int(input("Select Your Voice (0 for male, 1 for female) ")) 
            except ValueError:
                print("input either 0 or 1")
                continue
            
            if voicechoice not in [1, 0]:
                print("input either 0 or 1")
                continue
            else:
                break
        sentence = input("Type here: ")
        convertor.Choose(voicechoice)
        convertor.Say(sentence)
    #if more than two arguments are passed at the prompt
    else:
        print("too many arguments.")
        

if __name__ == "__main__":
    main()
    