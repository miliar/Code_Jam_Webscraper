#include <bits/stdc++.h>

using namespace std;

#define int int64_t
#define endl '\n'
#define fi first
#define se second

template <typename T1, typename T2>
ostream & operator << (ostream & out, pair <T1, T2> & p)
{
    out << "{" << p.fi << ", " << p.se << "}";
    return out;
}

template <typename T1, typename T2>
istream & operator >> (istream & in, pair <T1, T2> & p)
{
    in >> p.fi >> p.se;
    return in;
}

template <typename T>
ostream & operator << (ostream & out, vector <T> & arr)
{
    for (auto x : arr)
        out << x << " ";
        out << endl;
    return out;
}

template <typename T>
istream & operator >> (istream & in, vector <T> & arr)
{
    for (auto & i : arr)
        in >> i;
    return in;
}

ifstream in("A-large.in");
ofstream out("output.txt");

#define cin in
#define cout out

void solve()
{
    string s;
    cin >> s;
    int k;
    cin >> k;
    int ans = 0;
    int n = s.size();
    for (int i = 0; i < n - k + 1; ++i)
    {
        if (s[i] == '-')
        {
            ans++;
            for (int j = i; j < i + k; ++j)
                s[j] = '+' + '-' - s[j];
        }
    }
    for (int i = 0; i < s.size(); ++i)
    {
        if (s[i] == '-')
        {
            cout << "IMPOSSIBLE" << endl;
            return;
        }
    }
    cout << ans << endl;
    return;
}

signed main()
{
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    int t;
    cin >> t;
    for (int i = 0; i < t; ++i)
    {
        cout << "Case #" << i + 1 << ": ";
        solve();
    }
    return 0;
}
