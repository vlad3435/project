import sys
import time


def _max(arr):
    mx = (-1) * sys.maxsize
    for nm in range(len(arr)):
        if arr[nm] > mx:
            mx = arr[nm]
    return mx


def _min(arr):
    mn = sys.maxsize
    for nm in range(len(arr)):
        if arr[nm] < mn:
            mn = arr[nm]
    return mn


def _sum(arr):
    sm = 0
    for nm in range(len(arr)):
        sm += arr[nm]
    return sm


def _mult(arr):
    ml = 1
    for nm in range(len(arr)):
        ml = ml * a[nm]
        if ml == 0:
            break
    return ml

start = time.time()
f = open("тесты/тесты sum_mult/a.txt", 'r')
s = f.read().split()
if 0 < len(s) <= 1000000:
    a = []
    for i in range(len(s)):
        if s[i].isdigit():
            a.append(int(s[i]))
        else:
            a.append(0)
            print(f'На позиции {i + 1} найдена буква, замена на 0')

    print(_min(a), _max(a), _sum(a), _mult(a))
else:
    print("Данные некорректны")

print("%s секунд" % (time.time() - start))
