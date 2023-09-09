import sys

input = sys.stdin.readline

n = int(input())
numbers = input().split()

max1 = max2 = float('-inf')

for x in numbers:
    current_num = int(x)
    if current_num > max1:
        max2 = max1
        max1 = current_num
    elif current_num > max2:
        max2 = current_num

print(max1 * max2)