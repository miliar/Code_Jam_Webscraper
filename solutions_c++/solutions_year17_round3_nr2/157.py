#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <algorithm>
#include <vector>
#include <stack>
#include <queue>
#include <map>
#define N 111111
#define md 1000000007
using namespace std;

int t;

int allo[1450], dp[1450][750][2]; // dp[t][c][k] = at time t, minimum # of switches with cared c mins and owner is k

int main(void){
    scanf("%d", &t);
    for(int s = 1; s <= t; s++){
        int ac, aj;
        memset(allo, 0, sizeof allo);
        memset(dp, 0x3f, sizeof dp);
        dp[0][0][0] = 0, dp[0][0][1] = 0;
        scanf("%d%d", &ac, &aj);
        for(int i = 0; i < ac; i++){
            int u, v;
            scanf("%d%d", &u, &v);
            for(int j = u; j < v; j++) allo[j] = 1;
        }
        for(int i = 0; i < aj; i++){
            int u, v;
            scanf("%d%d", &u, &v);
            for(int j = u; j < v; j++) allo[j] = 2;
        }
        for(int tm = 0; tm < 1440; tm++){
            for(int c = 0; c <= 720; c++){
                // without switch
                if(allo[tm] != 1) dp[tm + 1][c + 1][0] = min(dp[tm + 1][c + 1][0], dp[tm][c][0]);
                if(allo[tm] != 2) dp[tm + 1][c][1] = min(dp[tm + 1][c][1], dp[tm][c][1]);
                // with switch
                if(allo[tm] != 1) dp[tm + 1][c + 1][0] = min(dp[tm + 1][c + 1][0], dp[tm][c][1] + 1);
                if(allo[tm] != 2) dp[tm + 1][c][1] = min(dp[tm + 1][c][1], dp[tm][c][0] + 1);
            }
        }
        printf("Case #%d: %d\n", s, (min(dp[1440][720][0], dp[1440][720][1]) + 1) / 2 * 2);
    }
}
