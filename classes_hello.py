# class Solution:
#     '''Приветствие человек'''
#     def __init__(self):  #, name, surname, age
#         '''свойсвта по умолчанию'''
#         self.name = 'Ivan' 
#         self.surname =  'Ivanov' 
#         self.age =  14 
    

#     '''Пока что не понял как реализовать'''
#     def hello(self, name, surname, age):
#             '''Берет аргументы и вставляет в строчку'''
#             print(f"Hello {name} {surname} {age} years old")





# people = Solution()
# people.hello('Dima', 'Petrov', 20)         #Hello Dima Petrov 20 years old
# people.hello('Dima', 'Petrov')             #Hello Dima Petrov 14 years old
# people.hello('Dima')                       #Hello Dima Ivanov 14 years old
# people.hello()                             #Hello Ivan Ivanov 14 years old



















class Solution:

    # def __init__(self):  #, name, surname, age
    #     self.name = 'Ivan' 
    #     self.surname = 'Ivanov' 
    #     self.age = 14 



    def hello(self, name = "Ivan" , surname = 'Ivanov', age = 14):#, name , surname, age
        print(f"Hello {name} {surname} {age} years old")




people = Solution()
people.hello('Dima', 'Petrov', 20)         #Hello Dima Petrov 20 years old
people.hello('Dima', 'Petrov')             #Hello Dima Petrov 14 years old
people.hello('Dima')                       #Hello Dima Ivanov 14 years old
people.hello()                             #Hello Ivan Ivanov 14 years old