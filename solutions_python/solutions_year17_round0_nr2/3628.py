t = int(input())  # read a line with a single integer
# print(t)
for i in range(1, t + 1):
    # print(input().split(" "))
    ans = None
    k = int(input())  # read a list of integers, 2 in this case
    for j in reversed(range(1,k+1)):
        if j < 10:
            ans = j
            break
        elif (j % 10 == 0):
            continue
        else:
            quit = 0
            num = j
            ld = num % 10
            num //= 10
            while(num):
                if(ld < num % 10):
                    q = 0
                    break
                else:
                    q = 1
                    ld = num % 10
                    num //= 10
            if(q == 0):
                continue
            else:
                ans = j
                break

    print("Case #{}: {}".format(i, ans))
