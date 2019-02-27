# Topics to test basic python knowledge

# 1. Lists
lst = [1, 2, 3]
# add values to lists
lst.append(3)
# insert things anywhere
lst.insert(0, 5)
# indexing through Lists
lst[1]
# get index of an element
lst.index(2)
# slice listt
lst[0:2]

# 2. Strings
mystring = "Hello"
mystring += " world."
print(mystring)

# 3. data type conversion
num_int = 123  # int type
num_str = "456"
num_str = int(num_str)

# 4. Loops
some_list = [1, 2, 3, 4, 5, 6]
for i in some_list:
    print(i * 2)

# 5. Conditions
nl=[]
for x in range(1500, 2701):
    if (x%7==0) and (x%5==0):
        nl.append(str(x))
print (','.join(nl))

# 6. Access index of a list
nums = [5, 15, 35, 8, 98]
for num_index, num_val in enumerate(nums):
print(num_index, num_val)

# 7. Merge two lists (same length)
names = ['peter', 'paul', 'marie']
ages = [20, 30, 40]
for name, age in zip(names, ages):
    print(name, age)

# 8. Difference between  two lists
list1 = [1, 2, 3, 4]
list2 = [1, 2]
print(list(set(list1) - set(list2)))

# 9. Convert lists to dictionary
name = ['peter', 'paul', 'marie', 'max']
age = [20, 30, 40, 18]
print([{'name': f, 'age': c} for f, c in zip(name, age)])


### FUNCTIONS ###
# function: sum items in a list
def sum_list(items):
    sum_numbers = 0
    for x in items:
        sum_numbers += x
    return sum_numbers
print(sum_list(some_list))

# function: multiply items
def multiply(numbers):
    total = 1
    for x in numbers:
        total *= x
    return total
print(multiply(some_list))

# function: largest number of a lists
def max_num_in_list( list ):
    max = list[ 0 ]
    for a in list:
        if a > max:
            max = a
    return max
print(max_num_in_list([1, 2, -8, 0]))

#### NUMPY ####
# multiply matrices with numpy
import numpy as np
x = np.random.random((5,3))
print("First array:")
print(x)
y = np.random.random((3,2))
print("Second array:")
print(y)
z = np.dot(x, y)
print("Dot product of two arrays:")
print(z)
