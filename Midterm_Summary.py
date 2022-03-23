# Session 1 & 2

#  IDE --> Integrated Development Environment
# Popular IDEs: Eclipse, Atom, Pycharm , Visual Studio

# Source Control: term used to describe a system that allows the tracking
# and managing of changes to code.

# Session 3 & 4

# Definitions are either ways to assign names to values or
# creating new "procedures" that we want to use as primitives

# Commands are statements that instruct the interpreter to do something.

# All objects have an identity, type and value.
# Identity - never changes for an object.
# Type - determines the operations it can support and define the possible values it can have. We can use the function type() to get the type of an object.
# Value - Objects whose value change are called "mutable", while objects whose value cannot change after being created are called "inmutable"

# Basic Scalar Objects:
# int - basic integer numbers: 5, 0, -6
# float - real numbers: 2.3, 0.4, -5.0
# bool - Boolean value: True or False
# NoneType - special type, has only one value: None

# TRY/EXCEPT SYNTAX AND FUNCTIONALITY

try:
    num = input("Give me a number")
    num = int(num)
    num2 = input("Give me another number")
    num2 = int(num2)
    result = num / num2

except ValueError:
    print("Please give me a proper number")
except ZeroDivisionError:
    print("The second number can not be zero")
except:
    print("Some other exception I did not see coming")
else:
    print("The division result is", result)


# IF STATEMENT

# If the logical condition is true, then the indented statement gets executed.
# If the logical condition is false, the indented statement gets skipped.
# Si no sabes como empezar con el if statement, basicamente usa if True: y seguis con el indented block q es lo de else y elif.

if number % 2 == 0:
    print(number, "is an even number")
    print(“Nothing would be printed if it were odd”)

# In this if statement, there's two options.
    # Only one of them gets executed based on the condition evaluated.
# If the condition is true, then the indented statement gets executed.
#If the condition is false, the indented statement after else gets executed.

if number % 2==0:
    print(number, "is an even number")
else
    print(number, "is an odd number")

# Sometimes there's more than 2 possibilities:

if a > b:
    print(a, ">", b)
elif a < b:
    print(a, "<", b)
else:
    print(a, "=", b)


# WHILE STATEMENTS
# similar to the if statement.

    while True:
        num = input("Give me a number (type quit to exit)")
        num2 = input("Give me another number(type quit to exit)")
        if num == "quit" or num2 == "quit":
            break
        num = int(num)
        num2 = int(num2)
        if num2 == 0:
            print("Can not divide by zero")
            continue
        print("The division result of", num, "and", num2, "is", num / num2)

# STRING OPERATIONS
# The len() function will return the length of a string.

salute = "hey there!"
    len(salute)

# FILES

# to open a file we use open()
#first parameter is the filename (path included), second parameter is the mode.
# The modes are: r (read), w (write), x (exclusive creation), a (append), b (binary), t (text), + (update).

fp = open("text.txt", "r")
print(fp)
all = fp.read()
print(all)
fp.close()

<_io.TextIOWrapper name='text.txt' mode='r' encoding='cp1252'>
#This is a file I wrote
#I made it quite short
#There are only 3 lines


# ONce the file is open we use write().
fp = open("text.txt", "a")
print(fp)
line = input("Give me some text, don't be shy: ")
fp.write(line)
fp.write("\n")
fp.close()
#this program will keep appending to the file

# we can simplify the process using the with statement
with open("text.txt", "a") as fp:
    print(fp)
    line = input("Give me some text, don't be shy: ")
    fp.write(line)
    fp.write("\n")


# Random Values
import random

for i in range(10):
    x = random.random()
    print(x)

>>> random.randint(5, 10)
7
>>> random.randint(5, 10)
10

>>> ppl = ["Jon", "Ana", "Maria", "Jim", "Florence", "George", "James"]
>>> random.choice(ppl)
'James'
>>> random.choice(ppl)
'Maria'
>>> random.choice(ppl)
'George'

# LISTS
# A list is a sequence of values. They are mutable.
#You define a list by enclosing it between [] and separated by ","

>>> lst = [1, 3, 5, 7, 9]
>>> lst[1]
3
>>> lst[1] = 11
>>> print(lst)
[1, 11, 5, 7, 9]
>>> lst[1] = lst[2]
>>> print(lst)
[1, 5, 5, 7, 9]
>>> lst[6] = 10
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: list assignment index out of range
>>> 1 in lst
True

# TUPLE
# It is a sequence of values. They are immutable, constructed w the built-in function: tuple.
# Enclose its elements between () and separated by ",".

# DICTIONARIES
# A more general type of list, the indices can be almost any immutable object.
# In dictionaries, the index is called a key, the keys need to be unique.
>>> d = {'one': 'uno', 'two': 'dos', 'three': 'tres'}
>>> d
{'one': 'uno', 'two': 'dos', 'three': 'tres'}    <<< order not important!
>>> d[1]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 1
>>> d["two"]
'dos'
>>> d["yes"]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'yes'

# You can add and delete elements to/from a dictionary
>>> d
{'John': 7, 'Mary': 9, 'James': 4, 'Jane': 6, 'Jorge': 8}
>>> d = {"John":7, "Mary":9, "James":4, "Jane":6, "Jorge":8}
>>> d["Ana"] = 9
>>> d
{'John': 7, 'Mary': 9, 'James': 4, 'Jane': 6, 'Jorge': 8, 'Ana': 9}
>>> del(d["Mary"])
>>> d
{'John': 7, 'James': 4, 'Jane': 6, 'Jorge': 8, 'Ana': 9}

# GET THE 10 MOST COMMON WORDS THAT APPEAR IN A FILE:
punctuation2 = ",.;:!?\"'()[]{}-*<>"
def common_words(file_name):
    fd = open(file_name, "r")
    d = {}
    for line in fd:
        for c in punctuation2:
            line = line.replace(c, " ")
        words = line.split()
        for word in words:
            if word in d:
                d[word] += 1
            else:
                d[word] = 1


    values = list(d.values())
    values.sort(reverse=True)
    common = []
    for numbers in values[:10]:
        for keys in d:
            if d[keys] == numbers:
                common.append((keys, numbers))
    print("the most common words are:")
    for i in common:
        print(i[0], i[1], "times")

#Creating ndarrays
# The function np.array() can be used to create an ndarray.

a = np.array([
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10]
])
print(a)

#ndim, size and shape attributes give info about the size of the array,
#while dtype gives information about the data type

print(f"{a.ndim}, {a.size}, {a.shape}, {a.dtype}")

# 2, 10, (2, 5), int64

# DATA VISUALIZATION IN PYTHON
# Most common library to visualize data is pyplot.
# In pyplot you can plot two lists, one on the X-Axis and one on the Y-Axis.
# These lists need to have the same number of elements.

from matplotlib import pylab as plt

series1 = []
series2 = []
series3 = []

for i in range(0,30):
    series1.append(i)
    series2 += [i*i]
    series3 += [i**3]

plt.plot(list(range(0,30)), series1)
plt.plot(list(range(0,30)), series2)
plt.plot(list(range(0,30)), series3)
plt.show()

#Separate each graph in their own window
figure()

#Label axes
xlabel("")
ylabel("")

# Improvements to data visualization
from matplotlib import pylab as plt
series1 = []
series2 = []
series3 = []

for i in range(0,30):
    series1.append(i)
    series2 += [i*i]
    series3 += [i**3]
plt.figure("first")
plt.plot(list(range(0,30)), series1)
plt.figure("second")
plt.plot(list(range(0,30)), series2)
plt.figure("third")
plt.plot(list(range(0,30)), series3)

plt.figure("first")
plt.title("Linear")
plt.ylim(0, 1000)
plt.xlabel("Series")
plt.ylabel("Linear Progression")
plt.figure("second")
plt.title("Quadric")
plt.figure("third")
plt.title("Cubic")
plt.ylabel("Cubic Progression")
plt.show()


