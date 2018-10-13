import sys

filename = sys.argv[1]
outfilename = sys.argv[2]
inputfile = file(filename, 'rb')
outputfile = file(outfilename, 'wb')

lines = inputfile.readlines()
testcases = int(lines[0].strip())
count = 0
while count < testcases:
    linedata = lines[count+1].strip().split(' ')

    cookiefarmcost = float(linedata[0])
    cookiefarmbonus = float(linedata[1])
    wincondition = float(linedata[2])

#    print cookiefarmcost, cookiefarmbonus, wincondition
    cookies = 0.0
    cookiespersecond = 2
    seconds = 0.0
    while cookies < wincondition:       
        cookietimeleft = wincondition / cookiespersecond
#        print "left: ", wincondition, cookiespersecond, cookietimeleft
        cookiefarmvalue = wincondition / (cookiespersecond + cookiefarmbonus)
        cookiefarmtime = cookiefarmcost / cookiespersecond
#        print cookietimeleft, cookiefarmvalue, cookiefarmtime

        if (cookiefarmvalue + cookiefarmtime) <= cookietimeleft:
            seconds += cookiefarmtime
            cookiespersecond += cookiefarmbonus
            cookies -= cookiefarmcost
        else:
            seconds += cookietimeleft
            cookies += cookietimeleft * cookiespersecond
            break
#        print "seconds", seconds

#    print cookiespersecond
    outputfile.write("Case #%i: %.7f\r\n" % ((count+1), seconds))
    
    count += 1

inputfile.close()
outputfile.close()
