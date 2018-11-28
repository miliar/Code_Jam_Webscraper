

def solveCase():
    row=int(input())
    rows=[input() for i in range(4)]
    set1=[int(e) for e in rows[row-1].split()]
    row=int(input())
    rows=[input() for i in range(4)]
    set2=[int(e) for e in rows[row-1].split()]
    matches=[i for i in set1 if i in set2]
    if len(matches)==1: return str(matches[0])
    elif len(matches)==0: return "Volunteer cheated!"
    else: return "Bad magician!"




if __name__=="__main__":
    cases=int(input())
    for i in range(1,cases+1):
        print("Case #"+str(i)+": "+solveCase())
