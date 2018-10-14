path = "C:/Users/Helge/Downloads/"
filename = "D-small-attempt4.in"
input_file = open(path+filename, 'r')
output = open(path + 'output', 'w')

numberOfTestcases = input_file.readline()
def readLineList():
    return input_file.readline().replace('\n', '').split(' ')
        
    
def writeOut(s, count):
    s = 'Case #' + str(count+1) + ': ' + s
    print(s)
    output.write(s + '\n')  

def reduceString(s):
    if len(s)==1:
        return s
    

for i in range(0, int(numberOfTestcases)):
    [X, R, C] = list(map(int, readLineList()))
    
    winner = 'GABRIEL'
    if (R*C)%X != 0:
        winner = 'RICHARD'
    if X == 3 and min(R,C)==1:
        winner = 'RICHARD'
    if X == 4 and (min(R,C)<3):
        winner = 'RICHARD'
        
    writeOut(winner, i)

output.close()