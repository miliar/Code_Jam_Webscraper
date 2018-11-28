out = open("ASmallOut.txt", 'w')
text = open("ASmall.txt", 'r')
text = text.readlines()

def solve(p1, p2):
    count = 0
    for i in poss1:
        for j in poss2:
            if i == j:
                count += 1
                ans = i
    if count == 0:
        return "Volunteer cheated!"
    elif count == 1:
        return str(ans)
    else:
        return "Bad magician!"

tc = int(text[0])
line = 0
for c in range(tc):
    line += 1
    r1 = int(text[line])
    for i in range(r1):
        line += 1
    poss1 = [int(num) for num in text[line].split()]
    for i in range(4-r1):
        line += 1
    line += 1
    r2 = int(text[line])
    for i in range(r2):
        line += 1
    poss2 = [int(num) for num in text[line].split()]
    for i in range(4-r2):
        line += 1
    ans = solve(poss1, poss2)
    case = c + 1
    out.write("Case #" + str(case) + ": " + ans + "\n")
out.close()

    
    
