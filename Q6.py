a=int(input("Enter the year: "))
b=a%100;
c=a%400;
print(" YEAR: ",a);
if((b%2)and(c%2)):
    print("The year you mentioned is a non leap year");
else:
    print("The year you mentioned is a LEAP YEAR");
