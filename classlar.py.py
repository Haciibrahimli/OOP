# 1. Bir Person class-ı yaradın. Daha sonra ona 5 atribut verin.
# Elə edin ki, bir obyekt yaratdıqdan sonra çapa verdikdə onun 2 
# əsas atributu vergüllə ekranda görünsün.
# class Person:
#     def __init__(self,age,name,colour,gender,adress) :
#         self.age = age
#         self.name = name
#         self.colour = colour
#         self.gender = gender
#         self.adress = adress

#     def __str__(self):
#         return str(self.age) + "," + self.name 

# person1 = Person(age = "25",name ="Ali",colour="white",gender="mail",adress="str.M.E.Resulzade 1" )

# print(person1)

# 2. Bir Animal class-ı yaradın. Və 3 atribut verin.
#    Daha sonra bu class üçün 1 dənə də metod yazın.
#    Hansı ki, Animal-ın yaş atributunun üzərinə 10 gəlib bizə qaytarır. 
#    Daha sonra aşağıda bir obyekt yaradın və metodu işə salın.
# class Animal:
#     def __init__(self,name,age,colour):
#         self.name=name
#         self.age=age
#         self.colour=colour
#     def __str__(self):
#        return self.age + 10
# cat = Animal(name = "mestan",age=2,colour="white", ) ????


# 3. Bir Workers class-ı yaradın. Daha sonra name,
#    surname, fullname kimi atributları olsun.
#    Fullname elə edin ki, name və surname-nin boşluqla birləşmiş forması olsun.

# class Worker:
#     def __init__(self,name,surname,fullname):
#         self.name = name
#         self.surname = surname
#         self.fullname = fullname 
#     def __str__(self):
#         return self.name + " " + self.surname + " " + self.fullname
# person1 = Worker(fullname = " ",name = "Ali",surname = "Aliyev",)
# print(person1)
      
# 4. Bir Electroincs class-ı yaradın. Müxtəlif atributlar verin.
#    Həmçinin, is_useful deyə bir atribut da verin və True olduqda
#    cihazın işlədiyi, False olduqda işləmədyini bilmək üçün.

# class Electronic:
#     def __init__(self,colour,condition,is_useful):
#         self.colour = colour
#         self.condition = condition
#         self.is_useful = is_useful

    
# 5. Bir Square class-ı yaradın. Onun tərəf atributunu verin.
#    Daha sonra onun sahəsini və perimetrini hesablamaq üçün metodlar yazın 
#    class-ın içində. Daha sonra class-dan kənarda bir obyekt yaradın,
#    və metodları obyekt üzərində istifadə edin. p =4*a a ** 2
# class Square:
#     def __init__(self,a):  
#         self.a = a
#     def square(self,a):
#           return a ** 2
#     def perimetr(self,a):
#          return a ** 4
#     def area_calculator():
#         figure = input("Which figure ?\n 1.Perimetr\n2.Square\n3")
#         if figure == "1":
#          area = int(input("Enter the main side: "))
#         return square(self,a)
#         if figure == "2":
#         side = int(input("Enter the any side of square: "))
#         return square(self,a):
# print(area_calculator()) ??????
# ​
    

# 6. Bir Person class-ı yaradın. name, surname, birth_year kimi atributları olsun.
#    Daha sonra bir metod yazın class-ın içindəki hansı ki, biz o metodu çağıranda
#    yaşını qaytarsın obyektin.

# class Person:
#     def __init__(self,name,surname,birth_year):
#         self.name = name
#         self.surname = surname
#         self.birth_year = birth_year
#     def __str__(self):
#         return self.birth_year
# per1 = Person(name = "Ali",surname = "Alyev",birth_year = "1989")
# print(per1)

         
# class Person:
#     yas = 5
# p = Person()
# p5 = Person()

# print(p.yas, p5.yas)


# class Animal:
#     def __init__(self, color, age):
#         self.color = color
#         self.age = age
#
#
# cat = Animal(color='white', age=1)
# dog = Animal(color='brown', age=2)
#
# print(cat.color, cat.age)
# print(dog.color, dog.age)


# class Vehicle:
#     def __init__(self, color, energy_type):
#         self.color = color
#         self.energy_type = energy_type
#
#     def __str__(self):
#         return self.color + "->" + self.energy_type
#
# car = Vehicle(color='black', energy_type='gasoline')
# print(car)


# class Electronics:
#     def __init__(myself, condition, color):
#         myself.condition = condition
#         myself.color = color
#     def __str__(myself):
#         return myself.condition
# wash_machine = Electronics(condition="New", color="Gray")
# print(wash_machine)

# class Animal:
#     def __init__(self, name, age, color):
#         self.name = name
#         self.age = age
#         self.color = color
#
#     def __str__(self):
#         return self.name + "," + str(self.age) + ","
#
# cat = Animal(name="Mestan", age=1, color='gray')
# dog = Animal(name='Husky', age=2, color='black')
#
# del cat.color
# dog.age = 5
#
# print(cat)
# print(dog)
# class Person:
#     pass          