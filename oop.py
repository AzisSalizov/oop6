# Создайте аналог телефонной книги. Каждая запись в книге должна иметь идентификационный номер, имя, фамилия, дату рождения, профессию.
# Напишите для этого класса метод get_information которая будет выдавать информацию об экземпляре этого класса.

# Пример входных данных:

# >>>from datetime import date >>> >>>c = Contact(id=1,       first_name='John',       last_name='Dow',       birth_date=date(day=21, month=4, year=1996),       profession='Python developer')
# Пример выходных данных:

# >>>c.get_information()

# ID - 1
# Full name - John Dow
# Birth Date - 21.04.1996
# Profession - Python developer

# id = int(input('Введите ID : '))
# name = input('Введите Имя : ')
# last_name = input('Введите Фамилию : ')
# birth_date = input('Введите Дату Рождению (dd.mm.yy): ')
# profession = input('Введите профессию : ')

# class phoneBook:
#    def __init__(self , id , name , last_name , birth_date , profession) -> None:
#       self.id = id
#       self.name = name
#       self.last_name = last_name
#       self.birth_date = birth_date
#       self.profession = profession
      
#    def get_information(self):
#       return f'ID - {self.id}\nFull name - {self.name} {self.last_name}\nbirth_date - {self.birth_date}\nprofession - {self.profession}'
   
# phone = phoneBook(id , name , last_name , birth_date , profession)
# print(phone.get_information())


# Создайте иерархию классов для описания фауны со следующими требованиями:
# Обязательное присутствие классов птиц, рыбы и млекопитающих. Напишите для них методы и парамметры свойственные для животных этих классов.
# Так же обязательное присутствие классов хищников и травоядных. У классов хищник и травоядное обязательно должен быть метод eat.
# Этот метод должен показывать, чем питается животное.
# Создайте классы сокол, пингвин, форель, кит. Наследуйте эти классы от вышеуказанных классов, при наследовании обратите внимание на природные свойства животных этих классов.
# Если есть необходимость, перепишите методы родителя для того чтобы эти методы соответствовали свойствам животного. Создайте экземпляры классов сокол, пингвин, форель, кит.
# Вызовите все доступные им методы
# Пример:
# >>>p = Penguin(type='royal', age='1 year')
# >>>p.eat()
# I eat fish
# >>>p.can_swim()
# True
# >>>p.can_fly()
# I cannot fly


# class birds():
#    def __init__(self, name ) -> None:
#       self.name = name 
      
#    def can_fly(self):
#       return f'Я умею летать'
   
# class fishs():
#    def __init__(self, name) -> None:
#       self.name = name
      
#    def can_swim(self):
#       return True
   
# class mammals():
#    def __init__(self, name) -> None:
#       self.name = name
   
#    def can_bite(self):
#       return f'Я могу укусить'
   
   
#    # У классов хищник и травоядное обязательно должен быть метод eat
   
# class lion():
#    def __init__(self, name , food ) -> None:
#       self.name = name
#       self.food = food
      
#    def can_hunt(self):
#       return f'Я умею охотиться'
   
#    def eat(self):
#       return f'Я питаюсь {self.food}'
   
# class snake():
#    def __init__(self, name , food) -> None:
#       self.name = name
#       self.food = food
      
#    def eat(self):
#       return 'я питаюсь мышами'
#    # сокол, пингвин, форель, кит
   
# class sokol(lion, birds):
   
#    def __init__(self, name , food) -> None:
#       super().__init__(name , food)
      
# class penguin(lion, fishs):
   
#    def __init__(self, name , food) -> None:
#       super().__init__(name, food)
      
# class trout(penguin,fishs):
   
#    def __init__(self, name ,food) -> None:
#       super().__init__(name , food)
      
# class whale(penguin,fishs):
   
#    def __init__(self, name , food) -> None:
#       super().__init__(name, food)
      
# sokoll = sokol('sokol', 'suslik')
# print(f'Я {sokoll.name.capitalize()}.\nУмеешь летать ? - {sokoll.can_fly()}\n{sokoll.eat()}\n{sokoll.can_hunt()}')
# print('--' * 70)
# p = penguin('penguin' , 'fish')
# print(f'Я {p.name.capitalize()}.\nУмеешь плавать? -  {p.can_swim()}\n{p.eat()}')
# print('--' * 70)
# t = trout('trout' , 'fish')
# print(f'Я {t.name.capitalize()}.\nУмеешь летать ? -  {t.can_swim()}\n{t.eat()}')
# print('--' * 70)
# w = whale('whale', 'fish')
# print(f'Я {w.name.capitalize()}.\nУмеешь плавать ? -  {w.can_swim()}\n{w.eat()}')



# Вам дана функция:

# def show_even_numbers(*args): even_numbers_lst = [] for i in args: try: if i%2 == 0: even_numbers_lst.append(i) except TypeError: continue return even_numbers_lst
# Напишите декоративную функцию для этой функции чтобы выводить каждое чётное число введённое в эту функцию раздельно, а так же указывать каким номером вы их получили.

# Пример выходных данных:

# >>>show_even_numbers(3, 8, 'hello', 100, [14, 13, 12], 12)
# 1 - 8
# 2 - 100
# 3 - 12

def decorator(func):
   def show_even_numbers(*args):
      even_numbers_lst = []
      for i in args:
         try:
            if i%2 == 0:
             even_numbers_lst.append(i)
         except TypeError:
             continue
      for i in even_numbers_lst:
           print (i)
   return show_even_numbers

@decorator
def f(s):
    print('num')
f(3, 8, 'hello', 100, [14, 13, 12], 12)
   