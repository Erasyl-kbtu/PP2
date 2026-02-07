a, b, c = map(int, input().split())
arr = list(map(int, input().split()))

l0 = b - 1
r0 = c - 1

arr[l0:r0+1] = arr[l0:r0+1][::-1]

for num in arr:
    print(num, end=' ')