tests = input()

for i in range(tests):
    data = map(int,raw_input().split())
    n = data[0] # number of Googlers
    s = data[1] # number of surprising triplets of scores
    p = data[2] # pass
    scores = [data[i] for i in range(3,n)]
    
    print data