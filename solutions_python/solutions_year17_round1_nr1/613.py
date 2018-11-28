def solve(state,r,c):
    for i in range(r):
        if len(set(state[i])) == 2 and '?' in state[i]:
            char=[x for x in state[i] if x != '?'][0]
            for j in range(c):
                state[i][j]=char
        elif len(set(state[i])) >= 3 and '?' in state[i]:
            char=[x for x in state[i] if x != '?']
            j=0
            for ch in char:
                while j < c and (state[i][j] == ch or state[i][j] == '?'):
                    state[i][j]=ch
                    j+=1
    for i in range(c):
        tmp=[state[j][i] for j in range(r)]
        if len(set(tmp)) == 2 and '?' in tmp:
            char=[state[j][i] for j in range(r) if state[j][i] != '?'][0]
            #print('ck,',char)
            for j in range(r):
                state[j][i]=char
        elif len(set(tmp)) >= 3 and '?' in tmp:
            char=[state[j][i] for j in range(r) if state[j][i] != '?']
            #print('ck,',char)
            j=0
            for ch in char:
                while j < r and (state[j][i] == ch or state[j][i] == '?'):
                    state[j][i]=ch
                    j+=1
                
    return state 


t=int(input())
for a in range(1,t+1):
    r,c=[int(x) for x in input().split(' ')]
    state=[]
    for _ in range(r):
        state.append([x for x in input()])
    print('Case #{0}:'.format(a))
    ans=solve(state,r,c)
    for b in range(len(ans)):
        print(''.join(ans[b]))
        
        
