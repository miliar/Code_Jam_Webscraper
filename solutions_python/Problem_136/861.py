from collections import deque
f = open('./B-large.in')
nbrs = deque([k for k in f.read().split()])
f.close()

def r():
    return nbrs.popleft()


f = open('output.out', 'w')
cases = int(r())
for current_case in range(0, cases):
    C = float(r())
    F = float(r())
    X = float(r())
    
    t = 0
    min_t = X/2
    farms = 0
    while t < min_t:
        min_t = min(min_t, t + X/(2+F*farms))
        t += C / (2+F*farms)
        farms += 1
    f.write('Case #' + str(current_case+1) + ': ' + str(min_t) + '\n')
    

f.close()