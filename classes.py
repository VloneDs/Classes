class Create_tree:
    '''Создает елочку'''
    def __init__(self, ) :
        '''Сюда сохраняется ввод пользователя '''
        self.height = " "
        self.pin = " "

    def tree(self):
        '''Создается елочка по параметрам пользователя'''
        for pyramid in range(self.height ):
           print(' ' * (self.height - pyramid), self.pin * (2 * pyramid + 1))

answer = Create_tree()

answer.height = int(input('Введите высоту пирамиды: '))
answer.pin = input('Введите значок пирамиды: ')

answer.tree()
