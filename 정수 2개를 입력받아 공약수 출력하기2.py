a,b = map(int, input().split())
if a < b:
    a,b = b,a
i = 1
while a >= i:
    if a % i == 0 and b % i == 0:
        print(i)
    i += 1