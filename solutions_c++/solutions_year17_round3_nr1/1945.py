#include "math.h"
#include <algorithm>
#include <set>
#include <complex>
#include <stack>
#include <cstdio>
#include <iomanip>
#include <iostream>
#include <map>
#include <queue>
#include <string>
#include <vector>
#include <random>
#define rep(i, n) for (lli i = 0; i < (n); i++)
#define rrep(i, n) for (lli i = (n)-1; i >= 0; i--)
using namespace std;
typedef long long int lli;

double dp[2000][2000] = {};
double solve()
{
    int n, k;

    cin >> n >> k;

    vector<pair<double, double>> d;
    rep(i, 2000) rep(j, 2000) dp[i][j] = 0;

    // dp[i][j] := iまでみてがでj枚積んだ解き
    double a, b;
    d.push_back(make_pair(1e10, 1e10));
    rep(i, n)
    {
        cin >> a >> b;
        d.push_back(make_pair(a, b));
    }
    sort(d.begin(), d.end());
    reverse(d.begin(), d.end());
    double pi = 3.14159265359;
    rep(i, n)
    {
        rep(j, k)
        {
            //cout << i << " " << j << endl;
            if (j == 0) {
                dp[i + 1][j + 1] = max(dp[i][j] + pi * d[i + 1].first * d[i + 1].first + 2 * pi * d[i + 1].second * d[i + 1].first, dp[i + 1][j + 1]);
            } else {
                dp[i + 1][j + 1] = max(dp[i][j] + 2 * pi * d[i + 1].first * d[i + 1].second, dp[i + 1][j + 1]);
            }
            dp[i + 1][j] = max(dp[i][j], dp[i + 1][j]);
            dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j + 1]);
        }
    }
    return dp[n][k];
}
int main()
{
    lli t;
    cin >> t;
    rep(i, t)
    {
        cout << "Case #" << i + 1 << ": ";
        printf("%.10f\n", solve());
    }
}
