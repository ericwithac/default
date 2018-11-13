text = "lorem ipsum     lorwm ipsum ipsumlor   lorlorlowlor lsdspldkkjddfdfdsfdfdf  lor dsfsff"
a = 0
x = 0
while a >= 0: #finds index value for each occurance of string in document
    a = text.find("lor",a)
    if a < 0:
        break
    else: 
        print(a) #remove this to only return number of occurances
        a = a + 1
        x = x + 1
        
print (x)    # counts number of strings found in doc