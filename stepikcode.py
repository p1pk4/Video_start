'''
Формат входных данных
На вход программе подаётся строка-разделитель и три строки, каждая на отдельной строке.

Формат выходных данных
Программа должна вывести введённые три строки через разделитель.

separator = input()
a = input()
b = input()
c = input()
print(a, b, c, sep = separator)
'''
'''
# put your python code here
name = input()
print('Привет, ', name, end='!')
print('dd')

x = 3 
y = 4 
z = x + y # 7
z = z + 1 # 8
x = y # 4
y = 5 # 5
x = z + y + 7
8 + 5 + 7
'''

'''
Напишите программу вывода на экран трех последовательно идущих чисел, каждое на отдельной строке. 
Первое число вводит пользователь, остальные числа вычисляются в программе.

Формат входных данных
На вход программе подается одно целое число.

Формат выходных данных
Программа должна вывести три последовательно идущих числа в соответствии с условием задачи.

# put your python code here
num = int(input())
#print(num)
print(num + 1)
print(num + 2)

###################################

Напишите программу, которая считывает три целых числа и выводит на экран их сумму. 
Каждое число записано в отдельной строке.

Формат входных данных
На вход программе подаётся три целых числа, каждое на отдельной строке.

Формат выходных данных
Программа должна вывести сумму введенных чисел.
'''
# put your python code here
a, b, c = input(), input(), input()
summ = int(a) + int(b) + int(c)
print(summ)
