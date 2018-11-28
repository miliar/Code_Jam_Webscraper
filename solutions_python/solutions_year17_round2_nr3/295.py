#!/usr/local/bin/pypy3

import sys, io, types, os, time, concurrent.futures, multiprocessing, heapq as hpq
import math, decimal as dec, collections as coll, itertools as itt, fractions as fr, pickle, functools as fts



def dijkstra(matrix, start, end):
    '''
    :param matrix:
    edges = [
        [None, 2, 3],
        [2, None, 5],
        [3, 5, None]
    ]
    :param start:
    :param end:
    :return: time + path
    '''
    g = coll.defaultdict(list)
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] != -1:
                g[i].append((matrix[i][j], j))

    global hs
    cities = [{ind: (hs[ind][0], hs[ind][1], 0)} for ind in range(len(hs)) ]

    q = [(0, start, ())]
    while q:
        (time_, v1, path) = hpq.heappop(q)
        # if v1 not in seen:
        #     seen.add(v1)
        path = (v1, path)
        # if v1 == end:
        #     # TODO: calc finish time
        #     return (time, path)

        start_hs = cities[v1]
        for dist, v2 in g.get(v1, ()):
            # if v2 not in seen:
                # TODO Move horses

            # Can I get there? Update horses
            ride = False
            fastest_time = float('inf')
            for hs_name, hs_attr in start_hs.items():
                if dist <= hs_attr[0]:
                    existing_hourse = cities[v2].get(hs_name)


                    if hs_attr[0] == hs[hs_name][0]:
                        # New horse
                        timings = [ h[2] for h in start_hs.values() if h[2]>0 ]
                        if len(timings) > 0:
                            time = min( timings )
                        else:
                            time = hs_attr[2]
                    else:
                        time = hs_attr[2]

                    if existing_hourse:
                        if existing_hourse[0] > hs_attr[0]-dist or existing_hourse[2] > time + dist/hs_attr[1]:
                            cities[v2][hs_name] = (hs_attr[0]-dist, hs_attr[1], time + dist / hs_attr[1])
                            ride = True
                            fastest_time = min(fastest_time, time + dist / hs_attr[1])
                    else:
                        cities[v2][hs_name] = (hs_attr[0] - dist, hs_attr[1], time + dist / hs_attr[1])
                        ride = True
                        fastest_time = min(fastest_time, time + dist / hs_attr[1])

            if ride:
                hpq.heappush(q, (fastest_time, v2, path))

    return min( [ h[2] for h in cities[end].values() if h[2]>0 ])


def code_here(_cc, _DEBUG, _data):
    global DEBUG
    DEBUG = _DEBUG
    dd = Data(_data)

    global hs
    hs = dd.horses

    res = []

    for dest in dd.dest:
        res.append( dijkstra(dd.m, dest[0]-1, dest[1]-1) )

    return ' '.join([ '{0:.7f}'.format(r) for r in res ])


def read_data(_T):
    for _cc in range(_T):
        N, Q = map(int, input().split())

        horses = []
        for _i in range(N):
            horses.append(list(map(int, input().split()))) # e, s

        m = []
        for _i in range(N):
            m.append(list(map(int, input().split())))

        dest = []
        for _i in range(Q):
            dest.append(list(map(int, input().split())))

        yield {k: v for k, v in locals().items() if k not in ["sys", "__builtins__", "_cc", "_T", "_i"]}


#<editor-fold defaultstate="collapsed" desc="GCJ init">

class Data(object):
    def __init__(self, dd):
        self.__dict__ = dd
        
_MAX_WORKERS = multiprocessing.cpu_count() - 1

def iterations(_outfile=None):
    _T = int(input())
    _tt = max(_T // 20, 1)

    _start_time = time.time()

    with concurrent.futures.ProcessPoolExecutor(max_workers=_MAX_WORKERS) as executor:
        map_func = map if DEBUG else executor.map

        _iterator = map_func(code_here, range(_T), itt.repeat(DEBUG, _T), read_data(_T))

        for _cc, res in zip(range(_T), _iterator):
            if _cc % _tt == 0:
                _time_diff = int((time.time() - _start_time) / (_cc + 1) * _T)
                print('Solving: ', (_cc + 1) * 100 // _T, '%',
                      'Estimated running:', '{}m {}s'.format(*divmod(_time_diff, 60)),
                      file=sys.stderr)

            if isinstance(res, list): 
                if DEBUG: print('Case #{}:'.format(_cc + 1))
                print('Case #{}:'.format(_cc + 1), file=_outfile)

                for _r in res:
                    if DEBUG: print(_r)
                    print(_r, file=_outfile)
            else:
                if DEBUG: print('Case #{}:'.format(_cc + 1), res)
                print('Case #{}:'.format(_cc + 1), res, file=_outfile)


def main():
    global DEBUG

    # Read input and prepare output
    _in = get_input_file()
    with open(_in, 'r') as _infile:
        sys.stdin.close()
        sys.stdin = _infile

        i = 0  # Do not overwrite existing files
        while os.path.isfile(_in + '.{}.out'.format(i)):
            i += 1

        print('', file=sys.stderr)
        if DEBUG: print('*** Running in DEBUG mode ***', file=sys.stderr)
        print('<<<', _in, '<<<', file=sys.stderr)
        print('>>>', _in + '.{}.out'.format(i), '>>>', file=sys.stderr)
        print('', file=sys.stderr)

        with open(_in + '.{}.out'.format(i), 'w') as _outfile:
            iterations(_outfile)

def get_input_file():
    global DEBUG
    
    # If file name is supplied via arguments – take it
    if len(sys.argv) > 1:
        _tmp = os.path.dirname(os.path.realpath(__file__)) + '/' + sys.argv[1]
        if os.path.isfile(_tmp):
            DEBUG, _in = len(sys.argv) > 2, _tmp
        else:
            DEBUG, _in = True, find_last_modified_file()
    else:
        DEBUG, _in = False, find_last_modified_file()
        # Debugging in PyCharm detection
        if "PYCHARM_HOSTED" in os.environ:
            try:
                import pydevd
                pycharm_debugging = True
            except ImportError:
                pycharm_debugging = False

            DEBUG = pycharm_debugging

    return _in

def find_last_modified_file(suffix='.in', subfolder=''):
    """
    Find the most recently modified *.in file (aka freshly downloaded input)
    in the *SAME* folder as the script
    :return: file path
    """
    _in = (0, None)
    _folder_path = os.path.dirname(os.path.realpath(__file__)) + subfolder  + '/'
    for _file in os.listdir(_folder_path):
        if _file.endswith(suffix):
            last_modified = os.path.getmtime(_folder_path + _file)
            if _in[0] < last_modified:
                _in = (last_modified, _folder_path + _file)
    if _in[1] == None:
        raise Exception('No input file is found :/')
    return _in[1]
    
#</editor-fold>

if __name__ == "__main__":
    main()