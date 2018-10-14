def is_increasing(num):
    list1 = list(map(int, list(str(num))))
    for i in range(len(list1) - 1):
        if list1[i] > list1[i + 1]:
            return False
    return True

T = int(input())

for i in range(T):
    N = int(input())
    # digits = list(str(N))
    # print(digits)
    while not is_increasing(N):
        N -= 1
    print("Case #{0}: {1}".format(i + 1, N))
