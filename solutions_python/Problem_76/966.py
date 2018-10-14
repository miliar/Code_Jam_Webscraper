import string

#find all numbers with colliding bits
def patrick_sum(numbers):
    bs=[]
    for n in numbers:
        #ignore leading `0b` and reverse
        bn=bin(n)[2:][::-1]
        for i in range(len(bn)):
            v_n=str(bn[i])
            if i >= len(bs):
                bs.append(v_n)
            else:
                v_s=bs[i]
                if v_n == v_s:
                    bs[i]='0'
                else:
                    bs[i]=str(int(v_n)+int(v_s))
    #reverse back
    bs=bs[::-1]
    if not bs:
        return 0
    #join
    binary_string=string.join(bs,'')
    #return (int(binary_string,2),binary_string)
    return int(binary_string,2)

def split_candy(s_candies):
    p_candies=[]
    while s_candies:
        candy=s_candies.pop(0)
        p_candies.append(candy)
        ps_p=patrick_sum(p_candies)
        ps_s=patrick_sum(s_candies)
        #print 'P: %s (%s) S: %s %s'%(p_candies,ps_p,s_candies,ps_s)
        if ps_p == ps_s:
            return (p_candies,s_candies)
    return ([],[])

if __name__=="__main__":
    import sys
    fn=sys.argv[1]
    lines=[line.strip() for line in open(fn).readlines()]
    out=open(fn.replace('in','out'),'w')
    n_cases = int(lines.pop(0))
    print 'cases: %s'%n_cases
    case =1
    while lines:
        print "%s / %s"%(case,n_cases)
        n_candies = int(lines.pop(0))
        candies_str = lines.pop(0)
        candies=[int(c) for c in candies_str.split()]
        candies.sort()
        #print candies
        if len(candies)!=n_candies:
            print 'something is wrong read %s got %s case %s'%(n_candies,len(candies),case)
        p_pile,s_pile=split_candy(candies)
        #print 'P: %s S: %s'%(p_pile,s_pile)
        result='Case #%s: %s\n'%(case,sum(s_pile) if s_pile else 'NO')
        print result[:-1]
        out.write(result)
        case+=1

