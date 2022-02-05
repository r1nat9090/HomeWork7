# class Test:
#
#     def __init__(self, ar1,ar2):
#         self.ar1 = ar1
#         self.ar2 = ar2
#
#     def __str__(self):
#         return f'info: param_1 = {self.ar1}, param_2 = {self.ar2}'
#
#     # def __del__(self):
#     #     print('Deleted')
#
#     def __add__(self, other):
#         return Test(self.ar1 + other.ar1, self.ar2 + other.ar2) # плюс
#
#     def __sub__(self, other):
#         return Test(self.ar1 - other.ar1, self.ar2 - other.ar2) # минус
#
# a = Test(2, 1)
# b = Test(3, 5)
# c = Test(1, 1)
# d = Test(11, -13)
# print(d)
# # del a
# print(a + b + c)
# print(a - b - c)
# # print(a.ar1)

# class Person:
#     def __init__(self, name, sur):
#         self.n = name
#         self.s = sur
#
# class Worker(Person):
#     def __init__(self, name, sur, bonus):
#         # Person.__init__(self, name, sur)
#         super().__init__(name, sur) # с super self не нужен
#         self.b = bonus
#
#     def __str__(self):
#         return f'Worker: name = {self.n}, surname = {self.s}, bonus = {self.b}'
#
# baker = Worker('Tom', 'Riddle', 2000)
# print(baker)

from abc import ABC, abstractmethod

class MyAbstractClass(ABC):
    @abstractmethod # Декоратор, теперь метод 1 - абстрактный метод, и мы должны его переопределить в дочернем классе
    def my_method_1(self):
        print('method 1')
    @abstractmethod
    def my_method_2(self):
        print('method 2')

class MyClass(MyAbstractClass):
    def my_method_1(self): # переопределили метод родительского класса
        print('method 1 - дочерний')
    def my_method_2(self):
        print('method 2 - крутой')


mc = MyClass()
mc.my_method_1()
mc.my_method_2()