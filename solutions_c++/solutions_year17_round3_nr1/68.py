#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <cmath>

using namespace std;

typedef pair<int, int> pii;

const double PI = acos(-1.0);
const double eps = 1e-8;
const int maxn = 1000 + 5;

double dp[2][maxn];
pii p[maxn];

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("answer.out", "w", stdout);
    int T, cas = 0;
    scanf("%d", &T);
    while(T--)
    {
        int n, k;
        scanf("%d%d", &n, &k);
        for(int i = 1; i <= n; ++i) scanf("%d%d", &p[i].first, &p[i].second);
        sort(p + 1, p + n + 1);
        int now = 0, nxt = 1;
        double ans = 0;
        memset(dp, 0, sizeof(dp));
        for(int i = 1; i <= k; ++i)
        {
            double tmp = 0;
            for(int j = 1; j <= n; ++j)
            {
                tmp = max(tmp, dp[now][j - 1]);
                dp[nxt][j] = tmp + 2 * PI * p[j].first * p[j].second;
                ans = max(ans, dp[nxt][j] + PI * p[j].first * p[j].first);
            }
            swap(now, nxt);
        }
        printf("Case #%d: ", ++cas);
        printf("%.10f\n", ans);
    }
    return 0;
}
