my_list = []
final_list = []
for _ in range(int(input())):
    name = input()
    score = float(input())
    my_list.append([name, score])

my_list.sort(key=lambda x: x[1])
z = my_list[0][1]
while my_list[0][1] == z:
    my_list.remove(my_list[0])

sec_least = my_list[0][1]
for i in range(len(my_list)):
    if my_list[i][1] == sec_least:
        final_list.append(my_list[i][0])
final_list.sort()
result = '\n'.join(final_list)
print(result)
