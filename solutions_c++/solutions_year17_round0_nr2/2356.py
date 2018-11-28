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

ll ten[19];

int main(int argc, char *argv[])
{
    cin.tie(0);
    cin.sync_with_stdio(false);
    freopen("b1.in", "r", stdin);
    freopen("b.out", "w", stdout);
    ten[0] = 1;
    for (int i = 1; i < 19; i++)
    {
        ten[i] = ten[i - 1] * 10;
    }
    ll t;
    cin >> t;
    for (int qq = 1; qq <= t; qq++)
    {
        cout << "Case #" << qq << ": ";
        ll n;
        cin >> n;
        string s = to_string(n);
        int i = 0;
        for (i = 0; i < s.length() - 1; i++)
        {
            if (s[i] > s[i + 1])
                break;
        }
        if (i == s.length() - 1)
        {
            cout << n << '\n';
            continue;
        }
        int j = i;
        for (; j > 0; j--)
        {
            if (s[j] != s[j - 1])
                break;
        }
        ll n1 = n - (n % ten[s.length() - j - 1]) - 1;
        cout << n1 << '\n';
    }
    return 0;
}
