import numpy
import numpy as np

a = np.array([1, 2, 3, 4, 5, 6, 7])
print(a, type(a))
print(a+2)
print(a/2)
print(a+a)
print(a**2)


#%%%

#print("\n\n\nBREAK\n\n\n")

#TRY AND EXCEPT

#try:
   # num= input("Give me a number")
 #   num =int(num)
   # num2 = input("Give me another number")
  #  num2 = int(num2)
   # result = num / num2
   # print("The division result is", result)

#except ValueError:
   # print("Please give me a proper number")
#except ZeroDivisionError:
   # print("The second number can not be zero")

print("\n\n\nBREAK\n\n\n")

#DEF

def greet():
    print("Hello!")

greet()
print((greet))

print("\n\n\nBREAK\n\n\n")

def salute(name):
    print("Hello,", str(name).capitalize())
salute("santos")

print("\n\n\nBREAK\n\n\n")


#Lists
lst = [1, 3, 4, 5, 6, 7]
print(lst[2])

#Range of values in list

print(lst[2:5])

# Values before

print(lst[:3])

# Values after

print(lst[3:])

#Reverse Lists
print(lst[::-1])

print("\n\n\nBREAK\n\n\n")

# NDARRAYS

a =np.array([
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10]
])
print(a)

print(f"{a.ndim}, {a.size}, {a.shape}, {a.dtype}")

#a.ndim: dimension (rows)
#a.size: amount of values
#a.shape: dimensions (rows, columns)
#a.dtype: data type

print("\n\n\nBREAK\n\n\n")

#Arithmetic operations on ndarray

a1 = np.array([1, 2, 3])
a2 = np.array([4, 5, 6])
print(a1+a2, a1*a2)

a1 = np.array([[1,2,3],[4, 5, 6]])
print(a1+a2)

print("\n\n\nBREAK\n\n\n")

# INDEXING

b = np.array([
    [1, 2, 3, 4, 5], #First row is 0, second row is 1
    [6, 7, 8, 9, 10] #First column is 0, second column is 1 and so on
])
print(b[0][3]) #here it is first row, fourth column
print(b[0, 1]) #same thing

print("\n\n\nBREAK\n\n\n")

#multi dimensional array indexing

c = np.random.randint(0, 10, size=(3, 4, 5))
# 3 is the number of arrays created
# 4 is the number of rows
# 5 is the amount of columns
print(f"c={c}")

print("\nBREAK\n")

print(f"c[1] = {c[1]}") #1 refers to the second array created

print("\nBREAK\n")

print(f"c[1, 2] = {c[1, 2]}") #One array, third row

print("\n\n\nBREAK\n\n\n")

#SLICING

z = np.array(
    [1, 2, 3, 4, 5, 6, 7, 8, 9])
print(z)
print(z[1:5])

print("\nBREAK\n")

slice = z[1:5]
slice[0] = 99
print(z)
slice[:] = 99
print(z)