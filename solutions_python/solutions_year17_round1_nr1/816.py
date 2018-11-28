from pip._vendor.distlib.compat import raw_input


def cake(s, r, c):
    i = 0
    while (i + 1) < (r -1):
        j = 0
        while j < c:
            if s[i][j] != '?' and s[ i +1][j] == '?':
                s[i + 1][j] = s[i][j]
            elif s[i][j] == '?' and s[i + 1][j] != '?':
                s[i][j] = s[i + 1][j]
            else:
                pass
            j += 1
        i += 2

    i = 0
    while i < r:
        j = 0
        while (j + 1) < (c - 1):
            if s[i][j] != '?' and s[i][ j +1] == '?':
                s[i][j + 1] = s[i][j]
            elif s[i][j] == '?' and s[i][j + 1] != '?':
                s[i][j + 1] = s[i][j + 1]
            else:
                pass
            j += 2
        i += 1

    i = 0
    while i < r:
        k = 0
        temp = [e for e in s[i] if e != '?']
        if len(temp) == 1:
            s[i] = [temp[0] for e in s[i]]
        while k < c:
            if k != 0 and s[i][k] == '?':
                s[i][k] = s[i][k-1]
            k += 1
        i+=1

    i=0
    while i < r:
        k = c-1
        while k > -1:
            if k != c-1 and s[i][k] == '?':
                s[i][k] = s[i][k+1]
            k -= 1
        if len([x for x in s[i] if x != '?']) == 0:
            s[i] = s[i-1]
        i += 1

    i = r-1
    while i > -1:
        if len([x for x in s[i] if x != '?']) == 0:
            s[i] = s[i+1]
        i -= 1
    for x in s:
        print(''.join(x))

if __name__ == "__main__":
    t = int(raw_input())
    for i in range(1, t + 1):
        r, c = [int(x) for x in raw_input().split(" ")]
        k = 0
        s = []
        while k < r:
            temp = raw_input()
            temp = [x for x in temp]
            s.append(temp)
            k += 1
        print("Case #{}:".format(i))
        cake(s, r, c)
