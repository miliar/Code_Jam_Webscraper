import sys

def resolve(exo):
    resultList = []
    cumuleSecondePasse = 0
    parameters = exo.split(' ')

    cookieParSecondes = 2
    palier            = float(parameters[0]) #C
    ferme             = float(parameters[1]) #F
    objectif          = float(parameters[2]) #X
    
    stop = False

    while(False == stop) :
        secondePassePalier = palier / cookieParSecondes
        secondePourObjectif =  objectif / cookieParSecondes
        totalTempsPasse = cumuleSecondePasse + secondePourObjectif
        cumuleSecondePasse += secondePassePalier
        resultList.append(totalTempsPasse)
        
        if len(resultList) > 2 and totalTempsPasse > resultList[-2]: stop = True

        cookieParSecondes += ferme
        

    answer =  min(float(s) for s in resultList)
    return str( "%0.7f" % (answer))

samples = int(sys.stdin.readline().rstrip())
for i in range(samples):
      exo = sys.stdin.readline().rstrip()
      print 'Case #' + str(i+1) + ': ' + resolve(exo)
