#include <bits/stdc++.h>

using namespace std;

using ll = long long;
using ld = long double;

int main() {
    #if __APPLE__
        freopen("in", "r", stdin);
        freopen("out", "w", stdout);
    #endif
    ios::sync_with_stdio(0);
    cin.tie(nullptr);
    int t;
    cin >> t;
    int r = 0;
    while (t--) {
        ++r;
        string s;
        cin >> s;
        string z = s;
        int x;
        cin >> x;
        int res = 0;
        for (int i = 0; i + x - 1 < s.size(); ++i) {
            if (s[i] == '-') {
                ++res;
                for (int j = i; j < i + x; ++j) {
                    if (s[j] == '-') s[j] = '+';
                    else s[j] = '-';
                }
            }
        }
        bool f = true, f1 = true;;
        cout << "Case #" << r << ": ";
        for (char c : s) {
            if (c == '-') f = false;
        }
        int res1 = 0;
        s = z;
        reverse(s.begin(), s.end());
        for (int i = 0; i + x - 1 < s.size(); ++i) {
            if (s[i] == '-') {
                ++res1;
                for (int j = i; j < i + x; ++j) {
                    if (s[j] == '-') s[j] = '+';
                    else s[j] = '-';
                }
            }
        }
        for (char c : s) {
            if (c == '-') f1 = false;
        }
        if (f < f1) {
            res = res1;
            f = f1;
        } else {
            res = min(res, res1);
        }
        if (!f) cout << "IMPOSSIBLE\n";
        else cout << res << '\n';
    }
}