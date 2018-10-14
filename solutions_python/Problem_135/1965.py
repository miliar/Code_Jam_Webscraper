import operator

debug = True
err1 = "Bad magician!"
err2 = "Volunteer cheated!"

def resolve(a, b):
    c = list(set(a) & set(b))
    r = len(c)
    if r == 1:
        return c[0]
    elif r < 1:
        return err2
    else:
        return err1
                
    
input_file = open('A-small-practice.in')
output_file = open('output', 'w')

T = int(input_file.readline())
for i in range(1, T+1):
    r1 = int(input_file.readline())
    row1 = [ input_file.readline()[:-1].split() for _ in range(4)][r1-1]
    r2 = int(input_file.readline())
    row2 = [ input_file.readline()[:-1].split() for _ in range(4)][r2-1]
    sol = 'Case #%d: %s\n' % (i, resolve(row1, row2))
    output_file.write(sol)
    if debug:
        print sol[:-1]

    
input_file.close()
output_file.close()

