
def get_recycled(X, times):
    head = X%(10**times)
    tail = X/(10**times)
    recycle = head*(10**(len(str(tail))))+ tail
#    print X, head ,tail ,recycle
    return recycle

def get_all_recycled_pairs(X):
    for times in range(1,len(str(X))):
        recycle = get_recycled(X, times)
#        print X, recycle

def count_recycled_pairs(A,B):
    count = 0
    X_records = []
    pairs = []

    for X in range(A,B+1):
        if X not in X_records:
            for times in range(1,len(str(X))):
                recycle = get_recycled(X, times)


                if recycle > X and recycle <= B and recycle >= A and [X, recycle] not in pairs:
                    count += 1
                    X_records.append(X)
                    pairs.append([X, recycle])


#    print 'count: ', count
#    print len(list(set(zip(n_list,m_list))))
    return count


def recycled(filename, output_tag):
    f = open(filename, 'r')
    output= open(output_tag+'_output.txt','w')
    num_of_case = int(f.readline())
    for caseid in range(num_of_case):
        integers = f.readline().split('\n')[0].split()
        A, B = int(integers[0]),int(integers[1])
        num_of_pair = count_recycled_pairs(A, B)



        output.write('Case #'+str(caseid+1)+': '+str(num_of_pair)+'\n')

    f.close()
    output.close()

if __name__ == '__main__':

#    for letter in sorted(mapping):
#        print letter,': ', mapping[letter]
#    print len(mapping.keys())

    recycled('C-small-attempt0.in', 'recycled_small')
#    get_all_recycled_pairs(129)
#    count_recycled_pairs(1111, 2222)






  