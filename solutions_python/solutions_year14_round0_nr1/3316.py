import sys

def resolve(f):
    answer1 = int(f.readline()[:-1])
    m1 = []
    for i in range(4):
        m1.append(f.readline()[:-1].split(" "))
    answer2 = int(f.readline()[:-1])
    m2 = []
    for i in range(4): 
        m2.append(f.readline()[:-1].split(" "))
    f1 = m1[answer1 -1]
    f2 = m2[answer2 -1]
    a = compare(f1,f2)
    if a > 0:
        return str(a)
    elif a == 0:
        return "Volunteer cheated!"
    else:
        return "Bad magician!"
        
def compare(f1,f2):
    match = 0
    for i in f1:
        for j in f2:
            if i == j:
                if match > 0:
                    return -1
                else:
                    match = int(i)
    return match

f = open(sys.argv[1])
cases = int(f.readline()[:-1])
for i in range(cases):
    r = resolve(f)
    print("Case #%i: %s" %(i+1, r))
