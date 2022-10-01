#Nitish
#Print Multiplication Table for Any Number
number=int(input("Enter number "))
print("Multiplication Table of ",number," is ")
for i in range(1,11):
    print(number,"  X  ",i,"  =  ",(number*i))
