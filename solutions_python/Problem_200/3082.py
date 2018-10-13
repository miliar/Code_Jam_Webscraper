def main():
    ans = []
    with open("B-large.in", "r") as r:
        count = int(r.readline()[:-1])
        for i in range(count):
            l = r.readline()[:-1]
            number = int(l)
            lnumber = list(reversed([int(a) for a in l]))
            maxnum = number
            j = 0
            while j < len(lnumber) - 1:
                if lnumber[j] < lnumber[j + 1]:
                    print(lnumber[j], lnumber[j + 1])
                    lnumber[j +1 ] -= 1
                    k = 0
                    while k <= j:
                        lnumber[k] = 9
                        k += 1  
                print(lnumber,j)
                j += 1
            ans.append(int("".join(reversed([str(item) for item in lnumber]))))
    with open("test.out", "w") as w:
        for i, a in enumerate(ans):
            if a >= 0:
                w.write("Case #{0}: {1}\n".format(i+1, a))
            else:
                w.write("Case #{0}: IMPOSSIBLE\n".format(i+1))

if __name__ == '__main__':
    main()