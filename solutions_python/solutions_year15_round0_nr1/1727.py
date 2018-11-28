with open("A-large.txt", "r") as f:
    with open("output2.txt", "w") as out:
        cases = int(f.readline().strip())
        for case in xrange(1, cases+1):
            [smax, audience] = f.readline().split()
            if int(smax) == 0:
                out.write("Case #%d: 0" % (case) + "\n")
                continue
            count = 0
            ans = 0
            for i in xrange(len(audience)):
                if (audience[i] > "0") and (count < i):
                    add =i - count
                    ans += add
                    count += (add +int(audience[i]))
                else:
                    count += int(audience[i])
            out.write("Case #%d: %s" %(case, ans)+ "\n")
