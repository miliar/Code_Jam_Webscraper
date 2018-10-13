import sys

def testRuns(runs):
    for i in range(0,runs):
        playGame(i)

def playGame(i):
    global curr_line
    printcase = 'Case #'+str(i+1)+':'
    #Get guess
    curr_line += 1
    g1 = int(inputs[curr_line])-1
    #Get 4 rows for arrangement
    arr = [[],[],[],[]]
    for x in range(0,4):
        curr_line += 1
        arr[x] = [int(n) for n in inputs[curr_line].split()]
    #Get second guess
    curr_line += 1
    g2 = int(inputs[curr_line])-1
    #Get 4 rows for second arrangement
    arr2 = [[],[],[],[]]
    for x in range(0,4):
        curr_line += 1
        arr2[x] = [int(n) for n in inputs[curr_line].split()]
    #Get first guess row
    r1 = arr[g1]

    answer = 0
    #Get answer based on second guess and arrangement
    for item in arr[g1]:        
        if item in arr2[g2]:
            if answer == 0:
                answer = item
            else:
                print printcase,'Bad magician!'
                answer = -1
                break
    if answer == 0:
        print printcase,'Volunteer cheated!'
        answer = -1
    elif answer not in [-1,0]:
        pass
        print printcase,answer

inputs = []
curr_line = 0

with open(sys.argv[1], 'r') as fp:
    inputs = fp.readlines()

runs = int(inputs[curr_line])
testRuns(runs)
