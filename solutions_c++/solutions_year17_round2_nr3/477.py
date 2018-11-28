#include <bits/stdc++.h>
#define int long long
using namespace std;
const int N = 1123456;
const int mod = 1e9 + 7;
const int inf = 1e14 + 7;
int read()
{
    int x;
    scanf("%I64d", &x);
    return x;
}
int e[N];
int s[N];
int a[1010][1010];
double d[110][110];
double ans[N];
double w[110];
void solve(int test)
{
    cout << "Case #" << test << ": ";
    int n, m, i, j;
    cin >> n >> m;
    for(i = 1; i <= n; i ++)
    {
        cin >> e[i] >> s[i];
    }
    for(i = 1; i <= n; i ++)
        for(j = 1; j <= n; j ++)
            d[i][j] = inf;
    for(i = 1; i <= n; i ++)
    {
        ans[i] = inf;
        for(j = 1; j <= n; j ++)
        {
            cin >> a[i][j];
            if(a[i][j] == -1)
                d[i][j] = inf;
            else
                d[i][j] = a[i][j];
            if(i == j)
                d[i][j] = 0;
        }
    }
    for(int k = 1; k <= n; ++k)
        for(i = 1; i <= n; ++i)
            for (j = 1; j <= n; ++j)
                d[i][j] = min (d[i][j], d[i][k] + d[k][j]);
    for(int q = 1; q <= m; q ++)
    {
        int x, y;
        cin >> x >> y;
        for(i = 1; i <= n; i ++)
            w[i] = inf;
        w[x] = 0;
        for(int r = 1; r <= n; r ++)
        {
            for(i = 1; i <= n; i ++)
            {
                for(j = 1; j <= n; j ++)
                {
                    if(i != j)
                    {
                        if(d[i][j] <= e[i])
                        {
                            w[j] = min(w[j], w[i] + d[i][j] / s[i]);
                        }
                    }
                }
            }
        }
        printf("%.10f ", w[y]);
    }
    cout << endl;
}
main()
{
    freopen("C-large.in", "r", stdin);
    freopen("C-large.out", "w", stdout);
    int t;
    cin >> t;
    for(int i = 1; i <= t; i ++)
    {
        solve(i);
    }
}

