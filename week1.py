from random import *

a = randint(1, 6)
b = randint(1, 6)

print("주사위 던지기")
print(f"주사위 1: {a}")
print(f"주사위 2: {b}\n")

print("실행할 연산의 종류를 입력하세요.")
print("1. 덧셈  2. 뺄셈  3. 곱셈  4. 나눗셈  5. 나머지 구하기")
option = input("연산 종류: ")

if(option == "1"):
    ans = a + b
    print(f"덧셈 결과 : {ans}")
elif(option == "2"):
    ans = a - b
    print(f"뺄셈 결과 : {ans}")
elif(option == "3"):
    ans = a * b
    print(f"곱셈 결과 : {ans}")
elif(option == "4"):
    ans = a / b
    print(f"나눗셈 결과 : {ans}")
elif(option == "5"):
    ans = a % b
    print(f"나머지 구하기 결과 : {ans}")

print("\n별찍기")
for i in range(ans):
    print("*"*(i+1))
