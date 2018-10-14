n = int(input())
for i in range(1, n + 1):
    s = list(input())
    swp = 0
    if len(s) <= 1:
        print("Case #%d: %s" % (i, "".join(s)))
        continue
    ptr = len(s) - 1
    while ptr > 0:
        # print("   ", "".join("[%s]" % s[ii] if ii == ptr else s[ii] for ii in range(len(s))))
        if s[ptr-1] <= s[ptr] and not swp:
            ptr -= 1
        else:
            swp = 1
            if ptr > 1 and int(s[ptr-1]) - 1 < int(s[ptr - 2]):
                ptr -= 1
            else:
                # print("swap here!")
                break
    else:
        if not swp:
            print("Case #%d: %s" % (i, "".join(s)))
            continue
    # print("swaping...", ptr, swp)
    # print("".join("[%s]" % s[ii] if ii == ptr else s[ii] for ii in range(len(s))))

    if ptr > 0:
        s[ptr - 1] = str(int(s[ptr - 1]) - 1)
    s[ptr:len(s)] = ['9'] * (len(s) - ptr)
    if s[0] == "0":
        s = s[1:]
    print("Case #%d:" % i, "".join(s))
