
def cut_grass(count):
    indexes = raw_input()
    n,m = indexes.split(' ')
    n = int(n)
    m = int(m)
    set_lawn = [0]*n
    test_lawn = [[100]*m]*n
    for i in range(0, n):
        set_lawn[i] = raw_input().split(' ')
        max_height = int(set_lawn[i][0])
        for j in range(0, m):
            if max_height < int(set_lawn[i][j]):
                max_height = int(set_lawn[i][j])
        test_lawn[i] = [max_height]*m
    for i in range(0, m):
        max_height = int(set_lawn[0][i])
        for j in range(0,n):
            if max_height < int(set_lawn[j][i]):
                max_height = int(set_lawn[j][i])
        for j in range(0,n):
            test_lawn[j][i] = min(max_height, test_lawn[j][i])
    for i in range(0, n):
        for j in range(0,m):
            if not test_lawn[i][j] == int(set_lawn[i][j]):
                print "Case #{}: NO".format(count)
                return
    print "Case #{}: YES".format(count)
        
count = input()
for i in range(1, count+1):
    cut_grass(i)
