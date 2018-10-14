import sys

case = 1

for line in sys.stdin:
    parts =  [float(x) for x in line.split()]
    if len(parts) < 3:
        continue

    targetcookies=parts[2]
    initialrate=2.0
    costfactory=parts[0]
    ratefactory=parts[1]

    factories=0
    factorytime=0
    currentrate=initialrate

    while True:
        currenttime=(targetcookies-costfactory)/(currentrate)
        newrate = currentrate + ratefactory
        buildtime = targetcookies / newrate

        if currenttime <= buildtime:
            break

        factorytime = factorytime + costfactory/currentrate
        factories = factories + 1
        currentrate = newrate

    totaltime = factorytime + targetcookies/currentrate
    print ("Case #" + str(case) + ": " + str(totaltime))
    case = case + 1