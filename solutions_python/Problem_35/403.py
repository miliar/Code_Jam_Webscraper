import sys

import networkx as nx


def generate_network(l, ncol):
    n = ncol
    G = nx.Graph()
    
    number = 0
    for item in l:
        G.add_node(number, alt=item)
        number += 1
        
    for i in range(len(l)):
        flow = i
        low = G.node[i]['alt']
        if i % n == 0:
            neighbors = [i - n, i + 1, i + n]
        elif i % n == n - 1:
            neighbors = [i - n, i - 1, i + n]
        else:
            neighbors = [i - n, i - 1, i + 1, i + n]
            
        for neighbor in neighbors:
            if neighbor < 0 or neighbor >= len(l):
                continue
            if G.node[neighbor]['alt'] < low:
                flow = neighbor
                low = G.node[neighbor]['alt']
                
        if flow != i:
            G.add_edge(i, flow)
                
    return G


def asign_letter(G):
    letters = dict()
    small = dict()
    graphs = list(nx.connected_component_subgraphs(G))
    for g in graphs:
        tmp = g.nodes()            
        small[min(tmp)] = tmp
        
    small_key = small.keys()
    small_key.sort()
    
    START = 97
    for s in small_key:
        l = small[s]
        for i in l:
            letters[i] = chr(START)
            
        START += 1
    
    return letters
        

if __name__  == '__main__':
    import psyco
    psyco.full()
    
    in_file = sys.argv[1]
    
    rfile = open(in_file)    
    rfile.readline()
    
    wfile = open('result_b.txt', 'w')
    case = 0
    
    lines = rfile.readlines()
    while lines:
        case += 1
        m, n = lines[0].strip().split()
        lines = lines[1:]
        m = int(m)
        n = int(n)
        
        l = lines[0:m]
        lines = lines[m:]
        
        tmp = list()
        for line in l:
            for i in line.strip().split():
                tmp.append(int(i))
                
        G = generate_network(tmp, n)
        letters = asign_letter(G)
        
        wfile.write('Case #'+str(case)+':'+'\n')
        out = ''
        for i in range(m * n):
            out += letters[i] 
            if i % n == n - 1:
                out += '\n'
                continue
            
            out += ' '
        wfile.write(out)
    wfile.close()
        
    
    
    
    
    
    
    
    
# END