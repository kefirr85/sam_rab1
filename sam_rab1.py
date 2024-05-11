def print_params(a=10, b='Kef', c=True):
    print(a, b, c, )


print_params()
print_params(a=39)
print_params(c=[15, 20, 30, 40])

values_list = ['Alex', False, [56, 72, 40]]
values_dict = {'a': 25, 'b': 'KefiRR', 'c': False}
print_params(*values_list)
print_params(**values_dict)

values_list_2 = ['age', 50]
print_params(*values_list_2, 42)
