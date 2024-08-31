str = input("Введіть довільне речення: ")
str = str.split()
first_word = str[0]
str[0] = str[len(str) - 1]
str[len(str) - 1] = first_word
print(f"Нове речення: {' '.join(str)}")
