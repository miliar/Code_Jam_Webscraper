def solve(paths, create):

    def exists(p):
        return any(x.startswith(p + '/') or x == p for x in paths)
    
    total = 0
    for p in create:
        names = p.split('/')[1:]
        path = ''
        while names:
            path += '/' + names[0]
            if not exists(path):
                total += 1
                paths.append(path)
            names = names[1:]
        
    return total
    
def main():
    file = open('A-large.in')
    output = open('output.txt', 'w')
    tests = int(file.readline().strip())
    for case in range(1, tests + 1):
        N, M = [int(x) for x in file.readline().split()]
        paths = [file.readline().strip() for i in range(N)]
        create = [file.readline().strip() for i in range(M)]
        print >> output, 'Case #%d:' % case, solve(paths, create)
    output.close()
    
if __name__ == '__main__':
    main()
    
