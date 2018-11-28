#
f = open("C-small.in","r")
fo = open("C-small.out","w")

lines = f.readlines()
i = 0
title ="welcome to code jam"
lt = 19
N = int(lines[i])
for icase in range(N):
      print(icase)
      i = i + 1
      lt = 19
      title ="welcome to code jam"
      words = lines[i].strip()
      lw = len(words)
      # set positions of each letter
      poss = [[] for x in range(19)]
      pose = [[] for x in range(19)]
      for qpos,q in enumerate(title):
            for ipos,let in enumerate(words):
                  if q == let:
                        poss[qpos].append(ipos)
                        pose[qpos].append(ipos)
      #print(pose)
      
      # search for 2 letters
      ll = 2
      while lt > 1:
            if round(lt/2-0.1)*2 == lt:
                  w_odd = False
                  lt = round(lt/2)
            else:
                  w_odd = True
                  lt = round(lt/2-0.1)+1
            poss_n = [[] for x in range(lt)]
            pose_n = [[] for x in range(lt)]
            for w in range(lt):
                  w2 = w*2
                  if w_odd == True and w == lt - 1:
                        poss_n[w] = poss[w2]
                        pose_n[w] = pose[w2]
                  else:
                        ws = w2
                        we = w2+1
                        for iposs,ipose in zip(poss[ws],pose[ws]):
                              for jposs,jpose in zip(poss[we],pose[we]):
                                    if ipose < jposs:
                                          poss_n[w].append(iposs)
                                          pose_n[w].append(jpose)
            poss = poss_n
            pose = pose_n
              
      ans = str(len(poss_n[0]))
      ans = ans[-4:]
      for x in range(4- len(ans) ):
            ans = "0" + ans
#      print(ans)
      print("Case #",icase+1,": ",ans,sep="")
      print("Case #",icase+1,": ",ans,sep="",file=fo)

#      print("Case #",icase+1,":",sep="",file=fo)

#            print( basin[ir][ic] for ic in range(c),sep=" ")
#      print("Case #",icase+1,": ",max_sat,sep="",file=fo)
f.close()
fo.close()
