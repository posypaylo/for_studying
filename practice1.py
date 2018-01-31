my_dict = {'one': 'asd', 'two': 'qwe', 3: 'zxc'}


dict_a = {a: b for a, b in my_dict.items()}
print(dict_a)
ts = [(1, 2), (3, 4), (5, 6)]
print(dict(ts))
gen = ((i, i+1) for i in range(1, 6, 2))

print(dict(gen))