


def calculate(lineString):
    splitted = lineString.split(' ');
    count = int(splitted[0])
    surpriseCount = int(splitted[1])
    schwellwert   = int(splitted[2])
    minOhneSurprise = max(0, schwellwert + (2*(schwellwert-1)))
    print("min schwellwert ohne surprise %i" %minOhneSurprise)
    minMitSurprise  = max(0, schwellwert + (2*(schwellwert-2)))
    print("min schwellwert mit surprise %i" %minMitSurprise)
    googlers = []
    for i in range(count):
        googlers.append(int(splitted[i + 3]))
    ok = []
    surpriseNeeded = []
    raus = []
    print("googlers: " + str(googlers))
    for googler in googlers:
        if googler == 0 and schwellwert > 0:
            raus.append(googler)
        elif googler >= minOhneSurprise:
            ok.append(googler)
            print("googler " + str(googler) + " ohne surprise")
        elif googler >= minMitSurprise:
            surpriseNeeded.append(googler)
            print("googler " + str(googler) + " mit surprise")
        else:
            raus.append(googler)
            print("googler " + str(googler) + " ist raus")
    return len(ok) + min(len(surpriseNeeded), surpriseCount);

filename = "D:\\codejam\\B-large.in"
out = open(filename + ".out", "w")
f = open(filename)
number = int(f.readline())
lines = f.read().splitlines()
for i in range(number):    
    a = ("Case #" + str(i+1) + ": " + str(calculate(lines[i])))
    print(a)
    out.write(a + "\n")
    