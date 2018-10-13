import re

f = open('A-large.in')
lines = f.readlines()
cases = []
count = 0
for line in lines:
    if count == 0 or line.strip() == "":
        count = count + 1
        cases.append("")
    else:
        cases[len(cases)-1] = cases[len(cases)-1] + line.strip()
f.close()


f = open('outputLARGE.txt', 'w')
count = 1
str1 = ""
for case in cases:
    if case.strip() == "":
        continue
    p1 = re.compile('[\.]+')
    p2 = re.compile('(.{4}){0,3}[TX]{4}.*')
    p3 = re.compile('(.{4}){0,3}[TO]{4}.*')
    p4 = re.compile('([TX][TXO\.]{4}){3}[TX]')
    p42 = re.compile('.*([TX][TXO\.]{3}){3}[TX].*')
    print p42.match(case)
    p5 = re.compile('([TO][TXO\.]{4}){3}[TO]')
    p52 = re.compile('.*([TO][TXO\.]{3}){3}[TO].*')
    p6 = re.compile('[TXO\.]{3}([TX][TXO\.]{2}){3}[TX]')
    p7 = re.compile('[TXO\.]{3}([TO][TXO\.]{2}){3}[TO]')
    if p2.match(case) or p4.match(case) or p42.match(case) or p6.match(case):
        str1 = str1 + "Case #" + str(count) + ": X won\n"
    elif p3.match(case) or p5.match(case) or p52.match(case) or p7.match(case):
        str1 = str1 + "Case #" + str(count) + ": O won\n"
    elif case.find('.')!=-1:
        str1 = str1 + "Case #" + str(count) + ": Game has not completed\n"
    else:
        str1 = str1 + "Case #" + str(count) + ": Draw\n"
    print case
    
    count += 1
f.write(str1.strip())
f.close()
