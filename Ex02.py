# Напишите однострочный генератор словаря,
# который принимает на вход три списка одинаковой
# длины: имена str, ставка int, премия str с указанием
# процентов вида “10.25%”. В результате получаем словарь
# с именем в качестве ключа и суммой премии в качестве значения.
# Сумма рассчитывается как ставка умноженная на процент премии
# Ввод:
# name_list = ['Vlad', 'Den', 'Alex']
# salary_list = [1000, 2000, 3000]
# extra_list = ['10.25%', '15%', '20%']
# Вывод:
# {'Vlad': 102.5, 'Den': 300.0, 'Alex': 600.0}

name_list = ['Vlad', 'Den', "Alex"]
salary_list = [1000, 2000, 3000]
extra_list = ['10.25%', '15%', '20%']
print(f'исходные данные:\n{name_list}\n{salary_list}\n{extra_list}')
print('Решение:')

print({name: salary * float(award[:-1]) /
       100 for name, salary, award in zip(name_list, salary_list, extra_list)})
