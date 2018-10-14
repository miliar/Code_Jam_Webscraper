def main():
    txtin = open("input.txt", "r")
    txtout = open("output.txt", "w")
    cases = int(txtin.readline())
    writelines = []
    for case in range(1, cases+1):
        l = txtin.readline().split()
        n = int(l[0])
        m = int(l[1])
        numbs = set()
        rows = []
        for i in range(n):
            l = txtin.readline().split()
            l = map(int, l)
            rows.append(l)
        columns = []
        for i in range(m):
            l = []
            for j in range(n):
                numb = int(rows[j][i])
                numbs.add(numb)
                l.append(numb)
            columns.append(l)
        numbs = sorted([i for i in numbs], reverse=True)[1:]
        ans = ""
        for k in numbs:
            ind = []
            for i in range(n):
                for j in range(m):
                    if rows[i][j] == k:
                        ind.append([i, j])
            for i in ind:
                fl1 = True
                for j in rows[i[0]]:
                    if k < j:
                        fl1 = False
                fl2 = True
                for j in columns[i[1]]:
                    if k < j:
                        fl2 = False
                if not fl1 and not fl2:
                    ans = "NO"
                    break
        if ans != "NO":
            ans = "YES"
        #####   res = res + '\n'
        res = "Case #" + str(case) + ": " + ans + '\n'
        writelines.append(res)
    txtout.writelines(writelines)
    txtout.close()

if __name__ == '__main__':
    main()
