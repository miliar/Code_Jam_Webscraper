import fileinput as FI

def sum_digits(digit):
    return sum(int(x) for x in digit if x.isdigit())
inPut = FI.input()
cases = int(inPut.readline())

for case in xrange(cases):
    ppl_to_send = 0
    count = 0
    each_case = inPut.readline()
    values = each_case.split()
    for i in xrange(int(values[0])+1):
        tmp =0
        if values[1][i] == '0':
            continue
        if count < i:
            tmp = i-count
            ppl_to_send += tmp
        count = count + int(values[1][i]) + tmp
        
    print 'Case #'+ str(case+1)+': '+ str(ppl_to_send)   