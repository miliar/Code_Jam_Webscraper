dct_gtoe = 'yhesocvxduiglbkrztnwjpfmaq'
ord_a = ord('a')
ord_z = ord('z')

def trans_gtoe(ip):
    op_l=[]
    for i in xrange(len(ip)):
        c = ip[i]
        ct = ' '
        ord_c = ord(c)
        if (ord_c>=ord_a) and (ord_c<=ord_z):
            ct = dct_gtoe[ord_c-ord_a]
        op_l.append(ct)
    op = ''.join(op_l)
    return op

def main ():
    fin = open('in.txt','r')
    fout = open('out.txt','w')
    num_cases = int(fin.readline())
    for i in xrange(num_cases):
        ip = fin.readline()
        op = trans_gtoe(ip)
        op1 = "Case #%i: %s\n"%(i+1, op)
        fout.write(op1)
main()
