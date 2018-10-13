

def find_num(n):
    to_int = lambda ss: int(''.join(ss))
    to_list = lambda nn: list(str(nn))
    sn = to_list(n)
    for i in range(len(sn) - 1, 0, -1):
        #import pdb;pdb.set_trace()
        if int(sn[i]) < int(sn[i - 1]):
            sn = to_list(to_int(sn) - to_int(sn[i:]) - 1)
            i = len(sn)
            
    return to_int(sn)
import sys
def main():
    input_file = open(sys.argv[1],'r')
    points = int(input_file.readline().strip())
    for i in range(points):
        num = int(input_file.readline())
        
        print 'Case #%d:' % (i+1,), find_num(num)
        

if __name__ == '__main__':
    main()