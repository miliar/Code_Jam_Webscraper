import math

class ProblemA:
    def timetogetfarm(c, f, numberOfFarms):
        return c/(f*numberOfFarms + 2)

time = 0

output = ''

with open("E:\\file.txt") as f:
    content = f.readlines()

    i = content.pop(0)
    for p in range(1, int(i)+1):
        numberOfFarms = 0
        timetofarm = 0

        case = content.pop(0)
        splitted = case.split()
        c = float(splitted[0])
        f = float(splitted[1])
        x = float(splitted[2])

        #rate = f*numberOfFarms + 2
        oldAnswer = x/2
        for j in range(1, int(x)):
            #zeroFarmTime = x/2
            timetofarm += ProblemA.timetogetfarm(c, f, numberOfFarms)
            numberOfFarms += 1
            newAnswer = timetofarm + x/(f*numberOfFarms + 2)

            oldAnswer = min(oldAnswer, newAnswer)

        output += 'Case #{0}: {1:.7f}\n'.format(p, oldAnswer)
        numberOfFarms = 0
        timetofarm = 0

text_file = open("E:\\output.txt", "w")
text_file.write(output)
text_file.close()
