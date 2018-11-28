from collections import deque
f = open('./D-large.in')
nbrs = deque([k for k in f.read().split()])
f.close()

def r():
    return nbrs.popleft()

def optimal(P1, P2):
    P1 = [k for k in P1]
    P2 = [k for k in P2]
    score = 0
    for k in range(0, len(P1)):
        if P1[k] > P2[0]: #can win!
            score += 1
            P2.pop(0)
        else: # can't win
            P2.pop()
    return score
    
def subopt(P1, P2):
    P1 = [k for k in P1]
    P2 = [k for k in P2]
    score = 0
    for k in P1:
        if k > max(P2):
            score += 1
            P2.pop(0)
        else:
            index = 0
            while(P2[index] < k):
                index += 1
            P2.pop(index)
    return score

f = open('output.out', 'w')
cases = int(r())
for current_case in range(0, cases):
    n = int(r())
    P1 = []
    P2 = []
    for k in range(0, n):
        P1.append(float(r()))
    for k in range(0, n):
        P2.append(float(r()))
    P1 = sorted(P1)
    P2 = sorted(P2)
    #print(P1)
    #print(P2)
    s = 'Case #' + str(current_case+1) + ': ' + str(optimal(P1, P2)) + ' ' + str(subopt(P1, P2)) + '\n'
    f.write(s)
    print(s)
    

f.close()