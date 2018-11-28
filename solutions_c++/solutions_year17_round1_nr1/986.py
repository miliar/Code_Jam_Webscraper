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
char a[101][101];
int xn[10000];
int xk[10000];
int ynn[10000];
int yk[10000];
void solve(int x)
{
    int n, m, i, j;
    cin >> n >> m;
    for(i = 0; i <= 1000; i ++)
    {
        xn[i] = inf;
        ynn[i] = inf;
        xk[i] = 0;
        yk[i] = 0;
    }
    for(i = 1; i <= n; i ++)
    {
        for(j = 1; j <= m; j ++)
        {
            cin >> a[i][j];
            int x = a[i][j];
            xn[x] = min(xn[x], i);
            xk[x] = max(xk[x], i);
            ynn[x] = min(ynn[x], j);
            yk[x] = max(yk[x], j);
        }
    }
    for(char i = 'A'; i <= 'Z'; i ++)
    {
        for(int j = xn[i]; j <= xk[i]; j ++)
        {
            for(int k = ynn[i]; k <= yk[i]; k ++)
            {
                a[j][k] = i;
            }
        }
    }
    for(char i = 'A'; i <= 'Z'; i ++)
    {
        if(xk[i] != 0)
        {
            while(xn[i] > 1)
            {
                bool ok = 1;
                for(j = ynn[i]; j <= yk[i]; j ++)
                {
                    if(a[xn[i] - 1][j] != '?')
                        ok = 0;
                }
                if(!ok)
                    break;
                xn[i] --;
            }
            while(xk[i] < n)
            {
                bool ok = 1;
                for(j = ynn[i]; j <= yk[i]; j ++)
                {
                    if(a[xk[i] + 1][j] != '?')
                        ok = 0;
                }
                if(!ok)
                    break;
                xk[i] ++;
            }
            for(int j = xn[i]; j <= xk[i]; j ++)
            {
                for(int k = ynn[i]; k <= yk[i]; k ++)
                {
                    a[j][k] = i;
                }
            }
        }
    }
    for(char i = 'A'; i <= 'Z'; i ++)
    {
        if(xk[i] != 0)
        {
            while(ynn[i] > 1)
            {
                bool ok = 1;
                for(j = xn[i]; j <= xk[i]; j ++)
                {
                    if(a[j][ynn[i] - 1] != '?')
                        ok = 0;
                }
                if(!ok)
                    break;
                ynn[i] --;
            }
            while(yk[i] < m)
            {
                bool ok = 1;
                for(j = xn[i]; j <= xk[i]; j ++)
                {
                    if(a[j][yk[i] + 1] != '?')
                        ok = 0;
                }
                if(!ok)
                    break;
                yk[i] ++;
            }
            for(int j = xn[i]; j <= xk[i]; j ++)
            {
                for(int k = ynn[i]; k <= yk[i]; k ++)
                {
                    a[j][k] = i;
                }
            }
        }
    }
    cout << "Case #" << x << ":\n";
    for(i = 1; i <= n; i ++)
    {
        for(j = 1; j <= m; j ++)
        {
            cout << a[i][j];
        }
        cout << endl;
    }
}
main()
{
    freopen("A-small-attempt0.in", "r", stdin);
    freopen("A-small-attempt0.out", "w", stdout);
    int t;
    cin >> t;
    for(int i = 1; i <= t; i ++)
    {
        solve(i);
    }
}

