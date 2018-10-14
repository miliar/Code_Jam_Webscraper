#f = open('Magic-Test.txt')
f = open('Magic-Small.txt')

def func(caseI,gen):
    row1 = int(gen.next())-1
    table1 = [gen.next().split(' ')[:4] for i in range(4)]
    row2 = int(gen.next())-1
    table2 = [gen.next().split(' ')[:4] for i in range(4)]
    results = filter(lambda x:x in table1[row1],table2[row2])
    v = ''
    if len(results) == 0:
        v = 'Volunteer cheated!'
    elif len(results) > 1:
        v = 'Bad magician!'
    elif len(results) == 1:
        v = results[0]
    return 'Case #' + str(caseI+1)+": " + v

lines = f.read().split('\n')
cases = int(lines[0])
gen = (l for l in lines[1:])
for i in range(cases):
    print func(i,gen)
