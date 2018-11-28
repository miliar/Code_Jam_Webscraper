from multiprocessing import Pool



def findLastWord((S,j)):
    lastword = [S[0]]

    for i,s in enumerate(list(S)[1:]):
        if s<lastword[0]:
            lastword.append(s)
        else:
            lastword.insert(0,s)

    return j,''.join(lastword)





def solveAll(filename='lastword.test',output_filename='lastword.test.out',num_threads=20):
    input_data = open(filename).read().split('\n')
    print input_data
    number_of_problems = int(input_data[0])
    print number_of_problems
    input_data = input_data[1:-1]
    print input_data
    output_data = range(number_of_problems)
    pool = Pool(processes=num_threads)
    for i, status in enumerate(pool.imap_unordered(findLastWord, zip(input_data,range(1,number_of_problems+1)))):
        print i,status
        output_data[status[0]-1] = 'Case #'+str(status[0])+': '+status[1]

    print output_data
    open(output_filename,'w').write('\n'.join(output_data))