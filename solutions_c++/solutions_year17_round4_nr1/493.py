
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <vector>
#include <utility>
#include <queue>
#include <stack>
#include <set>
#include <map>

using namespace std ; 

typedef long long ll ; 

int G[111] ; 

int dp[111][111][111] ; 

void sol(){
    int N, P ; 
    scanf("%d%d", &N, &P) ; 
    for(int i = 0 ; i != N ; i++)
        scanf("%d", &G[i]) ; 
    int ans = 0 ; 
    int stat[5] = {0} ; 
    for(int i = 0 ; i != N ; i++) {
        if(G[i] % P == 0) {
            ans++ ; 
            continue ; 
        }
        stat[G[i]%P]++ ; 
    }
    for(int i = 0 ; i <= stat[1] ; i++) 
        for(int j = 0 ; j <= stat[2] ; j++) 
            for(int k = 0 ; k <= stat[3] ; k++) 
                dp[i][j][k] = -1e+8 ; 
    dp[0][0][0] = 0 ; 
    for(int i = 0 ; i <= stat[1] ; i++) {
        for(int j = 0 ; j <= stat[2] ; j++) {
            for(int k = 0 ; k <= stat[3] ; k++) {
                if(i) 
                    dp[i][j][k] = max(dp[i][j][k], dp[i-1][j][k] + bool( ((i-1)*1+j*2+k*3)%P == 0 )) ; 
                if(j) 
                    dp[i][j][k] = max(dp[i][j][k], dp[i][j-1][k] + bool( (i*1+(j-1)*2+k*3)%P == 0 )) ; 
                if(k)
                    dp[i][j][k] = max(dp[i][j][k], dp[i][j][k-1] + bool( (i*1+j*2+(k-1)*3)%P == 0 )) ; 
            }
        }
    }
    printf("%d\n", ans + dp[stat[1]][stat[2]][stat[3]]) ; 
}

int main()
{
    int T ; 
    scanf("%d", &T) ; 
    for(int time = 1 ; time <= T ; time++){
        fprintf(stderr, "solving case (%d / %d)...\n", time, T) ; 
        printf("Case #%d: ", time) ; 
        sol() ; 
    }
    return 0 ; 
}


