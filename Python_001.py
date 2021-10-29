#First Lesson
print("Hello World")

#Variables and Types
height = 1.72
weight = 67

BMI = weight/height**2

#str = string
#float = float
#bool = Boolean
#type = determining the type of the data types
print(BMI)
print(type(BMI))

x = 5
y = 7
z = x + y + 1
print(z)

a = False
b = 'false'
print(type(a), type(b))

###### Python List ######
ls = ["2021", 1.72, "2020", 1.71, "2019", 1.70]
#### sublist ####
ls2 = [["2021", 1.72],
       ["2020", 1.71],
       ["2019", 1.70]]

print(ls2)

#### subsetting List ####
print(ls[2])
print(ls2[1])

#### list slicing ####
print(ls[0:3])

#changing list element
ls[0] = "2022"

#adding element to List
#ls + ["2021", 1.73]

#delete element from List
#del(ls[0])

###### Python Functions ######
ls3 = [1, 2, 2, 3, 5]
print(max(ls3))
#round decimal digit
print(round(1.69, 1))
#round
print(round(1.69))

###### Method ######
print(ls3.index(2))
print(ls3.count(2))
print(ls3.append(6))
print(ls3)

a = "lgs"
print(a.capitalize())
