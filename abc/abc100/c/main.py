n = int(input())
a = list(map(int, input().split()))
ans = 0

for i in range(len(a)):
    while (a[i] % 2 == 0):
        a[i] = a[i] // 2
        ans += 1

print(ans)