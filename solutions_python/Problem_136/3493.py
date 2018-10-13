from builtins import str, sum
import os

if __name__ == "__main__":
    fdata = open("B-small-attempt0.in", mode = "r")

    nbTest = int(fdata.readline())
    os.system('clear')
########################################################################################################
########################################################################################################
    for iTest in range(nbTest):
        line = fdata.readline()
        datas = line.split()
        C = float(datas[0])
        F = float(datas[1])
        X = float(datas[2])

        tempsTotal = []
        tempsConstructionFerme = [0]
        production = [2]



        n = 0
        while 1:
            currentTotal = (X / production[n]) + sum(x for x in tempsConstructionFerme)
            tempsTotal.append(currentTotal)
            if currentTotal > min(tempsTotal):
                break

            n = n + 1
            production.append(2 + (n * F))
            tempsConstructionFerme.append(C / production[n - 1])
        print("Case #{0}: {1}".format(iTest + 1, min(tempsTotal)))

########################################################################################################



