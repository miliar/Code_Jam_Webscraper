// Google Code Jam 2017, Round 2 [A]
// hhttps://code.google.com/codejam/contest/5314486/dashboard#s=p0
// 2017.05.13

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
#define ll long long
#define md 1000000007
using namespace std;

int dp2[111][2], dp3[111][111][3], dp4[111][111][111][4];

int solve2(int a, int m){
    if(dp2[a][m] < 0x3f3f3f3f) return dp2[a][m];
    dp2[a][m] = 0;
    if(m == 0){
        if(a > 0)
            dp2[a][m] = max(dp2[a][m], solve2(a - 1, (m + 1) % 2) + 1);
    } else {
        if(a > 0)
            dp2[a][m] = max(dp2[a][m], solve2(a - 1, (m + 1) % 2));
    }
    return dp2[a][m];
}
int solve3(int a, int b, int m){
    if(dp3[a][b][m] < 0x3f3f3f3f) return dp3[a][b][m];
    dp3[a][b][m] = 0;
    if(m == 0){
        if(a > 0)
            dp3[a][b][m] = max(dp3[a][b][m], solve3(a - 1, b, (m + 1) % 3) + 1);
        if(b > 0)
            dp3[a][b][m] = max(dp3[a][b][m], solve3(a, b - 1, (m + 2) % 3) + 1);
    } else {
        if(a > 0)
            dp3[a][b][m] = max(dp3[a][b][m], solve3(a - 1, b, (m + 1) % 3));
        if(b > 0)
            dp3[a][b][m] = max(dp3[a][b][m], solve3(a, b - 1, (m + 2) % 3));
    }
    return dp3[a][b][m];
}
int solve4(int a, int b, int c, int m){
    if(dp4[a][b][c][m] < 0x3f3f3f3f) return dp4[a][b][c][m];
    dp4[a][b][c][m] = 0;
    if(m == 0){
        if(a > 0)
            dp4[a][b][c][m] = max(dp4[a][b][c][m], solve4(a - 1, b, c, (m + 1) % 4) + 1);
        if(b > 0)
            dp4[a][b][c][m] = max(dp4[a][b][c][m], solve4(a, b - 1, c, (m + 2) % 4) + 1);
        if(c > 0)
            dp4[a][b][c][m] = max(dp4[a][b][c][m], solve4(a, b, c - 1, (m + 3) % 4) + 1);
    } else {
        if(a > 0)
            dp4[a][b][c][m] = max(dp4[a][b][c][m], solve4(a - 1, b, c, (m + 1) % 4));
        if(b > 0)
            dp4[a][b][c][m] = max(dp4[a][b][c][m], solve4(a, b - 1, c, (m + 2) % 4));
        if(c > 0)
            dp4[a][b][c][m] = max(dp4[a][b][c][m], solve4(a, b, c - 1, (m + 3) % 4));
    }
    return dp4[a][b][c][m];
}

int main(void){

    memset(dp2, 0x3f, sizeof dp2);
    memset(dp3, 0x3f, sizeof dp3);
    memset(dp4, 0x3f, sizeof dp4);

    int t;
    scanf("%d", &t);
    for(int s = 1; s <= t; s++){
        int ans = 0, n, r[5], p;
        scanf("%d%d", &n, &p);
        memset(r, 0, sizeof r);
        for(int i = 0; i < n; i++){
            int g;
            scanf("%d", &g);
            r[g % p]++;
        }
        if(p == 2)
            printf("Case #%d: %d\n", s, r[0] + solve2(r[1], 0));
        else if(p == 3)
            printf("Case #%d: %d\n", s, r[0] + solve3(r[1], r[2], 0));
        else if(p == 4)
            printf("Case #%d: %d\n", s, r[0] + solve4(r[1], r[2], r[3], 0));
    }
}