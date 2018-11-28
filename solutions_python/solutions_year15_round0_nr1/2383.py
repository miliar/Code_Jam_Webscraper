def solve():
    
    
    cases = raw_input()

    cses = int(cases)

    for y in range(cses):

        ds = raw_input()
        dss = ds.split()
        mx = dss[0]
        dat = dss[1]

        i = 1
        total = 0
        add = 0
        total += int(dat[0])
        dat = dat[1:]

        for c in dat:
            if i > total and int(c) is not 0:
                
                x = (i-total)
                add += (i-total)
                total += int(c) + x

            else:
                total += int(c)
            i += 1


        
        with open("out.out", "a") as myfile:
            myfile.write("Case #" + str(y+1) + ": " + str(add) + "\n")







solve()

