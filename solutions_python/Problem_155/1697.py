path = "C:/Users/Helge/Downloads/"
filename = "A-large.in"
input_file = open(path+filename, 'r')
output = open(path + 'output', 'w')

numberOfTestcases = input_file.readline()
def readLineList():
    return input_file.readline().replace('\n', '').split(' ')
        
    
def writeOut(s, count):
    s = 'Case #' + str(count+1) + ': ' + s
    print(s)
    output.write(s + '\n')  
    
for i in range(0, int(numberOfTestcases)):
    [S_max, S_bit] = readLineList()
    standing = int(S_bit[0])
    friends = 0
    for j in range(1,int(S_max)+1):
        if int(S_bit[j]) > 0:
            friends += max(0,j-standing)
            standing += max(0,j-standing)
            standing += int(S_bit[j])
    writeOut(str(friends), i)

output.close()