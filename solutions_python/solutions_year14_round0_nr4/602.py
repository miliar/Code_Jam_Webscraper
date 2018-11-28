from multiprocessing import Pool

def read_array(convertor=None):
    ret = raw_input().split()
    if convertor: ret = map(convertor, ret)
    return ret

#======================== BOF  =============================#

def wins(a, b):
    n = len(a)
    ai = 0
    bi = 0
    wincnt = 0
    while ai < n and bi < n:
        if a[ai] > b[bi]:
            wincnt += 1
            ai += 1
            bi += 1
        else:
            bi += 1
    return wincnt


def solver(data_container):
    n = data_container.n
    naomi = data_container.naomi
    ken = data_container.ken
    naomi.sort(reverse=True)
    ken.sort(reverse=True)

    deceive = wins(naomi, ken)
    war = n - wins(ken, naomi)
    return '%d %d' % (deceive, war)
    pass # return result as string


class DataContainer:
    def __init__(self):
        self.n = input()
        self.naomi = read_array(float)
        self.ken = read_array(float)
        pass # read data

#======================== EOF  =============================#


if __name__ == '__main__':
    NUM_THREAD = 2
    USE_MULTI = False

    T = input()
    input_queue = [DataContainer() for _ in xrange(T)]
    
    if USE_MULTI:
        pool = Pool(NUM_THREAD)
        result = pool.map(solver, input_queue)
    else:
        result = []
        for i in xrange(T):
            result.append(solver(input_queue[i]))

    for i in range(T):
        print 'Case #%d: %s' % (i+1, result[i])
