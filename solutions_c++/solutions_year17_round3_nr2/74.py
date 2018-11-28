//
// Created by Denis Mukhametianov on 30.04.17.
//

#include <cstdio>
#include <cstring>
#include <algorithm>

const int maxn = 24 * 60 + 10;
const int infin = (int)1e9;

using namespace std;

int busy[maxn];
int dp[2][maxn][maxn][2];

void solveB(int tc) {
    fprintf(stderr, "Solving %d...\n", tc + 1);
    int n, m;
    scanf("%d%d", &n, &m);
    memset(busy, -1, sizeof busy);
    for(int i = 0; i < n; i++) {
        int l, r;
        scanf("%d%d", &l, &r);
        for(int j = l; j < r; j++)
            busy[j] = 0;
    }
    for(int i = 0; i < m; i++) {
        int l, r;
        scanf("%d%d", &l, &r);
        for(int j = l; j < r; j++)
            busy[j] = 1;
    }
    for(int i = 0; i < 2; i++)
        for(int j = 0; j < maxn; j++)
            for(int k = 0; k < maxn / 2; k++)
                for(int l = 0; l < 2; l++)
                    dp[i][j][k][l] = infin;
    if(busy[0] != 0)
        dp[0][0][1][0] = 0;
    if(busy[0] != 1)
        dp[1][0][0][1] = 0;
    for(int starter = 0; starter < 2; starter++) {
        for(int total = 0; total < 24 * 60; total++) {
            for(int first = 0; first <= 12 * 60; first++) {
                auto second = total - first + 1;
                if(second > 12 * 60)
                    continue;
                for(int current = 0; current < 2; current++) {
                    if(dp[starter][total][first][current] == infin)
                        continue;
                    if(busy[total + 1] != 0) {
                        dp[starter][total + 1][first + 1][0] = min(
                                dp[starter][total + 1][first + 1][0],
                                dp[starter][total][first][current] + (current == 0 ? 0 : 1)
                        );
                    }
                    if(busy[total + 1] != 1) {
                        dp[starter][total + 1][first][1] = min(
                                dp[starter][total + 1][first][1],
                                dp[starter][total][first][current] + (current == 1 ? 0 : 1)
                        );
                    }
                }
            }
        }
    }
    int ans = infin;
    for(int i = 0; i < 2; i++)
        for(int j = 0; j < 2; j++) {
            ans = min(ans, dp[i][24 * 60 - 1][12 * 60][j] + (i == j ? 0 : 1));
            //printf("%d %d: %d\n", i, j, dp[i][24 * 60][12 * 60][j]);
        }
    printf("Case #%d: %d\n", tc + 1, ans);
}

void solveB() {
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int t;
    scanf("%d", &t);
    for(int i = 0; i < t; i++)
        solveB(i);
}