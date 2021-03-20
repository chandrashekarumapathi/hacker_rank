my_list = []
n = int(input('Enter numbers: '))
arr = list(map(int, input('Enter the number to split: ').split()))
z = max(arr)
while max(arr) == z:
    arr.remove(max(arr))

print(max(arr))

"""
for i in arr:
    my_list.append(i)
my_list = list(dict.fromkeys(my_list))
my_list.sort()
print(my_list[-2])
"""

