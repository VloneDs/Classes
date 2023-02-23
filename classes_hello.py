class Solution:
    '''Приветствие с человеком'''
    def hello(self, name = "Ivan" , surname = 'Ivanov', age = 14):#, name , surname, age
        '''
            Есть уже встроенные нахвания, которые будут заменять пропущенные аргументы
        '''
        print(f"Hello {name} {surname} {age} years old")


people = Solution()

people.hello('Dima', 'Petrov', 20)         #Hello Dima Petrov 20 years old
people.hello('Dima', 'Petrov')             #Hello Dima Petrov 14 years old
people.hello('Dima')                       #Hello Dima Ivanov 14 years old
people.hello()                             #Hello Ivan Ivanov 14 years old
