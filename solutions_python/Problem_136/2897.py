from decimal import Decimal

if __name__ == '__main__':
    inf = open('B-large.in')
    outf = open('cookies.out', 'w')
    
    T = int(inf.readline())
    for i in range(1, T+1):
        line = inf.readline().split()
        c = Decimal(line[0])
        f = Decimal(line[1])
        x = Decimal(line[2])
        
        old_f = Decimal(0.0)
        cur_f = Decimal(2.0)
        min_t = 99999999
        past_t = Decimal(0.0)
        
        while True:
            if cur_f > old_f:
                t = x / cur_f
                t += past_t
                old_f = cur_f
                if t < min_t:
                    min_t = t
                else:
                    break
            else:
                past_t += c / cur_f
                cur_f += f
        
        min_t = min_t.quantize(Decimal('.0000001'), rounding='ROUND_UP')
        outf.write('Case #%d: %s\n' % (i, str(min_t)))

    inf.close()
    outf.close()
    
