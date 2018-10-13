
def gen_vertices(n, A, B, C, D, x0, y0, M):
    vertices = []
    X = x0
    Y = y0
    vertices.append((X, Y))
    for i in xrange(1,n):
        X = (A * X + B) % M
        Y = (C * Y + D) % M
        vertices.append((X, Y))
    return vertices

def solve_case(vertices):
    num_triangles = 0
    for i in xrange(len(vertices)):
        for j in xrange(i + 1, len(vertices)):
            for k in xrange(j + 1, len(vertices)):
                x_remain = (vertices[i][0] + vertices[j][0] + vertices[k][0]) % 3
                y_remain = (vertices[i][1] + vertices[j][1] + vertices[k][1]) % 3
                if x_remain == 0 and y_remain == 0:
                    num_triangles += 1
    return num_triangles
    
def solve(filename, output):
    lines = file(filename).readlines()
    out = file(output, 'w')
    num_cases = int(lines[0])
    index = 1
    for i in xrange(num_cases):
        data = gen_vertices(*map(int, lines[index].split(' ')))
        index += 1
        res = solve_case(data)
        out.write("Case #%i: %i\n" % (i + 1, res))


import sys
solve(sys.argv[1],sys.argv[2])

            
        
        
