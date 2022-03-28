import sys
input = sys.stdin.readline

N = int(input())
xy = []

for _ in range(N):
    xy.append(list(map(int, input().split())))

xy.sort(key=lambda x: (x[0], x[1]))

for i in xy:
    print(i[0], i[1])
