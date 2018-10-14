def solve(state,k):
    ret=0
    while state:
        tmp=str(state)
        if state[0]=='+':
            state=state.replace('+','',1)
        else:
            if len(state) < k:return 'IMPOSSIBLE'
            state=flip(state,k)
            state=remove(state,k)
            ret+=1
        if tmp == state:return 'IMPOSSIBLE'
    return ret
def flip(state,k):
    tmp=''
    for a in range(k):
        if state[a] == '+':tmp+='-'
        else:tmp+='+'
    return tmp+state[k:]
def remove(state,k):
    for _ in range(k):
        if state[0]=='-':return state
        else:state=state.replace('+','',1)
    return state


t=int(input())
for i in range(1,t+1):
    state,k=input().split(' ')
    k=int(k)
    print('Case #{0}: {1}'.format(i,solve(state,k)))
