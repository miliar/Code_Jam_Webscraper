def countOccurances(l1,l2):
    occurances = 0
    lastOne = 0
    for i in range(len(l1)):
        for j in range(len(l2)):
            if l1[i] == l2[j]:
                occurances += 1
                lastOne = l1[i]
    return occurances, lastOne

def solve(r1, b1, r2, b2):
    occurances, lastOne = countOccurances(b1[r1-1], b2[r2-1])
    if occurances == 0:
        return 'Volunteer cheated!'
    elif occurances == 1:
        return str(lastOne)
    else:
        return 'Bad magician!'

with open('small.in') as f:
    content = f.readlines()
content = [[int(j) for j in i.rstrip('\n').split()] for i in content]
for i in range(int(content.pop(0)[0])):
    print ('Case #' + str(i + 1) + ': ' + solve(content.pop(0)[0], [content.pop(0) for i in range(4)], content.pop(0)[0], [content.pop(0) for i in range(4)]))
