#include <bits/stdc++.h>
#define ll long long
using namespace std;

string s;

int k;

int main()
{
#ifdef LOCAL
    freopen("xxx.in", "r", stdin);
    freopen("xxx.out", "w", stdout);
#endif
    int t;
    cin >> t;
    for (int tt = 0; tt < t; ++tt) {
        cin >> s >> k;
        int ans = 0;
        for (int i = 0; i <= (int)s.size() - k; ++i) {
            if (s[i] == '-') {
                ++ans;
                for (int j = i; j < i + k; ++j) {
                    if (s[j] == '-')
                        s[j] = '+';
                    else
                        s[j] = '-';
                }
            }
        }
        bool f = true;
        for (int i = (int)s.size() - k + 1; i < (int)s.size(); ++i) {
            if (s[i] == '-')
                f = false;
        }
        if (f)
            cout << "Case #" << tt + 1 << ": " << ans << "\n";
        else
            cout << "Case #" << tt + 1 << ": IMPOSSIBLE" << "\n";
    }
    return 0;
}