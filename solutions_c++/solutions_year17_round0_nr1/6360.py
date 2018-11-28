#include <bits/stdc++.h>
using namespace std;

string s;
int t, k, cnt = 0, ans;
bool fl;

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie();
    freopen ("input.txt", "r", stdin);
    freopen ("output.txt", "w", stdout);
    cin >> t;
    for (int ii = 0; ii < t; ++ii)
    {
        cin >> s >> k;
        fl = 1;
        ans = 0;
        for (int i = 0; i < (int)s.size(); ++i)
        {
            if (i + k > (int)s.size())
            {
                for (int j = i; j < (int)s.size(); ++j)
                {
                    if (s[j] == '-') fl = 0;
                }
                break;
            }
            if (s[i] == '-')
            {
                for (int j = i; j < i + k; ++j)
                {
                     if (s[j] == '-') s[j] = '+';
                        else s[j] = '-';
                }
                ans++;
            }

        }
        if (fl) cout << "Case #" << ii  + 1 << ": " << ans << "\n";
        else cout << "Case #" << ii + 1 << ": " << "IMPOSSIBLE\n";
    }
}
