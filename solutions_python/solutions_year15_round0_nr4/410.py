
def solve( X , R , C):
    people = ["RICHARD","GABRIEL"]
    if (R*C)%X !=0 or (R*C)<X:
        return people[0]
    result = -1
    if X==1:
        result = 1
    elif X==2:
        result = 1
    elif X==3:
        if R >C: return solve(X,C,R)
        if R==1: result = 0
        else: result = 1
    elif X==4:
        if R >C: return solve(X,C,R)
        if R==1: result = 0
        elif R==2: result = 0
        elif R==3: result = 1
        elif R==4: result = 1
    return people[result]


with open("D-small-attempt1.in")as file:
    T = int(file.readline())
    for i in range(T):
        line = [int(k) for k in file.readline().strip().split(" ")]
        r = solve(*line)
        print("Case #" + str(i+1) +": " + r)
