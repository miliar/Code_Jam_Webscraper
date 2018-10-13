'''
Created on 2010-5-8

@author: Zhonghao
'''


def gcd(a, b):
    while b != 0:
        t = b
        b = a % b
        a = t
    return a

def gcd_list(l):
    if len(l) == 1:
        return l[0]
    
    if len(l) == 2:
        return gcd(l[0], l[1])
    else:
        l = list(gcd(l[0], l[1])).extend(l[1:])
        return gcd_list(l)


if __name__ == '__main__':
    import sys
    in_file = sys.argv[1]
    out_file = sys.argv[2]
    
    lines = open(in_file).readlines()
    lines = [x.rstrip() for x in lines]
    lines = lines[1:]
    
    case_no = 0
    wfile = open(out_file, 'w')
    for line in lines:
        case_no += 1
        wfile.write('Case #' + str(case_no) + ': ')
        l = line.split()[1:]
        l = [int(x) for x in l]
        
        l.sort()
        l2 = []
        for i in range(len(l) - 1):
            l2.append(l[i+1] - l[i])
            
        print l2
        T = gcd_list(l2)
        print T
        tmp = T
        while tmp < l[0]:
            tmp += T
            
        res = tmp - l[0]
        wfile.write(str(res) + '\n')
        


# END