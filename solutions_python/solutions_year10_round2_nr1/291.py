from m_util import *

T = int(raw_input())

for c in range(1, T + 1):   
        N, M = map(int, raw_input().split())
        #print N,K
        root={}
        
        for i in range(N):
            node = root
            input = raw_input().split('/')[1:]            
            for j in input:                
                if(j not in node):
                    node[j] = {}                    
                node = node[j]
        
        
        #print "mid", root        
        
        create = 0
        for i in range(M):
            node = root
            input = raw_input().split('/')[1:]            
            for j in input:
                if(j not in node):
                    node[j] = {}
                    create += 1
                    #print root
                node = node[j]
                         
        print "Case #%d: %s" % (c, create)
    