elements = ['privet', 20, 4, True, [4, 5, 'fdg'], (5, 6), 6.345, {111, 222, 333}, "str"]

count_of_str = 0

for element in elements:
    if type(element) == str:
        count_of_str += 1

print(count_of_str)