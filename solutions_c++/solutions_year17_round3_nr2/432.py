#include <cstdio>
#include <algorithm>
#include <cstring>

const int INF = 0x3f3f3f3f;
const int MAXN = 2000;
const int MAXH = 720;
const int FULL = 1440;

using namespace std;

int dp[MAXH+10][MAXH+10][2];
int A[MAXN+5], B[MAXN+5];


void upgrade(int &, int);

int T, n, m, x, y;

void init() {
    memset(A, 0, sizeof(A));
    memset(B, 0, sizeof(B));
}

void input() {
    scanf("%d%d", &n, &m);
    for(int i = 0; i < n; ++i) {
        scanf("%d%d", &x, &y);
        for(int j = x; j < y; ++j) {
            A[j] = 1;
        }
    }
    int l, r;
    for(int i = 0; i < m; ++i) {
        scanf("%d%d", &l, &r);
        for(int j = l; j < r; ++j) {
            B[j] = 1;
        }
    }
}

int main() {

//    freopen("B-eg.in", "r", stdin);
//    freopen("B-small-attempt0.in", "r", stdin);
    freopen("B-large.in", "r", stdin);
//    freopen("B-eg.out", "w", stdout);
//    freopen("B-small-attempt0.out", "w", stdout);
    freopen("B-large.out", "w", stdout);

    scanf("%d", &T);
    for(int t = 1; t <= T; ++ t) {

        init();
        input();

        int ans = INF;
        if(!A[0]) {
            memset(dp, 0x3f, sizeof(dp));
            dp[1][0][0] = 0;
            for(int i = 0; i <= MAXH; ++i) {
                for(int j = 0; j <= MAXH; ++j) {
                    int tmp = i + j;
                    if(tmp >= FULL) {
                        continue;
                    }
                    if(dp[i][j][0] != INF) {
                        if(!A[tmp] && i < MAXH) {
                            upgrade(dp[i+1][j][0], dp[i][j][0]);
                        }
                        if(!B[tmp] && j < MAXH) {
                            upgrade(dp[i][j+1][1], dp[i][j][0]+1);
                        }
                    }
                    if(dp[i][j][1] != INF) {
                        if(!A[tmp] && i < MAXH) {
                            upgrade(dp[i+1][j][0], dp[i][j][1]+1);
                        }
                        if(!B[tmp] && j < MAXH) {
                            upgrade(dp[i][j+1][1], dp[i][j][1]);
                        }
                    }
                }
            }
            ans = min(dp[MAXH][MAXH][0], dp[MAXH][MAXH][1] + 1);
        }
        if(!B[0]) {
            memset(dp, 0x3f, sizeof(dp));
            dp[0][1][1] = 0;
            for(int i = 0; i <= MAXH; ++i) {
                for(int j = 0; j <= MAXH; ++j) {
                    int tmp = i+j;
                    if(tmp >= FULL) {
                        continue;
                    }
                    if(dp[i][j][0] != INF) {
                        if(!A[tmp] && i < MAXH) {
                            upgrade(dp[i+1][j][0], dp[i][j][0]);
                        }
                        if(!B[tmp] && j < MAXH) {
                            upgrade(dp[i][j+1][1], dp[i][j][0]+1);
                        }
                    }
                    if(dp[i][j][1] != INF) {
                        if(!A[tmp] && i < MAXH) {
                            upgrade(dp[i+1][j][0], dp[i][j][1] + 1);
                        }
                        if(!B[tmp] && j < MAXH) {
                            upgrade(dp[i][j+1][1], dp[i][j][1]);
                        }
                    }
                }
            }
            ans = min(min(ans, dp[MAXH][MAXH][0] + 1), min(ans, dp[MAXH][MAXH][1]));
        }

        printf("Case #%d: %d\n", t, ans);
    }
}

void upgrade(int &x, int v) {
    x = min(x, v);
}
