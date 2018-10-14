# taking the number of inputs
T = int(input())

for t in range(1, T + 1):
    s, k = input().split(" ")
    k = int(k)
    n = len(s)
    # converting s into a boolean string
    s = [i == "+" for i in s]
    # if all the elements in the list are true, then no filps needed
    if all(s) == True:
        print("Case #{}: {}".format(t, 0))
    elif k > n:
        print("Case #{}: {}".format(t, "IMPOSSIBLE"))
    else:
        i = 0
        flipcount = 0
        # if the pancakes starting from i to n are flippable
        while (i + k <= n):
            # if the pan cake is "+"
            if s[i]:
                i += 1
            # if the pan cake is "-"
            else:
                # flip all k pancakes staring from i
                # and discard all the ones correctly flipped till now
                # including ith element
                s = list(map(lambda x: not(x), s[i + 1:i + k])) + s[i + k:]
                # print(s)
                i = 0
                n = len(s)  # = n - (i + 1)
                flipcount += 1

        # if all the remaining pancakes are True
        if i + k == n or all(s):
            print("Case #{}: {}".format(t, flipcount))
        else:
            print("Case #{}: {}".format(t, "IMPOSSIBLE"))
