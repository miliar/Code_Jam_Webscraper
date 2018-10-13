T = input()

for t in range(T):

    q1 = input()
    g1 = []
    g1.append(raw_input().split(' '))
    g1.append(raw_input().split(' '))
    g1.append(raw_input().split(' '))
    g1.append(raw_input().split(' '))

    q2 = input()
    g2 = []
    g2.append(raw_input().split(' '))
    g2.append(raw_input().split(' '))
    g2.append(raw_input().split(' '))
    g2.append(raw_input().split(' '))

    result = set(g2[q2-1]) & set(g1[q1-1])
    if len(result) == 0 : result = "Volunteer cheated!"
    elif len(result) == 1 : result = result.pop()
    else : result = "Bad magician!"

    print "Case #" + str(t+1) + ": " + str(result)

