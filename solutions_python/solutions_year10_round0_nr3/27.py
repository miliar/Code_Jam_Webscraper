T = int(raw_input())

for t in range(T):
 R, K, N = map(int, raw_input().split())
 g = map(int, raw_input().split())
 s = [0] * N
 sum = [0] * N
 for j in range(len(g)):
   k = (j+1) % N
   sum[j] = g[j]
   while k != j and sum[j]+g[k] <= K:
     sum[j] += g[k]
     k = (k+1) % N
   s[j] = k
 
 ord = [-1] * N
 psum = []
 cur = 0
 idx = 0
 ts = 0
 while ord[cur] == -1:
   ts += sum[cur]
   psum.append(ts)
   ord[cur] = idx
   cur = s[cur]
   idx += 1
 
 clen = idx - ord[cur]
 csum = psum[idx-1]
 if idx-clen > 0:
   csum -= psum[idx-clen-1]
 
 tot = 0
 if R <= idx:
   tot = psum[R-1]
 else:
   R -= idx-clen;
   tot = (R // clen)*csum
   if idx-clen+(R%clen):
     tot += psum[idx-clen+(R%clen)-1]

 print "Case #%d: %d" % (t+1, tot) 
 
