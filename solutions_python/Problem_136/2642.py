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
    Inputfile = open("B-large.in", 'rU')
    content = Inputfile.readlines()
    testcases = int(content.pop(0))
    output = []
    for count in range(1, testcases+1):
        line = content.pop(0)
        line = line.split()
        farmmin = float(line[0])
        farmextra = float(line[1])
        target = float(line[2])
        cookies = 0
        currentrate = 2
        totaltime = 0
        caseoutput= "Case #" + str(count) + ": "
        while cookies < target:
            timetotarget = target / currentrate
            timewithfarm = farmmin / currentrate + target/(currentrate + farmextra)
            if timetotarget < timewithfarm:
                cookies = target
                totaltime = totaltime + timetotarget
            else:
                cookies = 0
                totaltime= totaltime + farmmin/currentrate
                currentrate = currentrate + farmextra

        caseoutput = caseoutput + str(totaltime)
        output.append(caseoutput)

    text_file = open("cookieOutput.txt", "w")
    for line in output:
        text_file.write(line+"\n")
    text_file.close()
if __name__ == '__main__':
    main()