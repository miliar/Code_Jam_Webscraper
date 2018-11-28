#include <bits/stdc++.h>

using namespace std;

bool good(string & s)
{
    for(int i = 0; i < s.size(); ++i)
        if(s[i] == '-')
            return false;
    return true;
}

void make(string & s, int l, int len)
{
    for(int i = l; i <= l + len - 1; ++i)
    {
        if(s[i] == '-')
            s[i] = '+';
        else
            s[i] = '-';
    }
}

void solve(int T)
{
    cout << "Case #" << T << ": ";
    string s;
    int k;
    cin >> s >> k;

    int res = 0;

    for(int i = 0; i + k - 1 < s.size(); ++i)
        if(s[i] == '-')
        {
            make(s, i, k);
            ++res;
        }

    if(good(s))
        cout << res << '\n';
    else
        cout << "IMPOSSIBLE\n";
    return;
}

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    int t;
    cin >> t;
    for(int t1 = 1; t1 <= t; ++t1)
        solve(t1);
    return 0;
}
