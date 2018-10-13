debug = True
 
def resolve(C, F, X):
    V = 2  # 2 cookies per second
    T = 0
    while C < X: 
        T += C / V
        if X / (V + F) < (X - C) / V:
            V = V + F
        else:
            X -= C
    T += X/V
    return "%0.7f" % T 


input_file = open('A-small-practice.in')
output_file = open('output', 'w')

T = int(input_file.readline())
for i in range(1, T + 1):
    C, F, X = map(float, input_file.readline().split())

    sol = 'Case #%d: %s\n' % (i, resolve(C, F, X))
    output_file.write(sol)
    if debug:
        print sol[:-1]

    
input_file.close()
output_file.close()

