import sys

def main(filename):
    f = open(filename)
    lines = f.readlines()
    f.close()
    out_lines = []
    
    T = int(lines.pop(0))
    
    def get_digits(d):
        digits = []
        dig_str = str(d)
        for c in dig_str:
            digits.append(c)
        return digits

    def all_perms(str):
        if len(str) <= 1:
            yield str
        else:
            for perm in all_perms(str[1:]):
                for i in range(len(perm) + 1):
                    yield perm[:i] + str[0:1] + perm[i:]

    
    for case in xrange(T):
        N = int(lines.pop(0))
        K = sys.maxint
        digits = get_digits(N)
        
        for p in all_perms(digits):
            num_str = ''
            for digit in p:
                num_str += digit
            num = int(num_str)
            if num > N and num < K:
                K = num
        
        if K == sys.maxint:
            str_num = str(N)
            
            sorted_num = sorted(digits)
            num_zeros = 0
            while sorted_num[0] == '0':
                num_zeros += 1
                sorted_num.pop(0)
                
            K_str = sorted_num.pop(0)
            for i in xrange(num_zeros + 1):
                K_str += '0'
            for digit in sorted_num:
                K_str += digit
            K = int(K_str)
        
#        digits = get_digits(N)
#        
#        comp_index = -1
#        for i in xrange(len(digits) - 1, -1, -1):
#            if digits[comp_index] > digits[i]:
#                min_index = min(len(digits) + comp_index, i)
#                max_index = max(len(digits) + comp_index, i)
#                K_arr = digits[:min_index] + [digits[max_index]] +\
#                    digits[min_index+1:max_index] + [digits[min_index]] +\
#                    digits[max_index+1:]
#        
#        K_str = ''
#        for dig in K_arr:
#            K_str += dig
#        K = int(K_str)
        
        
        line = 'Case #%i: %i\n' %((case + 1), K)
        print line
        out_lines.append(line)
    
    f = open('B.out', 'w')
    f.writelines(out_lines)
    f.close()
    

if __name__ == '__main__':
    main('B-small.in')