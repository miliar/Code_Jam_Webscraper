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

ifstream in("C-small-2-attempt0.in");
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
    int n, k;
    cin >> n >> k;
    multiset <int> s;
    s.insert(n);
    for (int i = 0; i < k - 1; ++i)
    {
        int a = *--s.end();
        s.erase(--s.end());
        int l = (a - 1) / 2, r = a / 2;
        s.insert(l);
        s.insert(r);
    }
    int a = *--s.end();
    int l = (a - 1) / 2, r = a / 2;
    cout << r << " " << l << endl;
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
