word = input("Введіть слово де дві і більше однакові літери: ")
count = 0
maximum = 0
for i in range(1, len(word)):
    if (word[i] == word[i - 1]): count += 1
    else: count  = 1
    if count > maximum: maximum = count

print(f"найбільша кількість однакових символів, розташованих підряд: {maximum}")