
FILE = open("A-large.in","r")
OUTPUT = open("A-large.out","w")

cases = FILE.readline()

for i in range(0,int(cases)):
    temp = FILE.readline().split(" ")
    snapperCount = int(temp[0])
    timesSnapped = int(temp[1])
    modValue = 1
    for j in range(0,snapperCount):
        modValue = modValue*2
    timesSnapped = timesSnapped % modValue
    lightState = "OFF"
    if timesSnapped == modValue - 1:
        lightState = "ON"
    OUTPUT.write('Case #' + str(i + 1) + ': ' + lightState + '\n')
        
FILE.close()
OUTPUT.close()

