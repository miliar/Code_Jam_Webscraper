infile=open('B-large.in','r')
lines=infile.readlines()
infile.close()
outfile=open('ans2.txt','w')
test=int(lines[0])
for i in range(test):
    text = "Case #" + str(i+1) + ": "
    cases = lines[1+i]
    timer1 = 0
    timer2 = 0
    starter = 2
    case = cases.strip().split(" ")
    goal = float(case[2])
    cost = float(case[0])
    gain = float(case[1])
    foo = 1/starter
    timer1 = goal/starter
    timer2 = cost/starter + goal/(starter+gain)
    while timer2 < timer1:
        starter += gain
        foo += 1/starter
        timer1 = timer2
        timer2 = goal/(starter+gain)+ (cost*foo)
    outfile.write(text)
    outfile.write('{0:.7f}'.format(timer1))
    outfile.write("\n")
outfile.close()

print("done")
