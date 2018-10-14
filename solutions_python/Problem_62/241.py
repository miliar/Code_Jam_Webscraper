def filtra_acima(wires, origem):
    return [wire for wire in wires if wire[0] > origem ]

def filtra_abaixo(wires, destino):
    return [wire for wire in wires if wire[1] < destino ]

def calculate(wires):
    count = 0
    for i in xrange(len(wires)):
        wires_acima = filtra_acima(wires, wires[i][0])
        wires_abaixo = filtra_abaixo(wires_acima, wires[i][1])
        
        count += len(wires_abaixo)
        
    return count
    
#print calculate([(1,3), (2,5), (4,1), (6,7)])
#print calculate([(1,10), (5,5), (7,7)])
#print calculate([(1,1), (2,2)])

def read_input(n):
    wires = []
    for i in xrange(n):
        o, d = map(int, raw_input().split())
        wires.append( (o,d) )
    
    return wires

for case_number in xrange(int(raw_input())):
    n,  = map(int, raw_input().split())
    wires = read_input(n)
    result = calculate(wires)
    print 'Case #%d: %s' % (case_number+1, result)