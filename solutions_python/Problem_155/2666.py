__author__ = 'MuSTERMIND'
import sys

#ipf = open("./input",  encoding="UTF-8")
#ipf = open("./A-small-attempt0.in",  encoding="UTF-8")
ipf = open("./A-large.in",  encoding="UTF-8")
ipls = ipf.readlines()
T = int(ipls[0])
row = 1
ret = None
for ipl in ipls[1:]:
    ii = 0
    highest = ""
    while ipl[ii] != " ":
        highest = highest + ipl[ii]
        ii += 1
    highest = int(highest)
    looper = ipl[ii+1:]
    rised = 0
    loop = 0
    add = 0
    while loop <= highest:
        while rised < loop:
            add += 1
            rised += 1
        rised += int(looper[loop])
        loop += 1
    if not ret:
        ret = "Case #"+str(row)+": "+str(add)
    else:
        ret = ret + "\n" + "Case #"+str(row)+": "+str(add)
    row += 1
#opf = open("./output", 'w', encoding="UTF-8")
#opf = open("./A-small-attempt0.out", 'w', encoding="UTF-8")
opf = open("./A-large.out", 'w' , encoding="UTF-8")
opf.write(ret)
opf.close()