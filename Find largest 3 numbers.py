a = int(input("Enter your 1st number : "))
b = int(input("Enter your 2nd number : "))
c = int(input("Enter your 3rd number : "))
if (a>=b) and (a>=c):
    largest = a
elif (b>=a) and (b>c):
    largest = b
else:
    largest = c
print("The largest number is :",largest)
