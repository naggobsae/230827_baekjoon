import sys

n = int(sys.stdin.readline())

lst = []

for i in range(n):
    xy_lst = list(map(int, sys.stdin.readline().split()))
    lst.append(xy_lst)

lst.sort(key = lambda x:(x[1], x[0]))

for i in lst:
    print("{0} {1}".format(i[0], i[1]))