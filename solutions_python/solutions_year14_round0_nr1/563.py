from collections import Counter

iname = open(raw_input("File name: "), "r")
oname = open("out.txt", "w")

dat = iname.read().splitlines()
del dat[0]
count = 1

for i in xrange(0, len(dat), 10):
    oname.write("Case #{}: ".format(count))
    count += 1
    
    r1v = dat[int(dat[i]) + i].split()
    r2v = dat[int(dat[5 + i]) + 5 + i].split()
    ans = [k for k, v in Counter(r1v + r2v).items() if v > 1]
    unique = set(r1v).union(r2v)

    if len(ans) == 1:
        oname.write(ans[0])
    elif len(unique) == 8:
        oname.write("Volunteer cheated!")
    else:
        oname.write("Bad magician!")
    oname.write("\n")
