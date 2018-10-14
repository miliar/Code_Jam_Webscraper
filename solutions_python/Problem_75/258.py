import math

if __name__ == '__main__':
    input = open('./source/B-small-0.in', 'r')
    output = open('./source/B-small-0.out', 'w')

    n = int(input.readline().strip())
    for i in range(n):
        seq = input.readline().strip().split()
        j = 0
        combine = {}
        opposed = {}
        c = int(seq[j])
        k = 0
        while k < c:
            j += 1
            k+=1
            cstr = seq[j]
            combine[(cstr[0], cstr[1])] = cstr[2]
            combine[(cstr[1], cstr[0])] = cstr[2]    
        j += 1
        d = int(seq[j])
        k = 0
        while k < d:
            j += 1
            k+=1
            ostr = seq[j]
            opposed[ostr[0]] = ostr[1]
            opposed[ostr[1]] = ostr[0]
        j += 1
        n = int(seq[j])
        rseq = seq[j+1]
        output_list = []
        print rseq
        for k in range(0,n):
            cs = rseq[k]
            #print cs
            if len(output_list) == 0:
                output_list.append(cs)
            else:
                pcs = output_list[-1]
                if combine.has_key((cs,pcs)) or combine.has_key((pcs, cs)):
                    output_list.pop(-1)
                    if combine.has_key((cs,pcs)):
                        cs = combine[(cs,pcs)]
                        output_list.append(cs)
                    else:
                        cs = combine[(pcs,cs)]
                        output_list.append(cs)
                    print '\t' + str(output_list)
                elif opposed.has_key(cs) and opposed[cs] in output_list:
                    #kk = output_list.index(opposed[cs])
                    #if kk == 0:
                    output_list = []
                    #else:
                    #    output_list = output_list[0:kk]
                    print '\t' + str(output_list)
                else:
                    output_list.append(cs)
                    print '\t' + str(output_list)
        print >>output, "Case #%d: [%s]" % (i+1,', '.join(output_list))
        
