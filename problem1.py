''' an integer, , perform the following conditional actions:

If  is odd, print Weird
If  is even and in the inclusive range of 2 to 5, print Not Weird
If  is even and in the inclusive range of 6 to 20, print Weird
If  is even and greater than 20, print Not Weird'''

n = int(input("enter a number: "))

a = n%2 

if a == 1:
    print("Weird")
    
elif a == 0 and n >=2 and n <=5:
        print("Not Weird")

        
elif a==0 and n >=6 and n <=20:
        print("weird")
        
elif a==0 and n > 20:
        print("Not Weird")

