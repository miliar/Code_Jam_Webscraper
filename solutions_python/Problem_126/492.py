#-------------------------------------------------------------------------------
# Name:        Consonants
# Purpose:
#
# Author:      udonko
#
# Created:     12/05/2013
# Copyright:   (c) udonko 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import sys

def counttext(text):
    count =0
    maxvalue = 0
    for chara in text:
        if chara == 'a' or chara =='i' or chara == 'o' or chara=='e' or chara == 'u':

            maxvalue=max(maxvalue,count)
            count=0
        else:
            count += 1
    maxvalue=max(maxvalue,count)
    return maxvalue
def resolve(name, n):
    count = 0
    lenname= len(name)
    for start in range(0,lenname-n+1):
        for end in range(start+n,lenname+1):
            substr = name[start:end]
            #sys.stdout.write('sub='+substr+'\n')
            value = counttext(substr)
            if value >= n:
                count += 1
    return count


def main():
    infile = open(sys.argv[1],"r")
    outfile = open(sys.argv[2],"w")
    temp = infile.readline()
    t= int(temp)
    for loop in range(t):

        sys.stdout.write(str(loop)+'\n')

        temp = infile.readline()
        temps = temp.split()

        result = resolve(temps[0], int(temps[1]))

        text = "Case #%(no)d: %(result)d\n" % {"no":loop+1, "result":result}
        outfile.write(text)
        sys.stdout.write(text)

if __name__ == '__main__':
    main()
