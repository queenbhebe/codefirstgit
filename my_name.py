print ("What's your name?")
name = raw_input()
print ("Hello" + name)

def add_two_numbers(num1,num2):
    sum = num1 + num2
    return sum


def hello_world(a,b):
    c = a + b
    print(str(c))

print ("Hello World!")

a=int(input("Input number 1: "))
b=int(input("Input number 2: "))

c  = add_two_numbers(a,b)
print(c)
