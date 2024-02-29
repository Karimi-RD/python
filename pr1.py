my_list = [1, 2, 3, 2, 4, 5, 3, 6, 7, 8, 7]
elementremove = 2
i = 0

while i < len(my_list):
    if my_list[i] == elementremove:
        my_list.remove(elementremove)
    else:
        i += 1

print("لیست نهایی بعد از حذف عنصر 2:")
print(my_list)

#lajevardian
