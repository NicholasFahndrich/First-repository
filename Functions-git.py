# 4.13.3: Greetings
# Nicholas Fahndrich
# 2/5/19

'''
name = input("What is your name: ")

def greeting():
    print("Hi there " + name + "! ")
    print("Nice to meet you")

greeting()



# 4.13.4: Functions And Variables
# Nicholas Fahndrich
# 2/18/19

x = 6

def print_something():
    x=3
    print (x)

print_something()
print (x)
'''


# 4.13.5: Functions and Variables, Part 2
# Nicholas Fahndrich
# 2/18/19

my_variable = 3.46745

def something():
    print (my_variable + 10)

something()

# 4.14.5: Default Parameter Values
# Nicholas Fahndrich
# 2.19.19


def print_two_number(x, y = 20):
    print('First Number:', x)
    print('Second Number: ' + str(y))

print_two_number(34, 45)
print_two_number(78)


# 4.14.6: Print Sum
# Nicholas Fahndrich
# 2.19.19

def print_sum(x, y):
    print(x + y)

print_sum(46,62)
