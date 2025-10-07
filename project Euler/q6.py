sum = 0
sum_num = 0

for i in range(1, 101):
    sum += i * i
    sum_num += i

print(sum_num * sum_num - sum)