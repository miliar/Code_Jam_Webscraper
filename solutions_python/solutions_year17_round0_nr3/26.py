def attempt(n, m):
    state = {n:1}
    while True:
        mk = sorted(state.keys())[-1]
        mv = state[mk]
        sk2 = (mk-1)//2
        sk1 = mk-1-sk2
        if(m <= mv):
            return sk1, sk2
        m-=mv
        state.pop(mk)
        state[sk1]=state.get(sk1, 0)+mv
        state[sk2]=state.get(sk2, 0)+mv
        #print(m, state)
cnt=int(input())
for i in range(1, cnt + 1):
  n, m = input().split(' ')
  n, m = attempt(int(n),int(m))
  print("Case #{}: {} {}".format(i, n, m))