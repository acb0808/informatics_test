# 소하고 정보 수행평가 🏴‍☠️💻
본 문서는 2023년 6월에 보는 정보 프로그래밍 수행평가에 도움을 드리고자 만들어진 문서입니다.

총 유형은 A형/B형으로 나뉘며 각 유형에 따라 나오는 문제가 다르므로 참고하시길 바랍니다.

풀이오류에 대한 내용은 `본교 2학년 8반 이석현`에게 제보 하시거나, 깃허브 이슈탭을 이용해주세요 😍

문서의 풀이는 파일로 저장되어있습니다.

---
## 문제 목록

링크 틀릭시 `코드업` 사이트로 연결됩니다. 
| 문제 이름 | 문제출처 | 출처상세 | 유형 |
|  :---:   | :---: | :---: | :---:|
|[출력하기(04)](https://codeup.kr/problem.php?id=6004)|부교재|12p| A형 |
|[문자 2개 입력받아 순서 바꿔 출력하기 01](https://codeup.kr/problem.php?id=6013)| 부교재 | 30p | B형 |
|[ 정수 3개 입력받아 짝수만 출력하기 ](https://codeup.kr/problem.php?id=6065)| 부교재 | 134p | A형 |
|[ 점수 입력받아 평가 출력하기 ](https://codeup.kr/problem.php?id=6068)| 부교재 | 140p | B형 |
|[ 정수 1개 입력받아 카운트다운 출력하기 01 ](https://codeup.kr/problem.php?id=6072)| 부교재 | 148p | A형 |
|[ 문자 1개 입력받아 알파벳 출력하기 ](https://codeup.kr/problem.php?id=6074)| 부교재 | 152p | A형 |
|[ 짝수 합 구하기 ](https://codeup.kr/problem.php?id=6077)| 부교재 | 158p | B형 |
|[ 3 6 9 게임의 왕이 되자 ](https://codeup.kr/problem.php?id=6082)| 부교재 | 168p | B형 |
| 정수 1개 입력받아 약수 출력하기| 수업시간 | 수업 | A와 B형 |
| 정수 1개를 입력받아 약수의 갯수 출력하기| 수업시간 | 수업 | B형 |
| 정수 2개를 입력받아 공약수 출력하기| 수업시간 | 수업 | A형 |

## 유형 A
- 출력하기(04)
- 정수 3개 입력받아 짝수만 출력하기
- 정수 1개 입력받아 카운트다운 출력하기 01
- 문자 1개 입력받아 알파벳 출력하기
- 정수 1개 입력받아 약수 출력하기
- 정수 2개를 입력받아 공약수 출력하기

## 유형 B
- 문자 2개 입력받아 순서 바꿔 출력하기 01
- 점수 입력받아 평가 출력하기
- 짝수 합 구하기
- 3 6 9 게임의 왕이 되자
- 정수 1개 입력받아 약수 출력하기
- 정수 1개를 입력받아 약수의 갯수 출력하기



---
## 풀이
`Ctrl+F`을 이용하여 문제 이름을 검색해보세요 😁😁
부교재에 있는 문제의 풀이는 [informatics](https://github.com/acb0808/informatics) `소하고 정보 부교재 정답`에 있습니다.

## 출력하기(04)
```python
print("'Hello'")
```

## 문자 2개 입력받아 순서 바꿔 출력하기 01
```python
a = input()
print(input())
print(a)
```

## 정수 3개 입력받아 짝수만 출력하기
```python
a,b,c = map(int, input().split())
if a%2==0:
    print(a)
if b%2==0:
    print(b)
if c%2==0:
    print(c)
```

## 점수 입력받아 평가 출력하기
```python
n = int(input())
if n >= 90:
    print('A')
elif n>=70:
    print('B')
elif n >= 40:
    print('C')
else:
    print('D')
```

## 정수 1개 입력받아 카운트다운 출력하기 01
```py
a=int(input())

while a!=0:
    print(a)
    a-=1
```

## 문자 1개 입력받아 알파벳 출력하기
```py
n = ord(input())
for i in range(ord('a'), n+1):
    print(chr(i))
```

## 짝수 합 구하기
```py
n = int(input())
sum = 0

for i in range(0, n+1, 2):
    sum += i
print(sum)
```

## 3 6 9 게임의 왕이 되자
```py
n = int(input())

for i in range(1, n+1) :
  if i%10==3 or i%10==6 or i%10==9 :
    print("X", end=' ')
  else :
    print(i, end=' ')
```

## 정수 1개 입력받아 약수 출력하기
```py
n = int(input())
for i in range(1, n+1):
    if n%i == 0:
        print(i)
```

## 정수 1개를 입력받아 약수의 갯수 출력하기
```py
n = int(input())
cnt = 0
for i in range(1, n+1):
    if n%i == 0:
        cnt += 1
print(cnt)
```

## 정수 2개를 입력받아 공약수 출력하기
1. 최대공약수의 약수를 출력하는 방법
2. while과 나머지를 이용한 방법
```py
a,b = map(int, input().split())
while b > 0:
    a, b = b, a % b
for i in range(1, a+1):
    if a%i == 0:
        print(i)
```
```py
a,b = map(int, input().split())
if a < b:
    a,b = b,a
i = 1
while a >= i:
    if a % i == 0 and b % i == 0:
        print(i)
    i += 1
```

# 코멘트
- 코드를 실행해 보고 잘 작성했는지 확인해보세요 😋
- 유클리드 호제법도 알아두시면 좋습니다
- A형과 B형은 당일에 바뀔 수 있습니다. 'A형만 외운다' 라는 생각은 ❌
- 최대 공약수의 유클리드 호제법은 교과서 154p에 실려있습니다.
