# Caiya Mimms | Jan 28,2023
# Planting_Grapevines_Program | HW #2.13
# Calculates number of grapevines that will fit in the row (User Inputs = 3)

print("I heard through the grapevine that this program calculates number of grapevines that will fit in the row.(get it?)")

    #INPUTS ( 3 reqired)

    #defining R,E,S inputs 
R = float(input("What is the length of the row? (In feet): "))
E = float(input("What is the amount of space used by an end-post assembly? (In feet): "))
S = float(input("What is the amount of space between the vines? (In feet): "))

    #Apllying formaula
V = (R - (2 * E)) / S


    #OUTPUTS
print("The number of grapevines that will fit in this row will be ",V)

    #End Statement
print("End Program. I didnt know you liked grapes like that.")