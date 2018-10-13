#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      derrickkwa
#
# Created:     12/04/2014
# Copyright:   (c) derrickkwa 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    Inputfile = open("magic trick.txt", 'rU')
    content = Inputfile.readlines()
    testcases = int(content.pop(0))
    output = []
    for count in range(1, testcases+1):
        firstanswer = int(content.pop(0))
        firstshuffle = content[0:4]
        firstshuffle[-1] = firstshuffle[-1]
        del(content[0:4])
        secondanswer = int(content.pop(0))
        secondshuffle = content[0:4]
        secondshuffle[-1] = secondshuffle[-1]
        del(content[0:4])
        firstrow = set(firstshuffle[firstanswer-1].split())
        secondrow = set(secondshuffle[secondanswer-1].split())
        chosen = list(firstrow.intersection(secondrow))
        caseoutput = "Case #" + str(count) + ": "
        if len(chosen)>1:
            caseoutput = caseoutput + "Bad magician!"
        elif len(chosen)==1:
            caseoutput = caseoutput + chosen[0]
        else:
            caseoutput = caseoutput + "Volunteer cheated!"
        output.append(caseoutput)
    for line in output:
      print(line)
if __name__ == '__main__':
    main()