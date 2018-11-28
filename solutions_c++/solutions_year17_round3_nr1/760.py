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

const double M_PI = 3.141592653589793238462643;

ifstream in("A-large111.in");
ofstream out("output.txt");

#define cin in
#define cout out

void solve()
{
    cout.precision(16);
    int n, k;
    cin >> n >> k;
    vector <pair <int, int> > arr(n);
    cin >> arr;
    sort(arr.rbegin(), arr.rend());
    vector <vector <int> > dp(n + 1, vector <int> (k + 1, -1000000000));
    dp[0][0] = 0;
    for (int i = 1; i <= n; ++i)
    {
        for (int j = 0; j <= k; ++j)
        {
            //if (j > i)
            //    continue;
            dp[i][j] = dp[i - 1][j];
            //cout << j << endl << (j == 1 ? arr[i - 1].fi * arr[i - 1].fi : 0) << endl;
            //cout << endl << dp[i][j] << endl;
            //cout << i << " " << j << endl;
            //cout << dp[i - 1][j - 1] + 2 * arr[i - 1].fi * arr[i - 1].se + (j == 1 ? arr[i - 1].fi * arr[i - 1].fi : 0) << endl;
            if (j > 0 && dp[i - 1][j] < dp[i - 1][j - 1] + 2 * arr[i - 1].fi * arr[i - 1].se + (j == 1 ? arr[i - 1].fi * arr[i - 1].fi : 0))
            {
                dp[i][j] = dp[i - 1][j - 1] + 2 * arr[i - 1].fi * arr[i - 1].se + (j == 1 ? arr[i - 1].fi * arr[i - 1].fi : 0);
            }
        }
    }
    //cout << "dp: " << dp << endl;
    cout << dp[n][k] * M_PI;
    return;
}

//#define out cout

signed main()
{
    int t;
    cin >> t;
    //std::cout << t << endl;
    for (int itt = 0; itt < t; ++itt)
    {
        //printf("%d", &itt);
        cout << "case #" << itt + 1 << ": ";
        solve();
        cout << endl;
    }
}
