def FindChoice(L1,L2):
    number=0
    result=-1
    for x in L1:
        if x in L2:
            result = x
            number+=1
    if number>1:
        return "Bad magician!"
    elif number==0:
        return "Volunteer cheated!"
    else: return str(result)
    
def Main():
    f = open("A-small-attempt0.in")
    s = f.read()
    s = s.split("\n")
    cases = int(s.pop(0))

    for case in range(cases):
        rows1 = []
        rows2 = []
        first = int(s.pop(0))
        for x in range(4):
            rows1.append(s.pop(0))
        second = int(s.pop(0))
        for x in range(4):
            rows2.append(s.pop(0))
        temp1 = rows1[first-1].split(" ")
        temp2 = rows2[second-1].split(" ")
        temp1 = [int(x) for x in temp1]
        temp2 = [int(x) for x in temp2]
        print("Case #"+str(case+1)+": "+FindChoice(temp1,temp2))

Main()
