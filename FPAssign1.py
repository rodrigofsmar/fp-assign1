# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 16:42:11 2024

@author: rodri
"""

def chooseTypeOfSatisfaction():
     """
     Asks the user for the type of satisfaction to be verified (general or weak).
     
     Returns
     -------
     String
         A string with one of the "G", "W" values.

     """
     result = input("Verify general or weak satisfaction (G/W)?: ")
     while result not in ["G","g","W","w"]:
        print("Must choose G or W")
        result = input("Verify general or weak satisfaction (G/W)?: ")
     return result.upper()


def verifyPropertyInPath(path, pathProp, typeOfSat):

    #Split path into list
    pathPlaces = [place.split('/') for place in path.split(';')]

    #Split property into a list of tuples
    #1st position: int representing the position
    #2nd postion: list of characteristics
    propertyList = []
    for property in pathProp.split(';'): #creates a list of property segments
        index, characteristics = property.split(':') #assigns relative positive to index and characteristics to characteristics
        index = int(index) #converts index to int
        characteristics = characteristics.split('/') #creates list of characteristics
        propertyList.append((index, characteristics)) #appends tuple to propertyList

    def checkPlaceSatisfaction(place, required_chars):
        if typeOfSat == 'G':  # General satisfaction
            return all(char in place for char in required_chars)
        elif typeOfSat == 'W':  # Weak satisfaction
            return any(char in place for char in required_chars)
        
    currentPosition = 0
    for index, characteristics in propertyList:
        #circular path
        nextPosition = (currentPosition + index) % len(pathPlaces)

        if not checkPlaceSatisfaction(pathPlaces[nextPosition], characteristics):
            return False #in case the property is not satisfied
        
        currentPosition = nextPosition #update current position

    return True #in case all properties were satisfied


    #print(pathPlaces)
    #print(propertyList)







####################################################################
####################################################################
   

#PROPERTIES = ("niceViews","childFriendly","nightCool","safe","cultural",\
#              "openAirActivs","goodFood")

# Let us interact with the user!
wantToContinue = True
while wantToContinue:
    path = input("Please input the path: \n")
    wantMoreProps = True
    while wantMoreProps:
        pathProp = input("Please input the property you want to verify: \n")
        typeOfSat = chooseTypeOfSatisfaction()
        satisfies = verifyPropertyInPath(path, pathProp, typeOfSat)
        print("The path does", "" if satisfies else "not", "satify the property")
        userWill = input("Do you want to verify another property on the same path (Y/N)? ")
        wantMoreProps = userWill.lower() == "y"
    # Should the interaction end after this turn?
    userWill = input("Do you want to process another path (Y/N)? ")
    wantToContinue = userWill.lower() == "y"

print("Bye")

