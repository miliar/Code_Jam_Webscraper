T = int(input())
for t in range(1,T+1):
    N, R, O, Y, G, B, V = map(int,input().split())
    if B <= R >= Y:     
        ans = 'R'
        R -= 1
    elif R <= B >= Y:     
        ans = 'B'
        B -= 1      
    else:     
        ans = 'Y'
        Y -= 1
    for i in range(1, N):
        if ans[-1]=='R':
            if B == Y == 0:
                ans = 'IMPOSSIBLE'
                break
            if B > Y or (B==Y and ans[0] == 'B'):
                ans = ans + 'B'
                B -= 1   
            else:
                ans = ans + 'Y'
                Y -= 1
        elif ans[-1]=='B':
            if R == Y == 0:
                ans = 'IMPOSSIBLE'
                break
            if R > Y or (R == Y and ans[0] == 'R'):
                ans = ans + 'R'
                R -= 1   
            else:
                ans = ans + 'Y'
                Y -= 1
        else:
            if R == B == 0:
                ans = 'IMPOSSIBLE'
                break
            if R > B or (R == B and ans[0] == 'R'):
                ans = ans + 'R'
                R -= 1   
            else:
                ans = ans + 'B'
                B -= 1
  #      print(ans,R, B, Y)        
    if ans[0]==ans[-1]:
        ans = 'IMPOSSIBLE'
    print('Case #'+str(t)+':', ans)
        