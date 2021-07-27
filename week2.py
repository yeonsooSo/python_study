class Shape:
    def __init__(self, a):
        self.a = a

    def area(self):  # 넓이를 계산하는 함수
        area = self.a**2
        return 0  # 반환 값 0


class Square(Shape):
    def __init__(self, length):
        Shape.__init__(self, length)
        self.length = length

    def area(self):
        area = self.length**2
        return area  # 계산한 넓이를 반환


length = int(input("정사각형의 한 변의 길이를 입력하세요: "))
ans = Square(length)
print(f"정사각형의 면적: {ans.area()}")
