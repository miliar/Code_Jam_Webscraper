#include <iostream>
#include <bits/stdc++.h>

using namespace std;
using ll = long long;

const string impos = "IMPOSSIBLE";

void flip(string &s, int l, int k)
{
    for (int i = l; i < l + k; i++)
    {
        if (s[i] == '-')
            s[i] = '+';
        else
            s[i] = '-';
    }
}

int main(int argc, char *argv[])
{
    cin.tie(0);
    cin.sync_with_stdio(false);
    freopen("a1.in", "r", stdin);
    freopen("a.out", "w", stdout);
    ll t;
    cin >> t;
    for (int qq = 1; qq <= t; qq++)
    {
        cout << "Case #" << qq << ": ";
        string s;
        int k;
        cin >> s >> k;
        int n = s.length();
        string sres(n, '+');
        int res = 0;
        for (int i = 0; i <= n - k; i++)
        {
            if (s[i] == '-')
            {
                flip(s, i, k);
                res++;
            }
        }
        if (s == sres)
            cout << res;
        else
            cout << impos;
        cout << '\n';
    }
    return 0;
}
