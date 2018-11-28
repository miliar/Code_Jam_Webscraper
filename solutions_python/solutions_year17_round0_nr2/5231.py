i = open("B-small-attempt0.in")
o = open("out.txt", "w")

cases = i.readline()
cases = int(cases)



for x in range(1, cases+1):
    range_of_num = int(i.readline())
    tidy = False
    tidynum = 0
    for num in range(1,range_of_num+1):
        if num < 10:
            tidy = True
            tidynum = num
        elif num // 10 == 0:
            tidy = False
        else:
            for digit in range(len(str(num))-1):
                if str(num)[digit] > str(num)[digit+1]:
                    tidy = False
                    break
                else:
                    tidy = True
            if tidy == True:
                tidynum = num
        #print(tidynum)

    o.write("Case #%s: %s\n" % (x, tidynum))

o.close()
i.close()

