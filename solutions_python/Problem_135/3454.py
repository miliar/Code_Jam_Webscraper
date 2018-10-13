
def result(input):
    input = map(lambda x:map(int,x.split()),input)
    x = set(input[input[0][0]]) & set(input[5+input[5][0]])
    if len(x) == 0:
        return 'Volunteer cheated!'
    elif len(x) > 1:
        return 'Bad magician!'
    else:
        return str(list(x)[0])
                        

f = open('A-small-attempt0.in')
r = f.readlines()
w = open('A-small-attempt0.out','w')

for i in range((len(r)+1)/10):
    w.write('Case #%s: %s\n' % (str(i+1), result(map(lambda x:x.strip(),r[10*i+1:10*(i+1)+1]))))
f.close()
w.close()
