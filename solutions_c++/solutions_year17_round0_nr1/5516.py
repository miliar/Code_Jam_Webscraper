#include <bits/stdc++.h>

using namespace std;

void solve() {
    string s;
    int k;
    cin >> s >> k;
    int ans = 0;
    for (int i = 0; i + k - 1 < s.size(); ++i) {
        if (s[i] == '-') {
            ++ans;
            for (int j = 0; j < k; ++j) {
                if (s[i + j] == '-')
                    s[i + j] = '+';
                else s[i + j] = '-';
            }
        }
    }
    int cnt = 0;
    for (int i = 0; i < s.size(); ++i) {
        if (s[i] == '-')
            ++cnt;
    }
    if (cnt) {
        cout << "IMPOSSIBLE\n";
    } else {
        cout << ans << endl;
    }
}


int main() {
#ifdef __APPLE__
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif
    int t = 1;
    cin >> t;
    for (int tt = 1; tt <= t; ++tt) {
        cerr << "Case #" << tt << " working" << endl;
        cout << "Case #" << tt << ": ";
        solve();
    }

    return 0;
}

