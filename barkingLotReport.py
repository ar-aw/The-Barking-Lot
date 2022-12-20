"""
name: arika awan
date: october 23
decription: doggy daycare, the Barking Lot, report cards
"""

#dec vars
dog_name = ""
num_days = 0
dog_app = 0
dog_appear = 0
dog_att = 0
app = []
appear = []
att = []

#ask user for dog's name, when typing in dog's name, enter "ZZZ" to exit program
dog_name = input("Enter the dog's name(enter ZZZ to quit): ")

while (dog_name.upper() != "ZZZ"):
    
    #ask user for number of days in stay
    num_days = int(input("For how many nights did the dog stay at The Barking Lot?"))
    
    #set up a countdown
    counter = num_days
    
    #days are from 1-21 inclusive (prompt again)
    while (num_days>21 or num_days<1):
        print("invalid number")
        num_days = int(input("Once again, for how many nights did the dog stay at The Barking Lot?"))
    
    #countdown system, loop through program for each night spent
    while (1<=counter<=21):
        
        #label the days
        print(f"Day {counter}: ")
        
        #for each day:
        
        #score from 1-5 for dog's appetite
        dog_app = int(input("On a scale of 1-5, how was the dog's appetite? "))
        #reprompt for valid score (1-5 inclusive)
        while (dog_app>5 or dog_app<1):
            print("not a valid value for appetite try again")
            dog_app = int(input("Once again, on a scale of 1-5, how was the dog's appetite? "))
        #add to list for summation
        app.append(dog_app)
        
        #score from 1-5 for dog's appearance    
        dog_appear = int(input("On a scale of 1-5, how was the dog's general appearance? "))
        #reprompt for valid score (1-5 inclusive)
        while (dog_appear>5 or dog_appear<1):
            print("not a valid value for appearance")
            dog_appear = int(input("Once again, on a scale of 1-5, how was the dog's general appearance? "))
        appear.append(dog_appear)
            
        #score from 1-5 for dog's attitude and demeanor
        dog_att = int(input("On a scale of 1-5, how was the dog's attitude and general demeanor? "))
        #reprompt for valid score (1-5 inclusive)
        while (dog_att>5 or dog_att<1):
            print("not a valid value for attitude")
            dog_att = int(input("Once again, on a scale of 1-5, how was the dog's attitude and general demeanor? "))
        att.append(dog_att)
            
        #countdown to match condition 
        counter -= 1
        
        """
        app_total = sum(app)
        appear_total = sum(appear)
        att_total = sum(att)
        """
    app_total = sum(app)
    appear_total = sum(appear)
    att_total = sum(att)
    report_card_total = app_total+appear_total+att_total
    app_avg = app_total/num_days
    appear_avg = appear_total/num_days
    att_avg = att_total/num_days
    print("\n")
    print(dog_name)
    print("total score:",report_card_total)
    print("average appetite score:",app_avg)
    print("average appearance score:", appear_avg)
    print("average attitude score:",att_avg)
        

  
            
    #prompt for another dog or quit    
    dog_name = input("Enter another dog's name(enter ZZZ to quit): ")
    
#output
#dog's name
#dog's total score for the entire stay
#dog's average score

#prompt for another dog or quit