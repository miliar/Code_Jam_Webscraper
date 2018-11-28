import copy

def solve(a, b):

    s_b = str(b)
    if len(s_b)==1:
        return 0
    elif len(s_b)==2:
        ans = 0
        for i in range(a, b+1):
            i_prime = (i/10 + i%10)*11-i
            if i< i_prime < b+1:
                ans+=1
                #print i
        return ans
    else:
        ans = 0
        for i in range(a, b+1):
            s_i = str(i)
            ii = int(s_i[1:]+s_i[0])
            iii = int(s_i[2]+s_i[:2])
            if i< ii < b+1:
                ans+=1
                #print (i,ii)
            if i < iii < b+1:
                ans +=1
                #print (i,iii)

        return ans
    

if __name__ == '__main__':
    str_in = 'C-small-attempt0.in'
    #str_in = 'A-large.in'
    #str_in = 'A-test.in'
    f_out = open(str_in.rstrip('.in') + '.out', 'w')
    f_in = open(str_in)
    N = int(f_in.next())
    
    
    for num_q in range(N):
        a,b = [int(_) for _ in f_in.next().split()]
        output = 'Case #' + str(num_q + 1) + ': ' + str(solve(a, b)) +'\n'
        f_out.write(output); print output,

    f_in.close()
    f_out.close()
    
    #print 'exit'
    #print A_D, set_A

