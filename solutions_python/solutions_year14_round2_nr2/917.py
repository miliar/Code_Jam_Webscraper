with open('lotterySmall.in') as infile:
    content = infile.readlines()
    for i in range(0, int(content[0])):
        [A, B, K] = [int(j) for j in content[i+1].split(' ')]
        count = 0;
        for ja in range(0, A):
        	for jb in range(0, B):
        	    count += 1 if( ja&jb < K )else 0
        print('Case #{0}: {1}'.format(str(i+1), str(count)))
