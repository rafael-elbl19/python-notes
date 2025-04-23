age = int ( input("Enter your age: ") )

if age < 18:
    print("Blocked")
elif age >= 18 and age <= 60:
    print("Allowed")
else: 
    print("Blocked by age, sir ")

text = input("Write your name, age and sex ( , , )")
Data = text.split(", ")
name = Data[0]
age = Data[1]
sex = Data[2]
print(name)
print(age)
print(sex)