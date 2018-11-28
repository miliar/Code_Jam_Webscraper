inputfile = open("A-large.in", "r")
outputfile = open("Output.txt", "w")
cases = int(inputfile.readline())
trials = 1

def snapper(devices, snaps):
    #If you don't click your fingers, it will be off
    if snaps == 0: return "OFF"

    #If there are more devices than snaps of the fingers, it will be off.
    if devices > snaps: return "OFF"

    #Work out the amount of snaps required
    times = 2**devices-1

    #If we have snapped that many times, it will be on.
    if snaps == times: return "ON"
    #If we have snapped less than needed, it will be off.
    if snaps < times: return "OFF"

    if snaps > times:
        if (snaps - times)%(times+1)==0:
            return "ON"
        else:
            return "OFF"

while trials <= cases:
    DS = inputfile.readline().split()
    outputfile.write("Case #" + str(trials) + ": " + snapper(int(DS[0]), int(DS[1])) + "\n")
    trials += 1
print "DONE"
outputfile.close()