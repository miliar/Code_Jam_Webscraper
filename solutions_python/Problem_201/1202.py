from math import log2
test_count = int(input())
for test_num in range(1, test_count + 1):
    n, k = map(int, input().split())
    a = 2 ** (int(log2(k)))
    b = (n - k) // a
    ans1 = (b + 1) // 2
    ans2 = b // 2
    print("Case #" + str(test_num) + ":", ans1, ans2)
