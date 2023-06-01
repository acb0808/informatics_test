a,b = map(int, input().split())
while b > 0:
    a, b = b, a % b
for i in range(1, a+1):
    if a%i == 0:
        print(i)