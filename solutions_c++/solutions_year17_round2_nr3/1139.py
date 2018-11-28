#include <bits/stdc++.h>
#define all(a) (a).begin(),(a).end()
#define ld long double
#define ll long long
#define sqr(a) (a)*(a)
#define mp make_pair
#define pb push_back
#define x first
#define y second
#define inf (int)1e9
#define pi pair<int,int>
#define y1 fdfs
using namespace std;

const int N = 105;

long long  n, m, dist[N], speed[N];
long long d[N][N], t;
long double dp[N];

void solve()
{
    cin >> n >> m;
    for (int i = 0; i < n; ++i)
        cin >> dist[i] >> speed[i];
    for (int i = 0; i < n; ++i)
        for (int j = 0; j < n; ++j)
        cin >> d[i][j];
    for (int i = 0; i < n; ++i)
        for (int j = i + 2; j < n; ++j)
    {
        if(d[i][j - 1] != -1 && d[j - 1][j] != -1)
            d[i][j] = d[i][j - 1] + d[j - 1][j];
    }
    cin >> m >> m;
    for (int i = 0; i < n; ++i)
        dp[i] = 1e18;
    dp[0] = 0;
    for (int i = 0; i < n; ++i)
    {
        for (int j = i + 1; j < n; ++j)
            if (dist[i] >= d[i][j])
            {
                dp[j] = min(dp[j], dp[i] + (d[i][j]+0.) / speed[i]);
            }
    }
    cout.precision(6);
    cout << fixed << dp[n - 1];
}

int main()
{
    freopen("C-small-attempt0.in","r",stdin);
    freopen("1.out","w",stdout);
    ios_base::sync_with_stdio(0);
    cin >> t;
    for (int i = 1; i <= t; ++i)
    {
        cout << "Case #" << i << ": ";
        solve();
        cout << "\n";
    }
}
