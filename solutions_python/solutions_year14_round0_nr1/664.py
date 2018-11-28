from multiprocessing import Pool

def read_array(convertor=None):
    ret = raw_input().split()
    if convertor: ret = map(convertor, ret)
    return ret

#======================== BOF  =============================#

def solver(data_container):
    set1 = set(data_container.matrix1[data_container.row1])
    set2 = set(data_container.matrix2[data_container.row2])
    intersect = set1 & set2
    if len(intersect) == 1:
        return str(list(intersect)[0])
    elif len(intersect) == 0:
        return 'Volunteer cheated!'
    else:
        return 'Bad magician!'

    pass # return result as string


class DataContainer:
    def __init__(self):
        self.row1 = input() - 1
        self.matrix1 = [read_array() for _ in range(4)]
        self.row2 = input() - 1
        self.matrix2 = [read_array() for _ in range(4)]
        pass # read data

#======================== EOF  =============================#


if __name__ == '__main__':
    NUM_THREAD = 2
    pool = Pool(NUM_THREAD)
    T = input()
    input_queue = [DataContainer() for _ in xrange(T)]
    result = pool.map(solver, input_queue)

    for i in range(T):
        print 'Case #%d: %s' % (i+1, result[i])
    #'\n'.join(map(lambda i: 'Case #%d: %s' % (i+1, result[i]), range(T)))
