class Free:
    def __init__(self, left, right):
        self.left = left
        self.right = right

def findFree(N,people):
    x = 'x'
    stalls = [x] + [None for i in range(N)] + [x]


    while people:
        MAX = 0

        free = None
        
        counted = False
        counter = 0
        for i in range(len(stalls)):
            if stalls[i] is None:
                counter += 1
                if not counted:
                    counted = True
                    left = i - 1 #left index
                
            else:
                if counted:
                    counted = False
                    right = i
                    if (right - left) > MAX:
                        MAX = right - left
                        free = Free(left,right)
                counter = 0
                left = 0
                right = 0
        #INSERT PERSON
        stalls[(free.left + free.right)//2] = x
        
        if people == 1:
            return free.left,free.right
        people -= 1
        free = None
        MAX = 0


def compute(N,people):
    N,people = int(N), int(people)
    left,right = findFree(N,people)

    R = right - (left+right)//2-1
    L = (left+right)//2  - left  -1

    if R>L:
        return R,L
    return L,R


filename = "C-small-1-attempt0.in"
infile = open(filename, 'r')
lines = infile.readlines()

cases = []
t = int(lines[0].strip('\n'))
for i in range(1,t+1):
    cases.append(lines[i].strip('\n').split(' '))

infile.close()

outfile = open("C-small-1-attempt0.out", 'w')

caseNo = 1
for case in cases:
    MAX, MIN = compute(case[0], case[1])
    outfile.write("Case #{}: {} {}\n".format(caseNo, MAX, MIN))
    caseNo += 1

outfile.close()
    
    
        
