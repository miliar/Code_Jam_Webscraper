'''
Created on May 22, 2011

@author: jagadeeshe
'''

def create_data_stream():
    from sys import stdin
    file_content = stdin.read()
    segs = file_content.split()
    segs.reverse()
    
    def read():
        return segs.pop()
    
    def readInt():
        return int(segs.pop())
        
    class _A(object): pass
    
    obj = _A()
    obj.read = read
    obj.readInt = readInt
    return obj


def codejam(solution):
    data_stream = create_data_stream()
    T = data_stream.readInt()
    for case in range(T):
        result = solution(data_stream)
        print "Case #%s: %s" % (case+1, result)



def square_tiles(data_stream):
    R = data_stream.readInt()
    C = data_stream.readInt()
    map = [[ x for x in data_stream.read()] for _ in range(R) ]

    def transform(r, c):
        if map[r][c] != '#': return
        if map[r][c+1] != '#' or map[r+1][c] != '#' or map[r+1][c+1] != '#': return
        map[r][c] = '/'
        map[r+1][c] = '\\'
        map[r][c+1] = '\\'
        map[r+1][c+1] = '/'

    def print_map():
        out = ''
        for row in map:
            s = '\n'
            for col in row:
                s += '%s' % col
            out += s
        return out
            
    for r in range(R-1):
        for c in range(C-1):
            transform(r, c)
    
    for r in range(R):
        for c in range(C):
            if map[r][c] == '#': return '\nImpossible'

    return print_map()


if __name__ == '__main__':
    codejam(square_tiles)
