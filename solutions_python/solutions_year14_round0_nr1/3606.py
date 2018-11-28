def case(l1, l2):
    ans = []
    for i in l1:
        if i in l2:
            ans.append(i)
    if len(ans) == 0:
        return "Volunteer cheated!"
    elif len(ans) > 1:
        return "Bad magician!"
    else:
        return ans[0]

fin = open("A-small.txt")
fout = open("A-small-answer.txt", "w")
t = int(fin.readline())
for i in range(t):
    a = int(fin.readline()) - 1
    lines = [fin.readline() for j in range(4)]
    l1 = lines[a].split()
    b = int(fin.readline()) - 1
    lines = [fin.readline() for j in range(4)]
    l2 = lines[b].split()
    answer = case(l1, l2)
    fout.write("Case #%d: %s\n" % (i+1, answer))
fin.close()
fout.close()
