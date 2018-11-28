#include <bits/stdc++.h>

#define LL long long
#define PI 3.141592653589793238462643383279502384197

using namespace std;

const int maxn = 1005;

struct Cake{
    int r, h;
}a[maxn];

bool cmp1(const Cake &x, const Cake &y){
    return x.r > y.r;
}

int n, k;

double dp[maxn][maxn], sum[maxn][maxn];

int main(){
    freopen("A-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    int T;
    scanf("%d", &T);
    for (int cas = 1; cas <= T; cas++){
        scanf("%d%d", &n, &k);
        for (int i = 1; i <= n; i++){
            scanf("%d%d", &a[i].r, &a[i].h);
        }
        sort(a + 1, a + 1 + n, cmp1);
        memset(sum, 0, sizeof(sum));
        memset(dp, 0, sizeof(dp));
        for (int i = 1; i <= n; i++){
            dp[i][1] = 2 * PI * a[i].r * a[i].h + PI * a[i].r * a[i].r;
            sum[i][1] = max(sum[i - 1][1], dp[i][1]);
        }
        for (int cc = 2; cc <= k; cc++){
            for (int i = cc; i <= n; i++)
                dp[i][cc] = sum[i - 1][cc - 1] + 2 * PI * a[i].r * a[i].h;
            for (int i = 1; i <= n; i++)
                sum[i][cc] = max(sum[i - 1][cc], dp[i][cc]);
        }
        double ans = 0;
        for (int i = k; i <= n; i++)
            ans = max(ans, dp[i][k]);
        printf("Case #%d: %.6f\n", cas, ans);
    }
    return 0;
}
