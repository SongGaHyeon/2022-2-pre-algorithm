import sys
input = sys.stdin.readline

size = int(input())
nd = [list(map(int, input().split()))for _ in range(size)]

a, b, c = 0, 0, 0
# a=0
# b=0
# c=0


def divi(row, col, size):
    # 9개로 나누기 부분 포함 부분
    global a, b, c
    initnode = nd[row][col]
    # 비교하기 위한 것
    for i in range(row, row+size):
        for j in range(col, col+size):
            if initnode != nd[i][j]:
                # 모두 같을때
                # 분활정복 부분
                div = size//3
                # 그냥 divi(nd, row+i*3..........)이런식으로 했다가 안됨,
                # 값이 변하기 때문에 (크기 따라) 아래와 같이 적어줘야함
                for k in range(3):
                    for l in range(3):
                        divi(row+k*div, col+l*div, div)
                return

    if initnode == 0:
        b += 1
    elif initnode == -1:
        a += 1
    elif initnode == 1:
        c += 1


divi(0, 0, size)
print(a)
print(b)
print(c)
