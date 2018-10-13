T = int(raw_input())
cards = [[[[0 for i in range(4)] for j in range(4)] for k in range(2)] for l in range(T)]
row = [[0,0] for i in range(T)]

#cards[2][1][2][3] = 1
#print cards
#print cards[2][1][2]

for i in range(T):
    for j in range(2):
        row[i][j] = int(raw_input())
        for k in range(4):
            cards[i][j][k] = map(int,raw_input().split())

#print cards
#print row
f = open('magic_ans.txt', 'w')

for i in range(T):
    x = [0,0]
    for j in range(2):
        x[j] = cards[i][j][row[i][j]-1]
    #print x
    z = set(x[0]) & set(x[1])
    #print z
    if len(z) == 1:
        f.write("Case #%d: %s\n" %(i+1,str(list(z)[0])))
    elif len(z) == 0:
        f.write("Case #%d: %s\n" %(i+1,"Volunteer cheated!"))
    else:
        f.write("Case #%d: %s\n" %(i+1,"Bad magician!"))
