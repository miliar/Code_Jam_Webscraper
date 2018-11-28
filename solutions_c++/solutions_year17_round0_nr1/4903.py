#include <bits/stdc++.h>

using namespace std;

int ans;

char inv(char c)
{
    if (c == '-') return '+';
    return '-';
}

bool solve()
{
    string s;
    int k;

    cin >> s >> k;

    int n = s.size();
    int cc = 0;

    for (int i = 0; i + k <= n; ++i)
    {
        if (s[i] == '-')
        {
            for (int j = i; j < i + k; ++j)
                s[j] = inv(s[j]);
            cc++;
        }
    }
    ans = cc;
    for (int i = 0; i < n; i++)
        if (s[i] == '-')
            return false;
    return true;
}

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);

    int t;
    cin >> t;
    for (int i = 1; i <= t; i++)
    {
        bool s = solve();
        cout << "Case #" << i << ": ";
        if (!s) cout << "IMPOSSIBLE";
        else cout << ans;
        cout << '\n';
    }
    return 0;
}
