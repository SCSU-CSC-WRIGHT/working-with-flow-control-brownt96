number = int(input("Enter any number: "))
total = 0
while number <= 0:
    print ("Use a positive number")
    number = int(input("Enter any number: "))

for i in range (1, number+1):
    total+=i
    print(total)