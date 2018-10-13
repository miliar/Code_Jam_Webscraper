#!/usr/bin/env python
#coding=utf-8

problem = 'bb'
input_file_name = problem + ".in"
output_file_name = problem + ".out"
test_data = """5
3 3
9 6 3
5 9 6
3 5 9
1 10
0 1 2 3 4 5 6 7 8 7
2 3
7 6 7
7 6 7
5 5
1 2 3 4 5
2 9 3 9 6
3 3 0 8 7
4 9 8 9 8
5 6 7 8 9
2 13
8 8 8 8 8 8 8 8 8 8 8 8 8
8 8 8 8 8 8 8 8 8 8 8 8 8
"""
test_data = None

def process(input):
    output = []
    iLine = 0
    N = int(input[iLine].strip())
    iLine += 1
    
    for case in range(1, N + 1):
        print "Case %d"%case
        
        ##########################
        # Get source data here
        H, W = map(lambda x: int(x), input[iLine].strip().split())
        iLine += 1
        b = []
        for h in range(H):
            b.append(map(lambda x: int(x), input[iLine].strip().split()))
            iLine += 1
            
                

        ##########################
        # Solve the case here
        result = []
        
        bb = [[]]*H*W
        sink = 0
        for h in range(H):
            for w in range(W):
                mina = 10000
                minh,minw = -1,-1
                if h > 0 and mina > b[h-1][w]:
                    minh,minw = h-1,w
                    mina = b[minh][minw]
                if w > 0 and mina > b[h][w-1]:
                    minh,minw = h,w-1
                    mina = b[minh][minw]
                if w < W-1 and mina > b[h][w+1]:
                    minh,minw = h,w+1
                    mina = b[minh][minw]
                if h < H-1 and mina > b[h+1][w]:
                    minh,minw = h+1,w
                    mina = b[minh][minw]
                                    
#                print minh,minw
                if b[h][w] > mina:
                    bb[h*W+w] = [minh,minw,-1]
                else:
                    bb[h*W+w] = [-1,-1,sink]
                    sink += 1
                    
        for i in range(H*W):
            ss = []
            j = i
            while -1==bb[j][2]:
                ss.append(bb[j])
                j = bb[j][0]*W+bb[j][1]
            while ss != []:
                e = ss.pop(-1)
                e[2] = bb[j][2]
        
        dd = {}
        c = ord('a')
        for h in range(H):
            rslt = []
            for w in range(W):
                e = bb[h*W+w]
#                print (e[0],e[1]),
                if e[2] not in dd:
                    dd[e[2]] = chr(c)
                    c+=1
                rslt.append(dd[e[2]])
            result.append(" ".join(rslt))
#            print
                
                    
        
        output.append(result)
        ##########################
        
        
    return output

def main():
    input = None
    if test_data is None:
        ifile = open(input_file_name)
        input = ifile.readlines()
        ifile.close()
    else:
        input = test_data.split('\n')
        
    output = process(input)
    
    if test_data is None:
        ofile = open(output_file_name, 'w')
        for i in range(len(output)):
            print >> ofile, "Case #%d:"%(i + 1)
            for line in output[i]:
                print >> ofile, line
        ofile.close()
    for i in range(len(output)):
        print "Case #%d:"%(i + 1)
        for line in output[i]:
            print line
        
    return len(output)
        
if __name__ == "__main__":
    import time
    start = time.time()
    N = main()
    print "Done in %f seconds"%(time.time() - start)
    print "Average %f milliseconds"%((time.time() - start) * 1000 / N)
    
