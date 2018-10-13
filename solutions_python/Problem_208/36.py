import numpy as np
import networkx as nx

input_file = 'C-large.in'
output_file = 'C.out'

with open(input_file) as f:
    with open(output_file, 'w') as out:
        cases = f.readline()
        cases = int(cases)
        for i in xrange(1, cases+1):
            n, q = map(int, f.readline().split())
            horses = [map(int, f.readline().split()) for j in range(n)]  # stamina speed
            graph = [map(int, f.readline().split()) for jj in range(n)]
            stops = np.array([map(int, f.readline().split()) for jjj in range(q)])-1
            graph = np.asmatrix(graph)
            graph[graph == -1] = 0
            g = nx.from_numpy_matrix(graph, create_using=nx.DiGraph())
            rr = nx.floyd_warshall_numpy(g)
            rr[rr == 0] = np.inf
            rr0 = np.zeros_like(rr)
            for ii in range(n):
                x = rr[ii]
                x[x > horses[ii][0]] = np.inf
                x = x/horses[ii][1]
                rr0[ii] = x
            gg = nx.from_numpy_matrix(rr0, create_using=nx.DiGraph())
            # now queries
            res = ' '.join(map(str, [nx.shortest_path_length(gg, source=q, target=w, weight='weight') for q, w in stops]))
            print 'Case #{i}: {z}'.format(z=res, i=i)
            out.write('Case #{i}: {z}\n'.format(z=res, i=i))