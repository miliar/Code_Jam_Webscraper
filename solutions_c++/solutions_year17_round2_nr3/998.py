#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;
#define N 105
typedef long long ll;
int d[N][N];
ll s[N];
int a[N][2];
double f[N];
int n, q;

void solve()
{
    scanf("%d%d", &n, &q);
    for (int i = 1; i <= n; ++i)
        for (int j = 0; j < 2; ++j)
            scanf("%d", &a[i][j]);
    for (int i = 1; i <= n; ++i)
        for (int j = 1; j <= n; ++j)
            scanf("%d", &d[i][j]);
    for (int i = 2; i <= n; ++i)
        s[i] = s[i - 1] + d[i - 1][i];
    while (q--)
    {
        int x, y;
        scanf("%d%d", &x, &y);
    }
    f[1] = 0;
    for (int i = 2; i <= n; ++i)
    {
        f[i] = 1e20;
        for (int j = 1; j < i; ++j)
            if (s[i] - s[j] <= a[j][0])
            {
                f[i] = min(f[i], f[j] + double(s[i] - s[j]) / a[j][1]);
                // printf("%f %f %d %d\n", f[i], f[j], s[i] - s[j], a[j][1]);
            }
    }
    printf("%.7f\n", f[n]);
}

int main()
{
    int t;
    freopen("1.txt", "r", stdin);
    freopen("2.txt", "w", stdout);
    scanf("%d", &t);
    for (int tt = 1; tt <= t; ++tt)
    {
        printf("Case #%d: ", tt);
        solve();
    }
    return 0;
}