#Напишите рекурсивную функцию для возведения числа a в
# степень b. Разрешается использовать только операцию умножения. 
#Циклы использовать нельзя
#Примеры/Тесты:
#<function_name>(2,0) -> 1
#<function_name>(2,1) -> 2
#<function_name>(2,3) -> 8
#<function_name>(2,4) -> 16

def power(numb, deg):
    if (deg == 1):
        return (numb)
    if (deg != 1):
        return (numb * power(numb, deg - 1))
numb = int(input("Введите число: "))
deg = int(input("Введите степень: "))
print("Результаn равен:", power(numb, deg))