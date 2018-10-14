__author__ = 'abu-abdurahman'
import bisect
contents = [lister.strip() for lister in open('D-large.in') ]
numberOfInput = int(contents[0])


def getSolutionD(Nani, kenny):
    Nani.sort()
    kenny.sort()
    wins = 0
    splitNani = []
    splitKenny = []
    if(kenny[0] >= Nani[len(Nani) - 1]):
        return 0
    if(Nani[0] >= kenny[len(kenny) - 1]):
        return len(Nani)
    for x in Nani:
        if(x < kenny[0]):
            del kenny[len(kenny) - 1]
        else:
            wins += 1
            del kenny[0]
        #    if(x == len(Nani) - 1):
        #        return wins
        #else:
        #    splitNani = Nani[x : ]
        #    splitKenny = kenny[x: ]
        #    break

    #Nani.sort()
    #for y in range(len(Nani)):
    #    if(Nani[y] > kenny[y]):
    #        return len(Nani) - y


    return wins


def getSolutionW(Nani, kenny):
    Nani.sort()
    kenny.sort()
    #print kenny
    #print Nani
    if(kenny[0] >= Nani[len(Nani) - 1]):
        return 0
    if(Nani[0] >= kenny[len(kenny) - 1]):
        return len(Nani)
    wins = 0
    for x in Nani:
        y = bisect.bisect(kenny, x)
        if(y == len(kenny)):
            y = 0
        if(x > kenny[y]):
            wins += 1
        del kenny[y]
    return wins

j = 1
solution = []
for i in range(numberOfInput):
    j += 1
    Naoni = [float(x) for x in contents[j].split()]
    print Naoni
    Naoni2 = list(Naoni) #[float(x) for x in contents[j].split()]
    j += 1
    ken = [float(y) for y in  contents[j].split()]
    ken2 = list(ken)
    j += 1
    Naoni.sort()
    ken.sort()
    #print Naoni
    #print ken
    sol = (getSolutionD(Naoni, ken), getSolutionW(Naoni2, ken2))
    print sol , len(Naoni)
    solution.append(sol)



#for s  in solution:
#    print s
output = open('output.txt', 'w')
#output.write('Output \n')
for i in range(1, len(solution) + 1):
    output.write(str('Case #') + str(i) + ': ' + str(solution[i-1][0]) + ' ' + str(solution[i-1][1]) +'\n' )