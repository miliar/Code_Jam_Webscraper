for i in range(int(input())):
    n = int(input().strip())
    while True:
        if list(str(n)) == sorted(str(n)):
            print("Case #{}: {}".format(i + 1, n))
            break
        else:
            n -= 1
