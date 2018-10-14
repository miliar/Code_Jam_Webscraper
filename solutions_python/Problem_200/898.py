def tidy_num(num):
    for k in xrange(0, len(num)-1):

        sel_num = num[len(num)-k-2:len(num)-k]
        to_change = ""


        if (int(sel_num[0]) > int(sel_num[1])):
            to_change = num[-(k+1):]
            subnum = int(num) - (int(to_change)+1)
            num = str(subnum)

    return num


f = open('tidy.in', 'r')
g = open('tidyoutput', 'w')
content = f.readlines()
numOfCases = int(content[0])
iter = 0
s = ""
for n in content:
    if iter == 0:
        pass
    else:
        m = int(n)
        n = str(m)

        print "Case #"+str(iter)+": "+ str(tidy_num(str(n)))
        s = s + "Case #"+str(iter)+": "+ str(tidy_num(str(n))) + "\n"
    iter = iter + 1
g.write(s)