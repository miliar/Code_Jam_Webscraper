#!/usr/bin/env python
#coding=utf-8

import math

# input 
infilepath = "A-small-attempt0.in"
outfilepath = infilepath.replace(".in", ".out")

def do_case(infile):
    #parse
    n, A, B, C, D, X0, Y0, M = map(int, infile.readline().strip().split())
    
    X = X0
    Y = Y0
    print X, Y
    vertices = [(X, Y)]
    for i in range(1, n):
        X = (A*X + B) % M
        Y = (C*Y + D) % M
        vertices.append((X,Y))
        
    print vertices
    
    v_cnt = len(vertices)
    triangles = []
    for i in range(0, v_cnt-2):
        for j in range(i+1, v_cnt - 1):
            for k in range(j+1, v_cnt):
                triangles.append([ vertices[i], vertices[j], vertices[k] ])
                
    print len(triangles)
    
    answer = 0
    for tri in triangles:
        if ((tri[0][0] + tri[1][0] + tri[2][0]) % 3) == 0 and ((tri[0][1] + tri[1][1] + tri[2][1]) % 3 ) == 0:
            answer += 1
        
    return answer

def main():
    ifobj = file(infilepath)
    ofobj = file(outfilepath, "w")
        
    num_of_case = int(ifobj.readline().strip())
    print int(num_of_case)
    
    for i in range(num_of_case):
        answer = do_case(ifobj)
        
        str1 = "Case #%d: " % (i+1, ) + str(answer)
        print str1
        ofobj.write(str1)
        ofobj.write('\n')
        
    # release resource
    ifobj.close()
    ofobj.close()
    
if __name__ == "__main__":
    main()
