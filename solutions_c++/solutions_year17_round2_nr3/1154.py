#include <bits/stdc++.h>

using namespace std;

#define int int64_t
#define mp make_pair
#define fi first
#define se second

ifstream in("C-small-attempt1.in");
ofstream out("C_small_ans.txt");

#define cin in
#define cout out

const long double eps = 1e-9;

long double solve()
{
    int n, q;
    cin >> n >> q;
    vector <int> d(n), s(n);
    for (int i = 0; i < n; ++i)
        cin >> d[i] >> s[i];
    vector <vector <int> > g(n, vector <int> (n, 0));
    for (int i = 0; i < n; ++i)
    {
        for (int j = 0; j < n; ++j)
        {
            cin >> g[i][j];
        }
    }
    vector <long double> dp(n, 1e18);
    dp[0] = 0.;
    for (int i = 1; i < n; ++i)
    {
        long double dist = 0.;
        for (int j = i - 1; j >= 0; --j)
        {
            dist += g[j][j + 1];
            assert(g[j][j + 1] >= 0);
            if (d[j] > dist - eps)
            {
                dp[i] = min(dp[i], dp[j] + (long double)dist / (long double)s[j]);
            }
        }
    }
    int u, v;
    cin >> u >> v;
    assert(u == 1 && v == n);
    //system("pause");
    assert(dp[n - 1 < 1e17]);
    return dp[n - 1];
}

signed main()
{
    cout.precision(20);
    int t;
    cin >> t;
    for (int itt = 0; itt < t; ++itt)
    {
        cout << "Case #" << itt + 1 << ": " << solve() << endl;
    }
    system("pause");
    return 0;
}

