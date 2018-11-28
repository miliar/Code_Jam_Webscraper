import numpy

with open("D-small-attempt0.txt", "r") as f:
    with open("D-output.txt", "w") as out:
        cases = int(f.readline().strip())
        for case in xrange(1, cases+1):
            [x, r, c] = map(int, f.readline().split())
            if (x ==r and r == c) or (x==1) or (x==2 and (r*c)%x == 0):
                out.write("Case #%d: %s" %(case, "GABRIEL")+ "\n")
                continue
            if (x > r and x > c) or ((r*c)%x != 0):
                out.write("Case #%d: %s" %(case, "RICHARD")+ "\n")
                continue
            if r*c ==3 or r*c == 4:
                out.write("Case #%d: %s" %(case, "RICHARD")+ "\n")
                continue
            if x ==4:
                if (r==2) or (c ==2):
                    out.write("Case #%d: %s" %(case, "RICHARD")+ "\n")
                    continue
            out.write("Case #%d: %s" %(case, "GABRIEL")+ "\n")
