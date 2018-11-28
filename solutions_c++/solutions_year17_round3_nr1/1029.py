/*
░░░░░░░▄▀▀▀▀▀▀▀▄▄░░░░░░
░░░░░░▐░░░▄▄▄▄▄░ ▀▀▄
░░░░░▐░$░▐▀░░░░▀▀▀▀▄▀
░░░░░▌░░▐░░░░░░░░░░▄▄
░░░░▐░░░░▀▄▄▄▄▄▄▀▀▀░▄▀
░░░░▌▒░▒░▒░▒░░░▄▄▄▀▀
░░░░▌▒▒░▒▒▒▒▄▄▀▀
░░░▐░░▒▒▒▄▀▀░░░░░░░
░░░▐░▒▒▒▐░░░░░░░░░
░░░▐▒▒▒▒▌░░░░░░░░
░░░▐▒▒▒░▐░░░░░░░░░▄▀▄
░░░▐▒▒░▒▐▄▄▀▀▀▀▄▄▄▀░▌
░░░▐░▒▒░▄▄▄▄▀▀▄▄▄▄▄▀
░░▐▒▒▄▒▒▀▄▄▄▄▄▀░░░▄▌░░
░░▌▒▐░▀▀▄▄▄▄▄▄▄▀▀▀░░░░
░▐▒▒▌░░░░░░░░░░░░░ 
*/
#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

void print(int it, double ans)
{
    cout << fixed << setprecision(20) << "Case #" << it << ": " << ans << '\n';
}

const int N = 1000 + 3;
const double pi = 3.141592653589793238462643383279;

double dp[N][N];

double solve()
{
    int n, k;
    cin >> n >> k;
    vector <pair <double, double> > e;
    for (int i = 0; i < n; i++)
    {
        int r, h;
        cin >> r >> h;
        e.push_back({r, h});
    }
    sort(e.rbegin(), e.rend());
    for (int i = 0; i <= n; i++)
    {
        for (int j = 0; j <= k; j++)
        {
            dp[i][j] = -1e18;
        }
    }
    dp[0][0] = 0;
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j <= k; j++)
        {
            dp[i + 1][j] = max(dp[i + 1][j], dp[i][j]);
            double kek = e[i].second * e[i].first * 2 * pi;
            double se = e[i].first * e[i].first * pi;
            if (j != k)
            {
                dp[i + 1][j + 1] = max(dp[i + 1][j + 1], dp[i][j] - ((j != 0) * se) + se + kek);
            }
        }
    }
    return dp[n][k];
}

int main()
{
#ifdef ONPC
    freopen("lagr.in", "r", stdin);
    freopen("a.out", "w", stdout);
#else
    //freopen("a.in", "r", stdin);
    //freopen("a.out", "w", stdout);
#endif
    int t;
    cin >> t;
    for (int it = 0; it < t; it++)
    {
        print(it + 1, solve());
    }
}
