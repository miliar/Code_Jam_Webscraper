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

double calc(vector <double> p, int k)
{
    int n = p.size();
    for (int i = 0; i <= n; i++)
    {
        for (int j = 0; j <= k; j++)
        {
            dp[i][j] = 0;
        }
    }
    dp[0][0] = 1;
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j <= k; j++)
        {
            dp[i + 1][j] += dp[i][j] * (1 - p[i]);
            dp[i + 1][min(k, j + 1)] += dp[i][j] * p[i];
        }
    }
    return dp[n][k];
}

double solve()
{
    int n, k;
    cin >> n >> k;
    double u;
    cin >> u;
    vector <double> p(n);
    for (int i = 0; i < n; i++)
    {
        cin >> p[i];
    }
    sort(p.begin(), p.end());
    double ans = 0;
    for (int i = 0; i < n; i++)
    {
        auto t = p;
        double x = u;
        for (int j = 0; j < i; j++)
        {
            double kek = t[i] - t[j];
            if (kek <= x)
            {
                x -= kek;
                t[j] = t[i];
            }
            else
            {
                t[j] += x;
                x = 0;
                break;
            }
        }
        double cur = 1;
        double rest = x / (double) (i + 1);
        for (int j = 0; j <= i; j++)
        {
            t[j] += rest;
        }
        for (auto c : t)
        {
            cur *= c;
        }
        ans = max(ans, cur);
    }
    return ans;
}

int main()
{
#ifdef ONPC
    freopen("smanul.in", "r", stdin);
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
