def stalling((N,K,index)):
    if K==0:
        return index,str(long(N))+' '+str(long(0))
    if K==1:
        return index,str(long(np.ceil((N-1.)/2.)))+' '+str(long(np.floor((N-1.)/2.)))

    pow2 = long(0)
    pow_sum = long(2**pow2)
    while pow_sum<K:
        pow2+=long(1)
        pow_sum+=long(2**pow2)
    next_pow_sum = long(pow_sum)
    pow_sum-=long(2**pow2)

    #print pow2,pow_sum,next_pow_sum
    possibilities = []
    G = long(pow2)
    for idx in range(1,long(2**G+1)):
        operations = ('{:0'+str(G)+'b}').format(2**G-idx)

        # now just nest the operations
        curr_N = long(N)
        for o in operations:
            if o=='1':
                curr_N = long(np.ceil((curr_N-1.)/2.))
            else:
                curr_N = long(np.floor((curr_N-1.)/2.))
            if curr_N<=1:
                curr_N = 1

        possibilities.append(str(long(np.ceil((curr_N-1.)/2.)))+' '+str(long(np.floor((curr_N-1.)/2.))))
    possibilities = sorted(possibilities,reverse=True)
    output = possibilities[long(K-pow_sum-1)]
    return index,output

from multiprocessing import Pool
def solveAll(filename='test1.txt',output_filename='out1.txt',num_threads=62):
    input_data = open(filename).read().split('\n')
    number_of_problems = int(input_data[0])
    output_data = range(number_of_problems)
    input_data1 = [long(n.split()[0]) for n in input_data[1:-1]]
    input_data2 = [long(n.split()[1]) for n in input_data[1:-1]]
    input_data = zip(input_data1,input_data2,range(number_of_problems))
    print input_data
    print number_of_problems,len(input_data)

    pool = Pool(processes=num_threads)
    for i,out in enumerate(pool.imap_unordered(stalling,input_data)):
        print i,out
        output_data[out[0]] = 'Case #'+str(out[0]+1)+': '+str(out[1])

    open(output_filename,'w').write('\n'.join(output_data))