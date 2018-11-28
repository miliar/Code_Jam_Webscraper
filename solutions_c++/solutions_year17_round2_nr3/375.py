#include <bits/stdc++.h>
using namespace std;
#pragma GCC diagnostic ignored "-Wmissing-declarations"

#define FINAL_OUT(x) {cout << (x) << '\n'; exit(0);}


void solve(int numtest)
{
    int n,q;
    cin >> n >> q;

    vector<pair<int, int> > h(n);
    for(int i = 0; i < n; ++i)
        cin >> h[i].first >> h[i].second;

    int const inf = 1000000008;

    vector<vector<long long> > d(n, vector<long long>(n));
    for(int i = 0; i < n; ++i)
        for(int j = 0; j < n; ++j)
        {
            cin >> d[i][j];
            if (d[i][j] < 0)
                d[i][j] = inf;
        }



    for(int k = 0; k < n; ++k)
        for(int i = 0; i < n; ++i)
            for(int j = 0; j < n; ++j)
                d[i][j] = min(d[i][j], d[i][k] + d[k][j]);


    vector<vector<double> > dp(n, vector<double>(n, 1e13));
    for(int i = 0; i < n; ++i)
        for(int j = 0; j < n; ++j)
            if (d[i][j] <= h[i].first)
                dp[i][j] = min(dp[i][j], d[i][j] / static_cast<double>(h[i].second));

    for(int k = 0; k < n; ++k)
        for(int i = 0; i < n; ++i)
            for(int j = 0; j < n; ++j)
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j]);


    cout << "Case #" << numtest << ": ";
    while (q--)
    {
        int x,y;
        cin >> x >> y;
        --x, --y;
        cout << dp[x][y] << " \n"[q == 0];
    }
}

int main()
{
    //freopen("in.txt", "r", stdin);
    freopen("C-large.in", "r", stdin);
    freopen("C-large.out", "w", stdout);
    ios_base::sync_with_stdio(false);

    cout << fixed << setprecision(10);

    int t;
    cin >> t;
    for(int i = 1; i <= t; ++i)
    {
        solve(i);
        cerr << "test " << i << endl;
    }
}
