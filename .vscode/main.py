
# CONDITIONALS
age = int(input("Enter your age: "))
if age < 18:
    print("Blocked")
elif age >= 18 and age <= 60:
    print("Allowed")
else:
    print("Blocked by age, sir ")

# USING SPLIT AND ARRAYS
text = input("Write your name, age and sex ( , , )")
Data = text.split(", ")
name = Data[0]
age = Data[1]
sex = Data[2]
print(name)
print(age)
print(sex)

# USING LISTS
empty_list = []
empty_list.append("Hello!")
empty_list.append(22)
print(empty_list)

numbers = [10, 1020, 2, 199, 398]
print("Total indexes: ", len(numbers))
print("Total value: ", sum(numbers))
print("Minor value: ", min(numbers))
print("Major value: ", max(numbers))

# FOR E WHILE
alumn = []
for x in range(2):
    alumn_code = input("Code: ")
    alumn_grade = input("Grade: ")
    result = [alumn_code, alumn_code]
    alumn.append(result)

for n in alumn:
    alumn_code = n[0]
    alumn_grade = n[1]
    print("Code: ", alumn_code, ", Grade: ", alumn_grade)
