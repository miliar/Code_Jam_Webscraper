import sys

def possible_design(lawn, n, m):
    possible = [[False for i in range(m)] for j in range(n)]
    for i in range(n):
        line = lawn[i]
        highest = max(line)
        for j in range(m):
            if line[j] == highest:
                possible[i][j] = True

    for j in range(m):
        line = [row[j] for row in lawn]
        highest = max(line)
        for i in range(n):
            if line[i] == highest:
                possible[i][j] = True
    possible = sum(possible,[])
    return all(x == True for x in possible)

def main():
    filename = sys.argv[1]
    file = open(filename,'r')
    cases = int(file.readline())
    for case_num in range(cases):
        params = file.readline().strip().split(' ')
        N = int(params[0])
        M = int(params[1])
        lawn = []
        for i in range(N):
            lawn.append( map(int, file.readline().strip().split(' ')) )
        print "Case #%d: %s" % (case_num+1, "YES" if possible_design(lawn, N, M) else "NO") 
    file.close()
    
if __name__ == '__main__':
    main()