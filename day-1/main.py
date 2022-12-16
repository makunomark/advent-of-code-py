print("--- Day 1: Calorie Counting ---")


print("--- Part One ---")
# read file line by line
read_file = open("input.txt", "r")
lines = read_file.readlines()

all_elves = []
current_elf = []
for count, line in enumerate(lines):
    if line.strip().__len__() == 0:
        all_elves.append(current_elf)
        current_elf = []
    else:
        current_elf.append(int(line.strip()))
    
    if count == lines.__len__() - 1:
        all_elves.append(current_elf)
        current_elf = []

all_elves_calories_count = []
for elf in all_elves:
    total = 0
    for item in elf:
        total += item
    all_elves_calories_count.append(total)

# find the max
max = 0
for item in all_elves_calories_count:
    if item > max:
        max = item

print("The maximum amount carried by one elf is: ",max)

print("--- Part Two ---")
max1 = 0
max2 = 0
max3 = 0
for item in all_elves_calories_count:
    if item > max1:
        max3 = max2
        max2 = max1
        max1 = item
    elif item > max2:
        max3 = max2
        max2 = item
    elif item > max3:
        max3 = item
    
print("Sum of max 3 calories: ", max1 + max2 + max3)
