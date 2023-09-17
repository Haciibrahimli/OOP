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
# bütün tapşırıqları işləyərkən çalışın, metodlar yazın öz təxəyyülünüzə uyğun, təkcə atributlarla yetinməyin. Metodlar önəmlidir.
# 1. Bir Electronics class-ı yaradın. Ona name və power
#    atributları verin. Daha sonra ondan törəmə olan 2 class yaradın. 
#    Birinin adı HomeElectronics olsun, digərinin adı isə WorkElectronics olsun.
#    Və bu törəmə klasslara əlavə atributlar da verin.
#    Həmçinin ana(parent) classda show_power() deyə bir metod yazın.
#    Və törəmə classlarda istifadə edin.

# class Electronics:
#     def __init__(self,name,power):
#         self.name = name
#         self.power = power
#     def show_power(self):
#         return "this is power"

# class HomeElectronics(Electronics):
#     def __init__(self, name, power,colour,model):
#         super().__init__(name, power)
#         self.colour = colour
#         self.model = model

#     def show_power(self):
#         return "this is power"
    
# tv = HomeElectronics(name = "samsung",power = "123",colour = "black",model = "m2w45")
# tosser = HomeElectronics(name = "unknown",power="125",colour = "red",model = "S21")

# class WorkElectronics(Electronics):
#     def __init__(self, name, power,year):
#         super().__init__(name, power)
#         self.year = year
#     def show_power(self):
#         return "this is power"
# notebook = WorkElectronics(name = "macbook",power = "222",year = "2023")
# phone = WorkElectronics(name = "nokia",power = "1011",year = "2023")

# print(tosser.name)


# 2. Bir Area adlı class yaradın. Və bundan törəmə Square,
#    Triangle, Circle classları olsun. Atributları və metodları 
#    öz düşüncənizə uyğun yazın. (Polimorfizm anlayışından istifadə edin.)

# class Area:
#     def __init__(self,num):
#         self.num = num
# class Square(Area):
#     def __init__(self, num):
#         super().__init__(num)

# class Triangle:
#     def __init__(self,num):
#         super().__init__(num)
# class Circle:
#     def __init__(self,num):
#         super().__init__(num)
        

# 3. Bir class yaradın. Bu classın sadəcə num deyə bir atributu olsun. 
#    Və bir metodu olsun, hansı ki, metodu çağırdıqda istifadəçidən bir 
#    ədəd istəsin və num-la hasilini tapıb return etsin.

# class New:
#     def __init__(self,num):
#         self.num = num

#     def calculator(self):  
#         return self.num 
#     def User(self,user):  
#         self.user = user
#         return self.user * self.num
# user = int(input("Enter the number "))

# print(user())
    
# 4. Bir Animal class-ı yazın. Age, color, feet deyə atributları olsun. 
#    Daha sonra bu class-ı daxil olduğu moduldan başqa bir modula daxil
#    edərək törəmə bir Cat class-ı yaradın. 
#    Daha sonra Cat class-ının bir obyektini yaradın.
# class Animal:
#     def __init__(self,Age,color,feet):
#         self.Age = Age
#         self.color = color 
#         self.feet = feet

# class Cat(Animal):
#     def __init__(self, age, color, feet):
#         super().__init__(age, color,feet)


# cat1 = Cat(age=3, color="Yellow", feet=4)
# print(cat1.Age)
#

# 5. Travel deyə bir class yaradın. direction, price kimi atributları olsun.
#    Daha sonra BusTravel, FlyTravel kimi törəmə siniflər yaradın. 
#    Və əlavə atributlar verin.

# class Travel:
#     def __init__(self,direction,price):
#         self.direction = direction
#         self.price = price
#         return self.direction + " " + self.price
# class BusTravel(Travel):
#     def __init__(self, direction, price,breaktime):
#         super().__init__(direction, price)
#         self.breaktime = breaktime
#     def __str__(self):
#         return self.breaktime

# class FlyTravel(Travel):
#     def __init__(self, direction, price,foods):
#         super().__init__(direction, price)
#         self.foods = foods
#     def __str__(self):
#         return self.foods

# 6. Bir Animal class-ı yaradın. age, color kimi atributlar verin. 
#    Daha sonra ondan törəmə birdənə Mammals, və 
#    NonMammals deyə 2 dənə də class yaradın. Mammals və NonMammals classlarının
#    özündən də törəmə siniflər yaradın.
#    Məsələn, Cow deyə bir class Mammals-dan, Snake deyə bir class isə NonMammals 
#    varis alsın. Müxtəlif atributlar və metodlar verin.


# class Animal:
#     def __init__(self,age,color):
#         self.age = age
#         self.color = color
#         return self.age + " " + self.color
# class Mammals(Animal):
#     def __init__(self, age, color,price):
#         super().__init__(age, color)
#         self.price = price
#         return self.price
    
# class Cow(Mammals):
#     def __init__(self, age, color, price,weight):
#         super().__init__(age, color, price)
#         self.weight = weight
#         return self.weight
    
# class NonMammals(Animal):
#     def __init__(self, age, color,country):
#         super().__init__(age, color)
#         self.country = country
#         return self.country
    
# class Snake(NonMammals):
#     def __init__(self, age, color, country,length):
#         super().__init__(age, color, country)
#         self.length = length
#         return self.length
     
# 7. Car deyə bir class yaradın. Marka, model, year, color 
#    deyə atributları olsun. Daha sonra ondan törəmə sinifləri təxəyyülünüzə 
#    uyğun yazın, müxtəlif atribut və metodlar yazmağı unutmayın.


# class Car:
#     def __init__(self,marka, model, year, color):
#         self.marka = marka
#         self.model = model
#         self.year = year
#         self.color = color
    
# class sport(Car):
#     def __init__(self, marka, model, year, color,maxspeed):
#         super().__init__(marka, model, year, color)
#         self.maxspeed = maxspeed
        
# car1 = sport(marka = "Ford",model = "MustangElanor",year = "1976",color = "black",maxspeed = "220")
   
# class crossover(Car):
#     def __init__(self, marka, model, year, color,power):
#         super().__init__(marka, model, year, color)
#         self.power = power
       

# car2 = crossover(marka = "Toyota",model = "prado",year = "2020" ,color = "black",power= "180hp")    

# class offroader(Car):
#     def __init__(self, marka, model, year, color,hppower):
#         super().__init__(marka, model, year, color)
#         self.hppower = hppower
        
# car2 = offroader(marka = "Jeep",model = "Wrangler",year = "2014",color = "white",hppower= "260hp")

# print(car2.marka)

# burda mes maxspeed niya car 3 olan class  aid olur

# 8. MyCard deyə bir class yaratmalısınız. username, balance, pin_code 
#    atributlarını verin. Daha sonra get_cash() deyə bir metod yaradın, 
#    hansı ki, bu metodu çağıranda bizdən məbləğ istəsin, əgər balansdakı
#    puldan çox deyilsə, pin_code-ni istəsin, doğru olduğu halda həmin məbləği
#    balansdan çıxarsın və "Uğurlu əməliyyat, balansınız: (balansda qalan pul)".
#    Həmçini in_cash() deyə bir metod yazın, istifadəçidən məbləğ istəyin,
#    daha sonra pin_codeni istəyin, pin_code doğru olarsa, həmin məbləği
#    balansla toplayın, balansımız o olsun. Birdənə də send_money() metodu yazın.
#    Bu metodu da işə saldıqda  16 rəqəmli kart nömrəsi istəyin.
#    Əgər daxil edilənlərdən hamısı rəqəmdirsə və 16 rəqəmlidirsə,
#    köçürüləcək məbləği istəyin. Köçürüləcək məbləğ balansdan çox olmadığı 
#    təqdirdə balansdan həmin məbləği çıxın və "Uğurlu köçürülmə" return etsin.
