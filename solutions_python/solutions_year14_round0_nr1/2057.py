f = open('A-small-attempt0.in').read().split('\n')

def chunks(l, n):
    for i in range(1, len(l)-1, n):
        yield l[i:i+n]

def flatten(lst):
    return sum( ([x] if not isinstance(x, list) else flatten(x)
             for x in lst), [] )
 
inputlist = chunks(f, 10)

n = 1
r=[]

for x in inputlist:    
    row = [int(x[0])-1, int(x[5])-1]
    rows = [[y.split(" ") for y in x[1:5]],
            [y.split(" ") for y in x[6:11]]]
    a = rows[0][row[0]]
    b = rows[1][row[1]]
    sames = []

    for x in a:
        if x in b:
            sames.append(x)

    answer = (sames[0] if len(sames) == 1 else 
              ("Bad magician!" if len(sames) > 1 else
              "Volunteer cheated!"))

    r.append("Case #{}: {}".format(n, answer))
    n += 1

with open('A-small-out.txt', 'w+') as out:
    for x in r:
        out.write(x + '\n')
    