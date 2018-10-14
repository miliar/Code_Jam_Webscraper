#Luke Miles
#2015-04-11
#google code jam round 1

def howmanyinvites(guests):
    numinvited,numstanding = 0,0
    for shyness,numpeople in enumerate(guests):
        if numstanding >= shyness:
            numstanding += numpeople
        else:
            numinvited += shyness-numstanding
            numstanding += shyness-numstanding
            numstanding += numpeople
    return numinvited

with open("/home/jane/codejam/data.txt", 'r') as fille:
    fille.next()
    cases = [[int(char) for char in line.split()[1]] for line in fille]

with open("/home/jane/codejam/out.txt",'w') as fille:
    for casenum, case in enumerate(cases):
        fille.write("Case #"+str(casenum+1)+": "
                    +str(howmanyinvites(case))+"\n")
