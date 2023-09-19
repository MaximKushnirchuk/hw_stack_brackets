
'''Домашнее задание к лекции 7. «Подготовка к собеседованию»

1 Нужно реализовать класс Stack со следующими методами:
is_empty — проверка стека на пустоту. Метод возвращает True или False;
push — добавляет новый элемент на вершину стека. Метод ничего не возвращает;
pop — удаляет верхний элемент стека. Стек изменяется. Метод возвращает верхний элемент стека;
peek — возвращает верхний элемент стека, но не удаляет его. Стек не меняется;
size — возвращает количество элементов в стеке.'''



class Stack :
    
    def __init__(self) -> None:
        self.stak_list = list()
        
    def is_empty(self) -> bool :
        '''проверка стека на пустоту. Метод возвращает True или False'''
        return bool(self.stak_list)

    def push(self, new_elem : str) -> None :
        '''добавляет новый элемент на вершину стека. Метод ничего не возвращает'''
        self.stak_list.append(new_elem)


    def pop(self) -> str :
        '''удаляет верхний элемент стека. Стек изменяется. Метод возвращает верхний элемент стека'''
        return self.stak_list.pop()
            


    def peek(self) -> str :
        '''возвращает верхний элемент стека, но не удаляет его. Стек не меняется'''
        return self.stak_list[-1]
    
    def size(self) -> int :
        '''возвращает количество элементов в стеке'''
        return len(self.stak_list)


''' 2 Используя стек из задания 1, решите задачу на проверку сбалансированности скобок. Сбалансированность скобок означает, что каждый открывающий символ имеет соответствующий ему закрывающий, и пары скобок правильно вложены друг в друга.'''

def check_brakets(bracket_string : str) -> None :
    '''функция check_brakets принимает на вход тсроку состоящую только из скобок, создает экземпляр класса Stack, проверяет строку на сбалансированность. Результат проверке выводится через функцию print'''
    if not isinstance(bracket_string, str) :
        print('ERROR В функцию должен передаваться объект класса str !!!')
        return 
    stack_ =  Stack()
    if len(bracket_string) % 2 == 0 :
        for bracket in bracket_string :
            if bracket == '(' or bracket == '[' or bracket == '{' :
                stack_.push(bracket)    
            else :
                if stack_.size() == 0 : 
                    print('ERROR stack_.size() : Не сбалансированная последовательность!!!')
                    break
                if bracket == ')' :
                    if stack_.peek() == '(' : stack_.pop()
                    else : 
                        print('ERROR Brakets () : Не сбалансированная последовательность!!!')
                        break 
                
                elif bracket == ']' :
                    if stack_.peek() == '[' : stack_.pop()
                    else : 
                        print('ERROR Brakets []: Не сбалансированная последовательность!!!')
                        break
                
                elif bracket == '}' :
                    if stack_.peek() == '{' : stack_.pop()
                    else : 
                        print('ERROR Brakets {}: Не сбалансированная последовательность!!!')
                        break
            
        else :
            if  stack_.is_empty() : print('ERROR stack_.is_empty : Не сбалансированная последовательность!!!')
            else : print('Сбалансированная последовательность!')
            
    else: print('ERROR Len : Не сбалансированная последовательность!!!')


string = '((((((([])))[{}[]]))))'

check_brakets(string)