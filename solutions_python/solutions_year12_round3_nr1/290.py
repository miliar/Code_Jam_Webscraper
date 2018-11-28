in_data = open('A-small-attempt1.in').readlines()
T=in_data[0]
in_data=in_data[1:]
outfile = open('res', 'w')
case_no = 0

def find_path(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    if not graph.has_key(start):
        return None
    for node in graph[start]:
        if node not in path:
            newpath = find_path(graph, node, end, path)
            if newpath: return newpath
    return None

def find(n, dag):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if i==j:
                continue
            tmp = find_all_paths(dag, i, j)
            if len(tmp) >=2:
                return 'Yes'
    
    return 'No'            

def find_all_paths(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return [path]
    if not graph.has_key(start):
        return []
    paths = []
    for node in graph[start]:
        if node not in path:
            newpaths = find_all_paths(graph, node, end, path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths


while len(in_data) > 0:
    case_no += 1
    n = int(in_data[0].strip())
    in_data = in_data[1:]
    lev = in_data[:n]
    in_data = in_data[n:]
    if n==1:
        res = 'No'
        out = 'Case #' + str(case_no) + ': ' + str(res) + '\n'
        outfile.write(out)
        continue
    
    
    dag = dict()
    for i in range(1, n+1):
        tmp = lev[i-1].strip().split()
        tmp = tmp[1:]
        dag[i] = []
        for k in tmp:
            dag[i].append(int(k))
    
    res = find(n, dag)


    out = 'Case #' + str(case_no) + ': ' + str(res) + '\n'
    outfile.write(out)        

outfile.close()    