def closest():
    t = int(input())  # read a line with a single integer
    for j in range(1, t + 1):
        m = str(input())
        numb = []
        for n in m:
            numb.append(int(n))
        diff = []
        maxdiff = 100
        maxdiffloc = -1
        for i in range(len(numb) - 1):
            loc = numb[i + 1] - numb[i]
            diff.append(loc)
            if loc < maxdiff:
                maxdiff = diff[i]
                maxdiffloc = i
        while (maxdiff < 0):
            numb[maxdiffloc+1] += 10
            numb[maxdiffloc] -= 1
            diff[maxdiffloc] = numb[maxdiffloc+1] - numb[maxdiffloc]
            maxdiff = 100
            for i in range(len(numb) - 1):
                diff[i] = min(9, numb[i + 1]) - min(9, numb[i])
                if diff[i] < maxdiff:
                    maxdiff = diff[i]
                    maxdiffloc = i
        print("Case #{0}: {1}".format(j, int("".join([str(min(i, 9)) for i in numb]))))

if __name__ == "__main__":
    closest()
