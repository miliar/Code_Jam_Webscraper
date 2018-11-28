f = open('D-large.in')
input_file = [x.strip().split() for x in f.readlines()]
f.close()

#number of cases
nC = int(input_file[0][0])

cases = []
for idx in range(nC):
    N = int(input_file[idx*3+1][0])
    #player A's set
    A = [float(x) for x in input_file[idx*3+2]]
    #player B's set
    B = [float(x) for x in input_file[idx*3+3]]
    cases.append([N,A,B])


def solve_deceit(A,B):
    A = sorted(A)
    B = sorted(B)
    points_deceit = 0
    while A:
        if A[0] > B[0]:
            points_deceit += 1
            A.pop(0)
            B.pop(0)        
        elif A[0] < B[0]:
            A.pop(0)
            B.pop()
        elif A[-1]>B[-1]:
            #highest element of A wins, B 
            points_deceit += 1
            A.pop()
            B.pop(0)
        else:
            #player A forces B to use their highest element
            A.pop(0)
            B.pop()
    return points_deceit


def solve_war(A,B):   
    A = sorted(A)
    B = sorted(B)
    points_war = 0
    while A:
        if A[-1] > B[-1]:
            points_war += 1
            A.pop()
            B.pop(0)
        else:
            B.remove(min([x for x in B if x>A[-1]]))
            A.pop()
            
    return points_war    

f = open('D_large_solution.txt','w')

for idx,case in enumerate(cases):
    N,A,B = case
    deceit = solve_deceit(A,B)
    war = solve_war(A,B)
    f.write('Case #'+str(idx+1) + ': ' + str(deceit) +' ' + str(war) + '\n')

f.close()