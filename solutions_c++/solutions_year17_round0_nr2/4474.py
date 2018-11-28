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

const int INF = 1000000000000000000;

ifstream in("B-large.in");
ofstream out("output.txt");

#define cin in
#define cout out

bool check(string & s)
{
    for (int i = 1; i < s.size(); ++i)
    {
        if (s[i] < s[i - 1])
            return false;
    }
    return true;
}

void solve()
{
    string s;
    cin >> s;
    if (check(s))
    {
        cout << s << endl;
        return;
    }
    string ans(s.size(), '0');
    for (int i = s.size() - 1; i >= 0; --i)
    {
        string t = s;
        if (s[i] == '0')
            continue;
        t[i] = s[i] - 1;
        for (int j = i + 1; j < s.size(); ++j)
            t[j] = '9';
        if (check(t))
        {
            ans = max(ans, t);
        }
    }
    while (ans.size() > 1 && ans[0] == '0')
        ans.erase(ans.begin());
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
