import sys

nodes = [0]
dp = {}

def manipulate(pos):
      if type(nodes[pos]) == type((1,)):
            if nodes[pos][0] == 1:
                  return (manipulate(pos*2) and manipulate(pos*2+1))
            else:
                  return (manipulate(pos*2) or manipulate(pos*2+1))
      else:
            return nodes[pos]

def findmin(pos,ach):
      temp = (pos,ach)
      if dp.has_key((pos,ach)):
            return dp[(pos,ach)]
      if manipulate(pos)==ach:
            dp[temp] = 0
            return dp[temp]
      else:
            if type(nodes[pos]) == type((1,)):
                  ret1 = 0
                  if nodes[pos][0]==1 and ach==1:
                        if manipulate(pos*2)!=1:
                              ret1+=findmin(pos*2,1)
                        if manipulate(pos*2+1)!=1:
                              ret1+=findmin(pos*2+1,1)
                  elif nodes[pos][0]==1 and ach==0:
                        t1 = findmin(pos*2,0)
                        t2 = findmin(pos*2+1,0)
                        ret1+=min(t1,t2)
                  elif nodes[pos][0]==0 and ach==1:
                        t1 = findmin(pos*2,1)
                        t2 = findmin(pos*2+1,1)
                        ret1+=min(t1,t2)
                  elif nodes[pos][0]==0 and ach==0:
                        if manipulate(pos*2)!=0:
                              ret1+=findmin(pos*2,0)
                        if manipulate(pos*2+1)!=0:
                              ret1+=findmin(pos*2+1,0)
                  
                  if nodes[pos][1]==1:
                        ret2 = 1
                        if nodes[pos][0]==0 and ach==1:
                              if manipulate(pos*2)!=1:
                                    ret2+=findmin(pos*2,1)
                              if manipulate(pos*2+1)!=1:
                                    ret2+=findmin(pos*2+1,1)
                        elif nodes[pos][0]==0 and ach==0:
                              t1 = findmin(pos*2,0)
                              t2 = findmin(pos*2+1,0)
                              ret2+=min(t1,t2)
                        elif nodes[pos][0]==1 and ach==1:
                              t1 = findmin(pos*2,1)
                              t2 = findmin(pos*2+1,1)
                              ret2+=min(t1,t2)
                        elif nodes[pos][0]==1 and ach==0:
                              if manipulate(pos*2)!=0:
                                    ret2+=findmin(pos*2,0)
                              if manipulate(pos*2+1)!=0:
                                    ret2+=findmin(pos*2+1,0)
                  else:
                        ret2=100000000
                  dp[temp] = min(ret1,ret2)
                  return dp[temp]
            else:
                  dp[temp] = 100000000
                  return dp[temp]
      

sys.stdin = open("Al.in","r")
sys.stdout = open("Al.out","w")

cases = int(raw_input().strip())
for T in xrange(cases):
      nodes = [0]
      dp = {}
      M,V = (int(i) for i in raw_input().strip().split())


      for i in xrange((M-1)/2):
            t1,t2 = (int(i) for i in raw_input().strip().split())
            nodes.append((t1,t2))
      
      for i in xrange((M+1)/2):
            t1 = int(raw_input().strip())
            nodes.append(t1)
      ans = findmin(1,V)
      if ans > M:
            ans = "IMPOSSIBLE"
      else:
            ans = str(ans)
      print "Case #%s: %s" % (str(T+1),ans)

sys.stdin.close()
sys.stdout.close()
