#include <bits/stdc++.h>

using namespace std;

const int MaxN = 1e3 + 15;
const int INF = 1e9;
const int MOD = 1e9 + 7;

int cases;

long long d[MaxN][MaxN];
long double D[MaxN][MaxN];

int n, q;

long long e[MaxN];
long double s[MaxN];


void solve()
{
    ++cases;
    cout << "Case #" << cases << ": ";
    cin >> n >> q;

    for(int i = 1; i <= n; ++i)
        cin >> e[i] >> s[i];

    for(int i = 1; i <= n; ++i)
        for(int j = 1; j <= n; ++j)
        {
            cin >> d[i][j];
            if(d[i][j] == -1)
                d[i][j] = INF * 1ll * INF;
        }

    for(int k = 1; k <= n; ++k)
        for(int i = 1; i <= n; ++i)
            for(int j = 1; j <= n; ++j)
                if(i != j && j != k && i != k)
                    d[i][j] = min(d[i][j], d[i][k] + d[k][j]);

    for(int i = 1; i <= n; ++i)
        for(int j = 1; j <= n; ++j)
        {
            if(d[i][j] > e[i])
                D[i][j] = INF * 1ll * INF;
            else
                D[i][j] = d[i][j] / s[i];
        }

    for(int k = 1; k <= n; ++k)
        for(int i = 1; i <= n; ++i)
            for(int j = 1; j <= n; ++j)
                if(i != j && j != k && i != k)
                    D[i][j] = min(D[i][j], D[i][k] + D[k][j]);

    cout.precision(9);
    for(int i = 1; i <= q; ++i)
    {
        int a, b;
        cin >> a >> b;
        cout << fixed << D[a][b] << ' ';
    }
    cout << '\n';
}

int main()
{
    freopen("C-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    ios_base :: sync_with_stdio(false);
    cin.tie(NULL);
    int t;
    cin >> t;
    while(t --> 0)
        solve();
    return 0;
}
