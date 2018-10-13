def StandingOvation(Smax, digits, case):
    
    result = 'Case #' + str(case + 1) +': ' 
    invited = 0
    audience = 0
    standUpAudience = 0
    invitedSum = 0
    for Si in range(Smax + 1):
        digitAudience = int(digits[Si])
      
        invited = 0
        stop = False
        while not stop:
            standUp = StandUp(standUpAudience + invited, Si, digitAudience)
            if standUp == 0:
                invited += 1                
            else:
                stop = True
                standUpAudience = standUp 
        invitedSum += invited
        
    result += str(invitedSum)       

    return result

def StandUp(standUpAudience, Si, digitAudience):
   if standUpAudience >= Si:
       return standUpAudience + digitAudience
   return 0

def WriteFile(name, text):
    file = open(name,'w')
    file.write(text)
    file.close()

def ReadFile(name):
    file = open(name , 'r')       
    return file

def ReadLine(file):
    linea = file.readline()
    return linea

nameInputFile = 'c:\\CodeJam2015\\QualificationRound\\StandingOvation\\A-large.in'
nameOutputFile = 'c:\\CodeJam2015\\QualificationRound\\StandingOvation\\A-large.out'

file = ReadFile(nameInputFile)
T = int(ReadLine(file))

result = ''

for case in range(T):
   
    line = ReadLine(file)

    lista = line.split(' ')
    
    Smax = int(lista[0])
    digits = lista[1].rstrip('\n')
    result += StandingOvation(Smax, digits, case) + '\n'

WriteFile(nameOutputFile, result)