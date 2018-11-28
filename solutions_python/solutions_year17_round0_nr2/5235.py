

filename = "B-small-attempt3.in"
infile = open(filename, 'r')
lines = infile.readlines()

cases = []
t = int(lines[0].strip('\n'))
for i in range (1,t+1):
    cases.append(lines[i].strip('\n'))
print(cases)

infile.close()


def check(number):
    number = int(number)
    strnumber = str(number)
    numlen = len(strnumber)
    if numlen == 1:
        return number
    else:
        previous = strnumber[0]
        for digit in strnumber:
            if digit < previous:
                return check(number-1)
            previous = digit
        return number

    
outfile = open("file3.txt",'w')

caseNo = 1
for case in cases:
    outfile.write("Case #{}: {}\n".format(caseNo, str(check(case))))
    caseNo += 1

outfile.close()
