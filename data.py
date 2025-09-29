#Floats represent numbers with decimal values
""" x = 3
y = float(3)
print(x,y)

values = [1,2.23,5,7,2,30,15]
print(values)
for i in values:
    print(i)

print(values[0])
print(values[6]) """

#Strings are a list of characters that represent text. It's important to understand that a String is not simply "just text", it is instead a list of characters. For example, "test" is really a list with each letter stored as an element in a list.
""" "test"
["t","e","s","t"]

x = "this is a thing"
y= x.split( )
z = y[0]
print(y)
print(z) """

#Here we can use the split function which allows for an parameter to be passed in. The parameter passed in will be used to split the string into a new list. By using an empty space we can break up our words into seperate elements. Since we know how to access elements in a list we can then store the first word as a seperate variable to be used later

type_a_sentence = input("How are you feeling?")
a = type_a_sentence.split()
b =(len(a))
print(b)

""" day_of_week = input("what day is it? ")
if day_of_week == "Friday":
    print("correct")     
else:
    print("incorrect")

x = "test"
print(f"hello {x}")

temp = 75
if temp > 68:
    print('warm')
elif temp == 68:
    print('perfect')
else:
    print('cold') """

#Odd or Even challenge

number = input("Type a number")
if int(f"{number}") % 2 ==0:
    print("even")
else:
    print("odd") 



#Tip challenge
bill=input("What is the bill?")

service=input("How is the service?")

if service == ("bad"):
    final= (float(bill)) * 1
    print(float(f"{final}"))
elif service == ("okay"):
    final= (float(bill)) * 1.15
    print(float(f"{final}"))
elif service == ("good"):
    final= (float(bill)) * 1.2
    print(float(f"{final}"))
elif service == ("great"):
    final= (float(bill)) * 1.25
    print(float(f"{final}"))

#Factor challenge

""" def factors(x,y):
    if x % y:
        print(f"{y} is a factor of {x}")
    else:
        print(f"{y} isn't a factor of {x}") """

m= int(input("Type a whole number"))
def factors(m):
    y = []
    for i in range(1, m+1):
        if int(m) % int(i) == 0:
            y.append(i)
    print(y)
factors(m)


#GCF challenge
x= int(input("Type another whole number"))
y= int(input("And another one"))
def gcf(x,y):
    e=[]
    for i in range(1, min(x,y)+1):
        if x%i==0 and y%i==0:
            e.append(i)
    print(max(e))
gcf(x,y)