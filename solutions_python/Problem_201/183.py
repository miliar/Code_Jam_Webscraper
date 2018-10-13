T = int(input())
for kase in range(T):
  N,K = map(int,input().split())
  X = [N] #Queue
  CntMap = {N:1} #CntMap

  def upload(sz,add):
    if not sz in CntMap.keys():
      X.append(sz)
    CntMap[sz] = CntMap.get(sz,0) + add

  for sz in X:
    cnt = CntMap[sz]
    #print('###',sz,cnt)
    if cnt >= K:
      print("Case #%d: %d %d" % (kase+1,sz//2,(sz-1)//2))
      break
    K -= cnt
    upload(sz//2, cnt)
    upload((sz-1)//2, cnt)
