#include <iostream>
#include <cstdio>
#include <cstring>

using namespace std;

const int maxn = 1111;
int e[maxn], s[maxn];
int w[maxn][maxn];
double dp[maxn];
int st[maxn], ed[maxn];

typedef long long LL;

int main() {
    freopen("cs1.txt", "r", stdin);
    freopen("csout1.txt", "w", stdout);
    int T, ca = 0;
    cin >> T;
    while (T--) {
        int n, Q;
        cin >> n >> Q;
        for (int i = 1; i <= n; ++i) {
            cin >> e[i] >> s[i];
        }
        for (int i = 1; i <= n; ++i) {
            for (int j = 1; j <= n; ++j) {
                cin >> w[i][j];
            }
        }
        for (int i = 0; i < Q; ++i) {
            cin >> st[i] >> ed[i];
        }
        //small;
        dp[n] = 0;
        for (int i = n - 1; i > 0; --i) {
            LL cur_dist = 0;
            dp[i] = 1e20;
            for (int j = i + 1; j <= n; ++j) {
                cur_dist += (LL)w[j - 1][j];
                if (cur_dist <= e[i]) {
                    dp[i] = min(dp[i], (double)cur_dist / s[i] + dp[j]);
                }
            }
        }
        printf("Case #%d: %.6lf\n", ++ca, dp[1]);
        
    }
    return 0;
}