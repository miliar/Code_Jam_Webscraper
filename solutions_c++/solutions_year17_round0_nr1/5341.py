#include <bits/stdc++.h>

using namespace std;

const int INF = 1e9;

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("1.out", "w", stdout);

    int tests;
    cin >> tests;

    for (int testNum = 1; testNum <= tests; ++testNum)
    {
        string s;
        cin >> s;
        int k, n, ans = 0;
        cin >> k;
        n = s.size();

        for (int i = 0; i  + k - 1 < n; ++i)
            if (s[i] == '-')
        {
            ++ans;
            for (int j = i; j < i + k; ++j)
            {
                if (s[j] == '-') s[j] = '+';
                else s[j] = '-';
            }
        }

        for (int i = 0; i < n; ++i)
            if (s[i] != '+') ans = INF;

        cout << "Case #" << testNum << ": ";
        if (ans == INF) cout << "IMPOSSIBLE";
                   else cout << ans;
        cout  << "\n";
    }
    return 0;
}
