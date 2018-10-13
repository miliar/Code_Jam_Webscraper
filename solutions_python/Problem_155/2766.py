import fileinput
def friends(max,friendList):
    standing=0
    added=0
    for n,i in enumerate(friendList):
        if(i>0):
            if(standing<n):
                added+=n-standing
                standing+=n-standing
            standing+=i

    return added



file=fileinput.input()

testcases=int(file.readline())
for i in range(testcases):
    case=file.readline()
    sMax,audience=case.split()
    sMax=int(sMax)
    audience=[int(x) for x in audience ]
    added=friends(sMax,audience)
    print('Case #{}: {}'.format(i+1, added))



