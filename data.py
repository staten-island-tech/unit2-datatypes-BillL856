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

