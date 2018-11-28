#include<bits/stdc++.h>
#define FOR(i,a,b) for (int i=(a),_b=(b);i<=_b;i=i+1)
#define FORD(i,b,a) for (int i=(b),_a=(a);i>=_a;i=i-1)
#define REP(i,n) for (int i=0,_n=(n);i<_n;i=i+1)
#define FORE(i,v) for (__typeof((v).begin()) i=(v).begin();i!=(v).end();i++)
#define ALL(v) (v).begin(),(v).end()
#define fi   first
#define se   second
#define MASK(i) (1LL<<(i))
#define BIT(x,i) (((x)>>(i))&1)
#define div   ___div
#define next   ___next
#define prev   ___prev
#define left   ___left
#define right   ___right
#define __builtin_popcount __builtin_popcountll
using namespace std;
template<class X,class Y>
    void minimize(X &x,const Y &y) {
        if (x>y) x=y;
    }
template<class X,class Y>
    void maximize(X &x,const Y &y) {
        if (x<y) x=y;
    }
template<class T>
    T Abs(const T &x) {
        return (x<0?-x:x);
    }

/* Author: Van Hanh Pham */

/** END OF TEMPLATE - ACTUAL SOLUTION COMES HERE **/

#define MAX   105

int solveTwo(int x, int y) {
    return x + (y + 1) / 2;
}

#define dp   I_LOVE_PMP

int dp[MAX][MAX][MAX][3];

int solveThree(int x, int y, int z) {
    REP(i, x + 1) REP(j, y + 1) REP(k, z + 1) REP(mod, 3)
        dp[i][j][k][mod] = -1;

    dp[0][0][0][0] = 0;
    REP(i, x + 1) REP(j, y + 1) REP(k, z + 1) REP(mod, 3) if (dp[i][j][k][mod] >= 0) {
        if (i < x) maximize(dp[i + 1][j][k][(mod + 0) % 3], dp[i][j][k][mod] + (mod == 0));
        if (j < y) maximize(dp[i][j + 1][k][(mod + 1) % 3], dp[i][j][k][mod] + (mod == 0));
        if (k < z) maximize(dp[i][j][k + 1][(mod + 2) % 3], dp[i][j][k][mod] + (mod == 0));
    }

    int res = -1;
    REP(mod, 3) maximize(res, dp[x][y][z][mod]);
    return res;
}

#undef dp

#define dp   MP_CUTE

int dp[MAX][MAX][MAX][MAX][4];

int solveFour(int x, int y, int z, int t) {
    REP(i, x + 1) REP(j, y + 1) REP(k, z + 1) REP(l, t + 1) REP(mod, 4)
        dp[i][j][k][l][mod] = -1;

    dp[0][0][0][0][0] = 0;
    REP(i, x + 1) REP(j, y + 1) REP(k, z + 1) REP(l, t + 1) REP(mod, 4)
        if (dp[i][j][k][l][mod] >= 0) {
            if (i < x) maximize(dp[i + 1][j][k][l][(mod + 0) % 4], dp[i][j][k][l][mod] + (mod == 0));
            if (j < y) maximize(dp[i][j + 1][k][l][(mod + 1) % 4], dp[i][j][k][l][mod] + (mod == 0));
            if (k < z) maximize(dp[i][j][k + 1][l][(mod + 2) % 4], dp[i][j][k][l][mod] + (mod == 0));
            if (l < t) maximize(dp[i][j][k][l + 1][(mod + 3) % 4], dp[i][j][k][l][mod] + (mod == 0));
        }

    int res = -1;
    REP(mod, 4) maximize(res, dp[x][y][z][t][mod]);
    return res;
}

int solve(void) {
    int n, mod; scanf("%d%d", &n, &mod);
    int cnt[10];
    memset(cnt, 0, sizeof cnt);
    REP(pmp, n) {
        int x; scanf("%d", &x);
        cnt[x % mod]++;
    }

    if (mod == 2) return solveTwo(cnt[0], cnt[1]);
    if (mod == 3) return solveThree(cnt[0], cnt[1], cnt[2]);
    if (mod == 4) return solveFour(cnt[0], cnt[1], cnt[2], cnt[3]);
    assert(false);
}

int main(void) {
    int t; scanf("%d", &t);
    REP(pmp, t) printf("Case #%d: %d\n", pmp + 1, solve());
    return 0;
}

/*** LOOK AT MY CODE. MY CODE IS AMAZING :D ***/
