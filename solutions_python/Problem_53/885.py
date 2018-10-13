def calcSnapper(N, K, case, outFile):
    binK = bin(K)[2:]
    if len(binK) >= N:
        if binK[-N:].find('0') == -1:
            outFile.write('Case #%d: ON\n'%case)
        else:
            outFile.write('Case #%d: OFF\n'%case)
    else:
        outFile.write('Case #%d: OFF\n'%case)

#prompt the user for the input file name
fileName = raw_input()

#open the input file and read it.
inFile =  open(fileName, 'r')
outFile = open('SnapperOutput.txt', 'w')

cases = eval(inFile.readline())
for count in range(1,cases+1):
    cur_case = inFile.readline().split(' ')
    calcSnapper(eval(cur_case[0]), eval(cur_case[1]), count, outFile)
    

