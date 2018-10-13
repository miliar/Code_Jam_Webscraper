#-------------------------------------------------------------------------------
# Name:        模块1
# Purpose:
#
# Author:      user
#
# Created:     12/04/2014
# Copyright:   (c) user 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------


if __name__ == '__main__':
    f = open('./input')
    output = open('./output','w')
    context = f.readlines()
    caseNum = int(context[0])
    i = 0
    while caseNum > i:
        fRow = int(context[i*10+1])
        sRow = int(context[i*10+6])
        fData = context[i*10+1+fRow].replace('\n','').split(' ')
        sData = context[i*10+6+sRow].replace('\n','').split(' ')
        if len(list(set(fData)&set(sData))) == 1:
             output.write('Case #'+str(i+1)+': ' +str(list(set(fData)&set(sData))[0])+'\n')
        elif len(list(set(fData)&set(sData))) == 0:
             output.write('Case #'+str(i+1)+': Volunteer cheated!\n')
        else:
             output.write('Case #'+str(i+1)+': Bad magician!\n')
        i += 1
    f.close()
    output.close()
