__author__ = 'sushrutrathi'

opt = open("output.txt", 'w')
with open("input.txt") as f:
    total_tests = int(f.readline())
    for tests in range(1,total_tests+1):
        n,r,o,y,g,b,v = [int(i) for i in f.readline().strip().split(' ')]

        arr = [[r,'R'],[y,'Y'],[b,'B']]
        arr = sorted(arr)

        if arr[2][0] > (arr[1][0]+arr[0][0]):
            opt.write("Case #" + str(tests) + ": " + "IMPOSSIBLE" + '\n')
        else:
            st = ""
            for i in range(arr[2][0]):
                st+= arr[2][1]

            ind = 0
            for i in range(arr[1][0]):
                st = st[0:i*2+1] + arr[1][1] + st[i*2+1:]
                m = len(st)
                ind+=1

            i = 0
            while(ind<arr[2][0]):
                st = st[0:ind*2+1] + arr[0][1] + st[ind*2+1:]
                i+=1
                ind+=1

            j=0
            while(i<arr[0][0]):
                st = st[0:j*3+1] + arr[0][1] + st[j*3+1:]
                i+=1
                j+=1


            opt.write("Case #" + str(tests) + ": " + st + '\n')