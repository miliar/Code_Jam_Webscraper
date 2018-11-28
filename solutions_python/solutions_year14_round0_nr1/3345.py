import sys

def solve():
    return 0


num_case = int(sys.stdin.readline())

for n in range(1, num_case + 1):
    #line = sys.stdin.readline().strip().split()
    row1 = int(sys.stdin.readline()) - 1
    
    lst1 = []
    for m in range(4):
        lst1.append(set(sys.stdin.readline().split()))
    
    set1 = lst1[row1]
    #print(row1)

    row2 = int(sys.stdin.readline()) - 1
    #print(row2)
    
    lst2 = []
    for m in range(4):
        lst2.append(set(sys.stdin.readline().split()))
    
    set2 = lst2[row2]
    
    #print(set1)
    #print(set2)
    
    set3 = set1.intersection(set2)
    
    print("Case #" + str(n) + ": ", end='')
    if len(set3) == 1:
        print(set3.pop())
    elif len(set3) > 1:
        print("Bad magician!")
    elif len(set3) == 0:
        print("Volunteer cheated!") 
    
    #print(lst1)

    
