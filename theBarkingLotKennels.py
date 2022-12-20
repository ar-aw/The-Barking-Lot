"""
name: Arika Awan
date: December 14 2022
desc: schedules kennel assignments for the current night. write kennel info to a txt file.
"""
#from sys import exit
import pprint
#really cool import i found when converting a dictionary to a string
import json

#declare variables
#dogName = ""
#dogWeight = 0

#dictionary that holds dog's ID, name, and weight
dog1 = {"ID":"1001", "name":"Bowser", "weight":130}
dog2 = {"ID":"1003", "name":"Ginger", "weight":80}
dog3 = {"ID":"1007", "name":"Molly", "weight":45}
dog4 = {"ID":"1008", "name":"Murphy", "weight":18}
dog5 = {"ID":"1012", "name":"Roxy", "weight":70}
dog6 = {"ID":"1034", "name":"Samantha", "weight":12}
dog7 = {"ID":"1038", "name":"Duke", "weight":90}
dog8 = {"ID":"1087", "name":"Pookie", "weight":16}
dog9 = {"ID":"1088", "name":"Abby", "weight":35}
dog10 = {"ID":"1120", "name":"Barney", "weight":65}
dog11 = {"ID":"1129", "name":"Autumn", "weight":20}
dog12 = {"ID":"1145", "name":"Hershey", "weight":100}
dog13 = {"ID":"1200", "name":"King", "weight":110}
dog14 = {"ID":"1211", "name":"Bosco", "weight":70}
dog15 = {"ID":"1222", "name":"Daisy", "weight":55}

#dictionaries for kennels
# under 50 pounds
kennel1 = {'kennel number':1, "dog":"empty"}
kennel2 = {"kennel number":2, "dog":"empty"}
#up to 99 pounds
kennel3 = {"kennel number":3, "dog":"empty"}
kennel4 = {"kennel number":4, "dog":"empty"}
kennel5 = {"kennel number":5, "dog":"empty"}
kennel6 = {"kennel number":6, "dog":"empty"}
#100 pounds and over
kennel7 = {"kennel number":7, "dog":"empty"}
kennel8 = {"kennel number":8, "dog":"empty"}

#function that finds dog based on ID
"""
name: SelectDog(dogs)
desc: look for dog's ID and return name and weight
parameters: combined dictionary dogs
return: name and weight
"""
def SelectDog(dogID, dogs):
          
    foundIt = False
    while(not foundIt):
        
        #search dictionary, if found, trip the flag
        for row,col in dogs.items():
            if (col.get("ID") == dogID):
                foundIt = True
                
    # search dogs for the entered ID, get the name and weight of the dog
    for row,col in dogs.items():
        if (col.get("ID") == dogID):
            dogName = col.get("name")
            dogWeight = col.get("weight")
        

    #return the dog's weight and name
    return dogName, dogWeight, dogID

#function that assigns dog to kennel
"""
name: KennelAssign(dogID, dogs, kennels)
desc: assign dog to a kennel, 
parameters: int dogID, combined dictionary dogs, combined dictionary kennels
return:
"""
def KennelAssign(dogID, dogs):
    
    nameWeight = SelectDog(dogID, dogs)
    dogName = nameWeight[0]
    dogWeight = nameWeight[1]
    
    if (dogWeight <= 50):
        if (kennel1.get("dog") == "empty"):
            kennel1["dog"] = dogName
            kennelNum = kennel1.get("kennel number")
            print(f"{dogName} was placed in kennel {kennelNum}.")
        elif (kennel2.get("dog") == "empty"):
            kennel2["dog"] = dogName
            kennelNum = kennel2.get("kennel number")
            print(f"{dogName} was placed in kennel {kennelNum}.")
        else:
            print ("Sorry, all kennels for dogs under 50 pounds are full.")
    if (50 < dogWeight <=99):
        if (kennel3.get("dog") == "empty"):
            kennel3["dog"] = dogName
            kennelNum = kennel3.get("kennel number")
            print(f"{dogName} was placed in kennel {kennelNum}.")
        elif (kennel4.get("dog") == "empty"):
            kennel4["dog"] = dogName
            kennelNum = kennel4.get("kennel number")
            print(f"{dogName} was placed in kennel {kennelNum}.")
        elif (kennel5.get("dog") == "empty"):
            kennel5["dog"] = dogName
            kennelNum = kennel5.get("kennel number")
            print(f"{dogName} was placed in kennel {kennelNum}.")
        elif (kennel6.get("dog") == "empty"):
            kennel6["dog"] = dogName
            kennelNum = kennel6.get("kennel number")
            print(f"{dogName} was placed in kennel {kennelNum}.")
        else:
            print ("Sorry, all kennels for dogs 51-99 pounds are full.")
    if(99 < dogWeight):
        if (kennel7.get("dog") == "empty"):
            kennel7["dog"] = dogName
            kennelNum = kennel7.get("kennel number")
            print(f"{dogName} was placed in kennel {kennelNum}.")
        elif (kennel8.get("dog") == "empty"):
            kennel8["dog"] = dogName
            kennelNum = kennel8.get("kennel number")
            print(f"{dogName} was placed in kennel {kennelNum}.")
        else:
            print ("Sorry, all kennels for dogs over 99 pounds are full.")
           

#display kennels to a txt file
"""
name: Display(kennels)
desc: display the kennels when sentinel value is entered, put info into a txt file 
parameters: combined dictionary kennels
return:
"""
def Display(kennelnum):
    
    print(kennelnum)
    fileName = "Kennels.txt"
    kennel = json.dumps(kennelnum)
    fileOut = open(fileName, "a")
    fileOut.write(kennel)
    fileOut.write("\n")
    fileOut.close()
    
    
    
#main function
def main():
        
    kennels = {"kennel1":kennel1, "kennel2":kennel2, "kennel3":kennel3, "kennel4":kennel4, "kennel5":kennel5, "kennel6":kennel6, "kennel7":kennel7, "kennel8":kennel8}
    dogs = {"dog1":dog1, "dog2":dog2, "dog3":dog3, "dog4":dog4, "dog5":dog5, "dog6":dog6, "dog7":dog7, "dog8":dog8, "dog9":dog9, "dog10":dog10, "dog11":dog11, "dog12":dog12, "dog13":dog13, "dog14":dog14, "dog15":dog15}
    
    IDnum = input("Enter the dog's ID number (e to exit): ")    
    while (IDnum != 'e'.lower()):
        
        SelectDog(IDnum, dogs)
        #print(SelectDog(IDnum, dogs)) - used to check my work
        KennelAssign(IDnum, dogs)
        IDnum = input("Enter the dog's ID number (e to exit): ")
    
    Display(kennel1)
    Display(kennel2)
    Display(kennel3)
    Display(kennel4)
    Display(kennel5)
    Display(kennel6)
    Display(kennel7)
    Display(kennel8)
    
    
        
main()
print("finished")

    
    