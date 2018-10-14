f = open("bottrust.large.in", "r")

t = int(f.readline())

N = []

C = []
B = []

j = 0

for line in f:
    v = line.split(" ")
    N.append(int(v[0]))

    C.append([])
    B.append([])
    
    for i in range(0, int(v[0])):
        C[j].append(v[(2*i)+1])
        B[j].append(int(v[(2*i)+2]))

    j += 1

f.close()

STEPS = []

POS = {}



for u in range(0, t):
    master = C[u][0]
    steps = 0

    free = 0

    POS['O'] = 1
    POS['B'] = 1

    for i in range(0, N[u]):
        goal = B[u][i]
        if C[u][i] == master:
            togoal = abs(goal - POS[C[u][i]])
            togoal += 1 # push

            POS[C[u][i]] = goal

            free += togoal
            steps += togoal
        elif (C[u][i] != master and free > 0):
            # kolla free moves
            togoal = abs(goal - POS[C[u][i]])

            if free >= togoal:
                POS[C[u][i]] = goal
            else:
                # free > 0 men under hela vägen
                if goal < POS[C[u][i]]:
                    POS[C[u][i]] -= free
                else:
                    POS[C[u][i]] += free

            free = 0

            # betala för resten

            togoal = abs(goal - POS[C[u][i]])
            togoal += 1 # push

            POS[C[u][i]] = goal
                
            free += togoal
            steps += togoal

            master = C[u][i]
        else:
            # inga free steps, betala
            togoal = abs(goal - POS[C[u][i]])
            togoal += 1 # push

            POS[C[u][i]] = goal

            free += togoal
            steps += togoal

            master = C[u][i]

    STEPS.append(steps)

f = open("bottrust.out", "w")

for i in range(0, t):
    f.write("Case #" + str(i + 1) + ": " + str(STEPS[i]) + "\n")

f.close()

print "done"
            
            
                

            
            

        
        



















        
