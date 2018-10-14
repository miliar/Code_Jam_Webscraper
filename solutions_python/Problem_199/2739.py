f = open("A-large.in", "r")
ans = open("ans_a_large.txt", "w")
data = f.readlines()
t = int(data[0])
for i in range(t):
    a, k =data[i+1].split()
    a = list(a)
    k = int(k)
    d = {
            "+": "-",
            "-": "+"
    }
    not_possible = False
    count = 0
    if a.count("-") == 0:
        print "Case #{}: {}" .format(i+1, count)
        ans.write("Case #{}: {}" .format(i+1, count) + "\n")

    else:
        while a.count("-") > 0:
            if a.index("-")+ k > len(a) and a.count("-") >= 1:
                not_possible = True
                break
            s = a.index("-")
            if s == 0:
                a = map(lambda x: d[x], a[s:s+k]) + a[s+k:]
            else:
                a = a[:s] + map(lambda x: d[x], a[s:s+k]) + a[s+k:]
            count += 1


        if not_possible == True:
            print "Case #{}: IMPOSSIBLE" .format(i+1)
            ans.write("Case #{}: IMPOSSIBLE" .format(i+1)+"\n")
        else:
            print "Case #{}: {}" .format(i+1, count)
            ans.write("Case #{}: {}" .format(i+1, count)+"\n")