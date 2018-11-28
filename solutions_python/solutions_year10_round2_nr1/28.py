import sys

def num_mkdirs(existing_paths, wanted_paths):
    
    existing_directories = {'/': True}
    for path in existing_paths:
        nodes = path.split('/')[1:]
        tree = ''
        for node in nodes:
            tree += '/' + node
            existing_directories[tree] = True
    
    count = 0
    
    for path in wanted_paths:
        nodes = path.split('/')[1:]
        tree = ''
        for node in nodes:
            tree += ('/' + node)
            if tree not in existing_directories:
                count += 1
                existing_directories[tree] = True
                
    return count


if __name__ == '__main__':
    ntests = int(sys.stdin.readline())
    for i in range(1, ntests+1):
        N, M = map(int, sys.stdin.readline().split())
        wanted_paths = []
        existing_paths = []
        for j in range(N):
            existing_paths.append(sys.stdin.readline().strip())
        for j in range(M):
            wanted_paths.append(sys.stdin.readline().strip())
        ans = num_mkdirs(existing_paths, wanted_paths)
        print 'Case #%s: %s' %  (i, ans)
