INPUT_FILE = 'inputs/C-small-attempt0.in'
OUTPUT_FILE = 'outputs/C-small-attempt0.out'

PHRASE = 'welcome to code jam'
counter = 0;

def findLetter(index, startPos, str):
    global counter
    while True:
        newPos = str.find(PHRASE[index], startPos)
        if (newPos != -1) and (index < len(PHRASE) - 1) :
            findLetter(index + 1, newPos + 1, str)
        elif (newPos != -1):
            counter = counter + 1;
        else:
            return;
        startPos = newPos + 1

f_in = open(INPUT_FILE, 'r')
f_out = open(OUTPUT_FILE, 'w+')

N = int(f_in.readline())

for i in range(N):
    # minor optimizations
    case = f_in.readline()
    case = case[case.find(PHRASE[0]):case.rfind(PHRASE[-1]) + 1]
    buffer = ''
    for j in case:
        if j in PHRASE:
            buffer = buffer + j
    case = buffer;
    
    # actual search
    counter = 0
    findLetter(0, 0, case)
    f_out.write("Case #" + str(i + 1) + ": " + str(counter % 1000).zfill(4) + "\n")

f_in.close()
f_out.close()