#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Demo-User
#
# Created:     14/04/2013
# Copyright:   (c) Demo-User 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------
allPal={}
def main():

    file=open('C-small-attempt0.in')
    lines=file.readlines()
    file.close()
    inp=int(lines.pop(0))

    file=open('3.out','w+')
    for y in range(inp):
        down,up=lines[y].split()
        down=int(down)
        up=int(up)
        c=0
        for x in range(down,up+1):
            sn=x**0.5

            if sn==int(sn):
                if(isPal(str(x)) and isPal(str(int(sn)))):
                    c+=1

        print('Case #'+str(y+1)+':',c,file=file)
    file.close()

def isPal(inp):
    if inp in allPal:
        return allPal[inp]
    elif(inp==inp[::-1]):
        allPal[inp]=True
        return True
    else:
        allPal[inp]=False
        return False






if __name__ == '__main__':
    main()
