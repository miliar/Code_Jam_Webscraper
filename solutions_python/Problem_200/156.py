n = int(input())

for case in range(1, n + 1):
    s = input()
    sinv = s[::-1]
    # print(nums)
    sfinal = []
    borrowflag = False
    for i in range(0, len(s)):
        # print(sfinal)
        digit = int(sinv[i])
        if i is 0:
            if digit is not 0:
                sfinal.append(digit)
                dmin = digit
            else:
                borrowflag = True
                sfinal.append(9)
                dmin = 9
            continue
        if borrowflag is True:
            if digit is not 0:
                digit -= 1
                borrowflag = False
            else:
                digit = 9
        if digit <= dmin and digit is not 0:
            dmin = digit
            sfinal.append(digit)
        else:
            for j in range(0, len(sfinal)):
                sfinal[j] = 9
            if digit is not 0:
                sfinal.append(digit-1)
                dmin = digit - 1
            else:
                sfinal.append(9)
                dmin = 9
                borrowflag = True
    # print(sfinal)
    if sfinal[len(sfinal) - 1] is 0 or borrowflag is True:
        del sfinal[len(sfinal) - 1]
    output = "".join([str(i) for i in sfinal[::-1]])



    print("Case #{}: {}".format(case, output))

