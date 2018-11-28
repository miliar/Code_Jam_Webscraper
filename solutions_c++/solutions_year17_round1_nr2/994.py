#include <bits/stdc++.h>
#define int long long
using namespace std;
const int N = 1123456;
const int mod = 1e9 + 7;
const int inf = 1e9 + 7;
int read()
{
    int x;
    scanf("%I64d", &x);
    return x;
}
int a[100];
int id[100];
int d[100][100];
int y[100];
double l[101];
double r[101];
bool cmp(int x, int y)
{
    return a[x] < a[y];
}
void solve(int x)
{
    int n, m, i, j;
    cin >> n >> m;
    for(i = 1; i <= n; i ++)
    {
        y[i] = 1;
        id[i] = i;
        cin >> a[i];
    }
    for(i = 1; i <= n; i ++)
        for(j = 1; j <= m; j ++)
            cin >> d[i][j];
    sort(id + 1, id + n + 1, cmp);
    for(i = 1; i <= n; i ++)
    {
        sort(d[i] + 1, d[i] + m + 1);
    }
    int ans = 0;
    while(1)
    {
        bool ok = 1;
        double lx = 0;
        double rx = inf;
        for(j = 1; j <= n; j ++)
        {
            r[j] = d[j][y[j]] / (0.9 * a[j]);
            l[j] = d[j][y[j]] / (1.1 * a[j]);
            lx = max(lx, l[j]);
            rx = min(rx, r[j]);
        }
        int llx = lx;
        int rrx = rx;
        if(llx < lx)
            llx ++;
        if(llx <= rrx)
        {
            ans ++;
            for(int j = 1; j <= n; j ++)
            {
                y[j] ++;
                if(y[j] > m)
                    ok = 0;
            }
        }
        else
        {
            double mx = inf;
            int id = 0;
            for(j = 1; j <= n; j ++)
            {
                r[j] = d[j][y[j]] / (0.9 * a[j]);
                l[j] = d[j][y[j]] / (1.1 * a[j]);
                if(mx > l[j])
                {
                    mx = l[j];
                    id = j;
                }
            }
            y[id] ++;
            if(y[id] > m)
                ok = 0;
        }
        if(!ok)
            break;
    }
    cout << "Case #" << x << ": " << ans << endl;
}
main()
{
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
    int t;
    cin >> t;
    for(int i = 1; i <= t; i ++)
    {
        solve(i);
    }
}

