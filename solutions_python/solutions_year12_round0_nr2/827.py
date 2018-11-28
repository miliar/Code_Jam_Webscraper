from sys import stdin, stdout

def solve(s, p, totals):
    count = 0

    for total in totals:
        subs = False
        for i in range(11):
            good = False
            for diff in [-2, -1, 0, 1, 2]:
                j = i + diff
                k = total - (i + j)
                if k >= 0 and k <= 10 and j >= 0 and abs(k-j) <= 2 and abs(k-i) <=2:
                    #print(i, j, k, total)
                    if k >= p or i >= p or j >= p:
                        if diff == -2 or diff == 2 or abs(k-i) == 2 or abs(k-j) ==2:
                            subs = True
                        else:
                            good = True
                            subs = False
                            break
            if good:
                count += 1
                break
        if subs and s > 0:
            s -= 1
            count += 1
    return count

line_count = int(stdin.readline())
for i in range(line_count):
    parts = [int(x) for x in stdin.readline()[:-1].split()]
    result = solve(parts[1], parts[2], parts[3:])
    print("Case #"+str(i+1)+": "+str(result));
