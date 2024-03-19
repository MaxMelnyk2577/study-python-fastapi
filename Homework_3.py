                                              ### Умовні конструкції ###
password = input("Введіть пароль: ")
if 'password123' in password:
    print("Ви увійшли в систему")
else:
    print("Неправильний пароль")

#---------------------------------------------#

test_list = [1, 2, 3, 4, 5, 6, 7]
test = input()
if "1" in test and test_list:
    print("Monday")
elif "2" in test and test_list:
    print("Tuesday")
elif "3" in test and test_list:
    print("Wednesday")
elif "4" in test and test_list:
    print("Thursday")
elif "5" in test and test_list:
    print("Friday")
elif "6" in test and test_list:
    print("Saturday")
elif "7" in test and test_list:
    print("Sunday")
else:
    print("Номер дня недійсний!")

                                                     ### Цикли ###
a = int(input())
for num in range(1, 11):
    b = a * num
    print(f"{a} x {num} = {b}")

#------------------------------------------------------------#

test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
test = sum(test_list)
print(test)

#------------------------------------------------------------#

test = int(input())
f = 1
for x in range(2, test + 1):
   f *= x
print(f)

#------------------------------------------------------------#

for i in range(1, 51):
    if i % 2 == 0:
        print(i)

#------------------------------------------------------------#

for num in range(2, 51):
    is_prime = True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    else:
        print(num)
