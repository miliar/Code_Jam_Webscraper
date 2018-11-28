f=open("C-small-attempt0.in","r")
lines=f.readlines()
i=0
title ="welcome to code jam"
N=int(lines[i])
for ii in range(N):
    i=i+1
    lt=19
    poss=[[] for x in range(19)]
    pose=[[] for x in range(19)]
    line=lines[i].strip()
    lw=len(line)
    for qpos,q in enumerate(title):
       for ipos,let in enumerate(line):
          if q==let:
             poss[qpos].append(ipos)
             pose[qpos].append(ipos)
    ll=2
    while lt>1:
       if round(lt/2-0.1)*2==lt:
          w_odd=False
          lt=round(lt/2-0.1)
       else:
          w_odd=True
          lt=round(lt/2-0.1)+1
       poss_n=[[] for x in range(lt)]
       pose_n=[[] for x in range(lt)]
       for w in range(lt):
          w2=w*2
          if w_odd==True and w==lt-1:
             poss_n[w]=poss[w2]
             pose_n[w]=pose[w2]
          else:
             ws=w2
             we=w2+1
             for iposs,ipose in zip(poss[ws],pose[ws]):
                for jposs,jpose in zip(poss[we],pose[we]):
                   if ipose<jposs:
                      poss_n[w].append(iposs)
                      pose_n[w].append(jpose)
       poss=poss_n
       pose=pose_n
    ans=str(len(poss_n[0]))
    ans=ans[-4:]
    for x in range(4-len(ans) ):
       ans="0"+ans
    output="Case #"+ str(ii+1)+": "+ans
    print output
f.close()
