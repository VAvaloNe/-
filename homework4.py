immutable_var = 1, 5, 7, 'кино', 'Мир'
print(immutable_var)
#immutable_var [2] = 100 # Нельзя изменить потому что кортеж не потдерживает оброщение по элементам
#print(immutable_var)
mutable_list = [1,5, 10, 'Море', 'Ночь']
mutable_list.append('Low')
print(mutable_list)