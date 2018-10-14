
def getRows():
    elements = []
    for i in range(4):
        temp = [int(x) for x in raw_input().split()]
        elements.append(temp)
    return elements
def solve():
    row1 = int(raw_input()) - 1
    elem = getRows()[row1]
    row2 = int(raw_input()) - 1
    elem2 = getRows()[row2]
    
    output = []
    for i in elem:
        if i in elem2:
            output.append(i)
    if len(output) == 0:
        print "Volunteer cheated!"
    elif len(output) > 1:
        print "Bad magician!"
    else :
        print output[0]

if __name__ == "__main__":
    x = int(raw_input())
    for i in range(x):
        print "Case #" +str(i + 1) + ":",
        solve()

