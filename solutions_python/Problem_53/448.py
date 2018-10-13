'''
Created on 2010-5-8

@author: Zhonghao
'''


if __name__ == '__main__':
    import sys
    in_file = sys.argv[1]; out_file = sys.argv[2]
    lines = open(in_file).readlines()
    lines = [x.lstrip() for x in lines]
    
    lines = lines[1:]
    
    wfile = open(out_file, 'w')
    case_no = 0
    for line in lines:
        case_no += 1
        wfile.write('Case #' + str(case_no) + ': ')
        N, K = line.split()
        N = int(N); K = int(K)
        tmp = 2 ** N
        if K % tmp == tmp - 1:
            wfile.write('ON\n')
        else:
            wfile.write('OFF\n')
            

# END