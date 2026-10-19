# Make a list of elements (more elements added)
elements = ["privet", 20, 4, True, [4, 5, 'fdg'], "poka", 3536, -668, 
            (5, 6), "lalalala", 6.345, {111, 222, 333}, "str"]

# Just to count strings
count_of_str = 0

for element in elements:
    if type(element) == str:
        count_of_str += 1

print("Number of strings: ", count_of_str)