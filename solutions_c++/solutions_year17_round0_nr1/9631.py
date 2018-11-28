#include <bits/stdc++.h>

using namespace std;

int b[(int)1e5 + 10];

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("A.out", "w", stdout);
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    int qwe;
    cin >> qwe;
    for (int qq = 0; qq < qwe; qq++)
    {
        string s;
        int a;
        cin >> s >> a;
        int n = s.size();
        fill(b, b + n + 1, 0);
        int c = 0;
        int ans = 0;
        bool d = 0;
        for (int i = 0; i < n; i++)
        {
            c -= b[i];
            if (c % 2)
                s[i] = '+' + '-' - s[i];
            if (s[i] == '-')
            {
                if (i + a <= n)
                {
                    s[i] = '+';
                    c++;
                    ans++;
                    b[i + a]++;
                }
                else
                    d = 1;
            }
        }
        cout << "Case #" << qq + 1 << ": ";
        if (d)
            cout << "IMPOSSIBLE\n";
        else
            cout << ans << "\n";
    }
    return 0;
}
