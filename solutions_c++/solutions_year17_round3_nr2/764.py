#include <bits/stdc++.h>

using namespace std;

#define int int64_t
#define endl '\n'
#define fi first
#define se second
#define mp make_pair
#define pb push_back

template <typename T>
ostream & operator << (ostream & out, vector <T> & arr)
{
    for (int i = 0; i < (int)arr.size() - 1; ++i)
        out << arr[i] << " ";
    if (arr.size())
        out << arr.back() << endl;
    return out;
}

template <typename T>
istream & operator >> (istream & in, vector <T> & arr)
{
    for (auto & i : arr)
        in >> i;
    return in;
}

template <typename T1, typename T2>
ostream & operator << (ostream & out, pair <T1, T2> & p)
{
    out << "{ << p.fi << ", "" << p.se << "}";
    return out;
}

template <typename T1, typename T2>
istream & operator >> (istream & in, pair <T1, T2> & p)
{
    in >> p.fi >> p.se;
    return in;
}

ifstream in("B-large.in");
ofstream out("output.txt");

#define cin in
#define cout out

const int32_t sz = 24 * 60;

int dp[sz + 1][sz + 1][2];

void solve()
{
    int n, m;
    cin >> n >> m;
    vector <pair <int, int> > c(n), j(m);
    cin >> c >> j;
    vector <int> arr(sz, -1);
    for (int i = 0; i < n; ++i)
    {
        for (int k = c[i].fi; k < c[i].se; ++k)
            arr[k] = 0;
    }
    for (int i = 0; i < m; ++i)
    {
        for (int k = j[i].fi; k < j[i].se; ++k)
            arr[k] = 1;
    }
    int ans = 1000000000000000000;

    for (int i = 0; i < sz + 1; ++i)
        for (int k = 0; k < sz + 1; ++k)
        {
            dp[i][k][0] = 1000000000000000000;
            dp[i][k][1] = 1000000000000000000;
        }
    dp[0][0][0] = 1;
    for (int i = 1; i <= sz; ++i)
    {
        for (int j = 0; j <= sz; ++j)
        {
            for (int t = 0; t < 2; ++t)
            {
                if (arr[i - 1] != t)
                {
                    if (j - (t == 0) >= 0)
                        dp[i][j][t] = min(dp[i][j][t], dp[i - 1][j - (t == 0)][1 - t] + 1);
                    if (j - (t == 0) >= 0)
                        dp[i][j][t] = min(dp[i][j][t], dp[i - 1][j - (t == 0)][t]);
                }
            }
        }
    }
    ans = min(ans, min(dp[sz][sz / 2][1], dp[sz][sz / 2][0] - 1));

    for (int i = 0; i < sz + 1; ++i)
        for (int k = 0; k < sz + 1; ++k)
        {
            dp[i][k][0] = 1000000000000000000;
            dp[i][k][1] = 1000000000000000000;
        }
    dp[0][0][1] = 1;
    for (int i = 1; i <= sz; ++i)
    {
        for (int j = 0; j <= sz; ++j)
        {
            for (int t = 0; t < 2; ++t)
            {
                if (arr[i - 1] != t)
                {
                    if (j - (t == 0) >= 0)
                        dp[i][j][t] = min(dp[i][j][t], dp[i - 1][j - (t == 0)][1 - t] + 1);
                    if (j - (t == 0) >= 0)
                        dp[i][j][t] = min(dp[i][j][t], dp[i - 1][j - (t == 0)][t]);
                }
            }
        }
    }
    ans = min(ans, min(dp[sz][sz / 2][0], dp[sz][sz / 2][1] - 1));

    cout << ans;
    return;
}

signed main()
{
    int t;
    cin >> t;
    for (int itt = 0; itt < t; ++itt)
    {
        cout << "case #" << itt + 1 << ": ";
        solve();
        cout << endl;
    }
}
