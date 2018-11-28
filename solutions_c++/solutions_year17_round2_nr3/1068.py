#include <vector>
#include <stdio.h>
#include <string.h>
#include <iostream>
#include <algorithm>

using namespace std;

//#define FIN freopen("C-small-attempt0.in", "r", stdin)
#define FIN freopen("C-small-attempt0.in", "r", stdin)
#define FOUT freopen("out.ads", "w", stdout)

const int N = 1e2 + 5;

int g[N][N], dis[N][N];

bool can[N][N];

pair<int, int> a[N];

double dp[N][N];

const double MAX = 1e15;

int main() {
    FIN;
    FOUT;
    int T, ncase = 0;
    scanf("%d", &T);
    while(T--) {
        int n, q;
        scanf("%d%d", &n, &q);
        for(int i = 0; i < n; ++i) {
            scanf("%d%d", &a[i].first, &a[i].second);
        }
        for(int i = 0; i < n; ++i) {
            for(int j = 0; j < n; ++j) {
                scanf("%d", &g[i][j]);
                dp[i][j] = MAX;
            }
        }
        memset(dis, 0, sizeof(dis));
        memset(can, false, sizeof(can));
        for(int i = 0; i < n; ++i) {
            int sum = 0;
            for(int j = i + 1; j < n; ++j) {
                sum += g[j - 1][j];
                dis[i][j] = sum;
                if(sum <= a[i].first) {
                    can[i][j] = true;
                }
                else {
                    can[i][j] = false;
                }
            }
        }
        while(q--) {
            int s, t;
            scanf("%d%d", &s, &t);
        }
        dp[0][0] = 0;
        for(int i = 1; i < n; ++i) {
            for(int j = 0; j < i; ++j) {
                if(can[j][i]) {
                    dp[i][j] = dp[i - 1][j] + g[i - 1][i] * 1.0 / a[j].second;
                }
            }
            double mmin = MAX;
            for(int k = 0; k < i; ++k) {
                mmin = min(mmin, dp[i][k]);
            }
            dp[i][i] = mmin;
        }
        double ans = MAX;
        for(int k = 0; k < n; ++k) {
            ans = min(ans, dp[n - 1][k]);
        }
        printf("Case #%d: %.7f\n", ++ncase, ans);
    }
    return 0;
}
