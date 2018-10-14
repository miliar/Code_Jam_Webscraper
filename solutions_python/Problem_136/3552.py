__author__ = 'jbojcic'

def main():
    f = open('B-small-attempt2.in', 'r')
    f2 = open('B-small-attempt2-output.in', 'w')
    numOfTestCases = f.readline()

    for i in range(int(numOfTestCases)):
        line = f.readline()
        line = line[0:-1].split(' ')
        productionFactor = 2.0
        C = float(line[0])
        F = float(line[1])
        X = float(line[2])
        t = 0.0
        while(True):
            oldSettingTime = t + (X / productionFactor)
            newSettingTime = t + (C / productionFactor) + (X / (productionFactor+F))
            if(newSettingTime < oldSettingTime):
                t = t + (C / productionFactor)
                productionFactor += F
            else:
                t = oldSettingTime
                break

        f2.write("Case #" + str(i+1) + ": " + "{0:.7f}".format(t) + "\n")

    f.close();
    f2.close();

main()

