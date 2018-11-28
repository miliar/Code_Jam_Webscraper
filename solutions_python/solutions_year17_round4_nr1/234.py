

T = input()

for case in range(1,T+1):
    N,P = [int(_) for _ in raw_input().split()]
    people = [int(_) for _ in raw_input().split()]

    if P == 2:
        left = sum([1 for i in people if i % 2 == 1])
        ans = N - (left/2)

    elif P == 3:
        one = sum([1 for i in people if i % 3 == 1])
        two = sum([1 for i in people if i % 3 == 2])
        if one == two:
            ans = N - one
        else:
            x = min(one,two)
            y = max(one,two) - x

            good = N - one - two + x

            if y % 3 == 0:
                ans = good + y/3

            elif y % 3 == 1:
                ans = good + y/3 + 1

            else:
                ans = good + y/3 + 1

    else:
        pass

                

    print "Case #%d: %d" % (case,ans)
