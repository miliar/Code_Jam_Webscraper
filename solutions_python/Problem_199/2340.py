t = int(input())

for i in range(1, t + 1):
    s, k = [m for m in input().split(" ")]
    k = int(k)    

    if '-' not in s:
        print("Case #{}: {}".format(i, 0))

    elif k == len(s) and '+' in s:
        print("Case #{}: {}".format(i, 'IMPOSSIBLE'))

    elif k == 1:
        count = 0
        for m in range(len(s)):
            if s[m] == '-':
                count += 1
        print("Case #{}: {}".format(i, count))

    else:
        count = 0
        sl = []
        for j in range(len(s)):
            sl.append(s[j])

        cont = True
        while '-' in sl:

            if sl.index('-') + k > len(sl):
                count = 'IMPOSSIBLE'
                break
                
            start = sl.index('-')
            for x in range(start, start+k):
                if sl[x] == '-':
                    sl[x] = '+'
                else:
                    sl[x] = '-'
            count += 1
                
        print("Case #{}: {}".format(i, count))
