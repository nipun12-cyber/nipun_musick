def div(n):
    for i in range(1, 21):
        if n % i != 0:
            return False
    return True

num = 20
while True:
    if div(num):
        print(num)
        break
    num = num + 20