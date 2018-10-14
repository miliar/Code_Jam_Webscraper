input1 = open('A-small-attempt1.in','r').read()
lines = input1.split('\n')[1:]
segments = []
for i in range(0,len(lines),5):
    segments.append(lines[i:i+5])
testcases = [[segments[j],segments[j+1]] for j in range(0,len(segments)-1,2)]
for casenumber, case in enumerate(testcases):
    answer1 = int(case[0][0])
    answer2 = int(case[1][0])
    overlaps = [i for i in case[0][answer1].split() if i in case[1][answer2].split()]
   # print overlaps
    if len(overlaps) == 1:
        answer = overlaps[0]
    elif len(overlaps) > 1:
        answer = "Bad magician!"
    elif len(overlaps) < 1:
        answer = "Volunteer cheated!"
    print "Case #{0}: {1}".format(casenumber+1,answer)

