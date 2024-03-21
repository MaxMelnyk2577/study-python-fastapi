                                                ### Списки ###
a = [1, 2, 3, 4, 5]
b = a.append(10), a.append(20)
print(a)
c = a.remove(10)
print(a)

#--------------------------------------------------------------#

test_a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
test_b = sum(test_a)
print(test_b)

#--------------------------------------------------------------#

my_a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
my_b = [num * 2 for num in my_a]
print(my_b)

                                              ### Кортежі ###
test = ("яблуко", "банан", "апельсин")
print(test[0], test[1], test[2])

#--------------------------------------------------------------#

my_test = (1, 2, 3)
your_test = (4, 5, 6)
our_test = my_test + your_test
print(our_test)

                                                ### Словники ###
my_class = {'Name': 'Lionel Messi', 'Age': '36', 'Sport': 'football'}
print(my_class)

#----------------------------------------------------------------------------#

my_book = {'Назва книги': 'Rich Dad Poor Dad', 'Рік видання': 1997}
print(my_book)
new_book = {'Назва книги': 'Thinking, Fast and Slow)', 'Рік видання': 2011}
my_book.update(new_book)
print(my_book)

#----------------------------------------------------------------------------#

country = {'Україна': 'Київ', 'Польща': 'Варшава', 'Франція': 'Париж', 'Англія': 'Лондон', 'Японія': 'Токіо'}
user_country = input("Введи назву країни: ")

if user_country in country:
    print(country[user_country])
else:
    print("Помилка! Такої країни не знайдено!")
