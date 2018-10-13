from multiprocessing import Pool

def read_array(convertor=None):
    ret = raw_input().split()
    if convertor: ret = map(convertor, ret)
    return ret

#======================== BOF  =============================#

def solver(data_container):
    C, F, X = data_container.C, data_container.F, data_container.X

    now = 0
    rate = 2.0
    best = X / rate
    while now < best:
        buy_new_time = C / rate
        now += buy_new_time
        rate += F
        best = min(best, now + X / rate)

    return '%.7f' % best

    pass # return result as string


class DataContainer:
    def __init__(self):
        self.C, self.F, self.X = read_array(float)
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
