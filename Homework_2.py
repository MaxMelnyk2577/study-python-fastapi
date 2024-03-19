string_variable = "Hello, World!"
integer_variable = 42
float_variable = 3.14
bool_variable = True
list_variable = [1, 2, 3, 4, 5]
dict_variable = {"name": "John", "age": 30}
tuple_variable = (1, 2, 3, 4, 5)
none_variable = None

num1 = 10
num2 = 5
print(num1 > num2)
str1 = "apple"
str2 = "banana"
print(str1 < str2)
bool1 = True
bool2 = False
print(bool1 == bool2)
list1 = [1, 2, 3]
list2 = [4, 5, 6]
print(len(list1) == len(list2))
dict1 = {'a': 1, 'b': 2}
dict2 = {'a': 1, 'b': 3}
print(dict1 == dict2)
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
print(tuple1 < tuple2)

# Робота з рядками
num_str = str(125)
print(num_str)

message = 'Hi, my name is Python!'
message = message.replace('y', '0').replace('i', '1')
print(message)

split_test = 'This is a split test'
split_test = split_test.split()
print(split_test)
string_join = " ".join(split_test)
print(string_join)

string_join = len(string_join)
print(string_join)

# Робота зі списками
list_append = [1, 2, 3]
list_append.append(4)
list_append.append(5)
print(list_append)
print(len(list_append))

list_extend = [4, 5, 6]
list_append = list_extend.extend([7, 8, 9])
print(list_extend)
print(list_extend.index(6))

# Робота зі словниками
dict_test = {'car': 'Toyota', 'price': 4900, 'where': 'EU'}
print(dict_test['car'])
print(dict_test['where'])
print(dict_test.keys())
print(dict_test.values())
print(dict_test.items())