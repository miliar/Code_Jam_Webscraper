__author__ = 'Pierre-Luc'


def solve(C,F,X,numCase):
    time = 0
    cps = 2
    done = False
    if X<C:
        time = X/cps
    else:
        while done == False:
            time = time + C/cps
            'Decide whether to build another farm or to keep to X'
            timeToFinish1 = (X-C)/cps
            timeToFinish2 = X/(cps+F)
            if timeToFinish1<= timeToFinish2:
                time = time + (X-C)/cps
                done = True
            else:
                cps += F




    fOutput.write("Case #" + str(numCase+1) + ": ")
    fOutput.write(str(time))
    fOutput.write("\n")




list = [1]
a = 1
typeInput = "Large"
fInput = open("2Input" + typeInput + ".txt","r")
fOutput = open("2Output" + typeInput + ".txt","w")


T = int(fInput.readline())

for numCase in range(0,T):
    line = fInput.readline().strip("\n").split(" ")
    C = float(line[0])
    F = float(line[1])
    X = float(line[2])
    solve(C,F,X,numCase)

