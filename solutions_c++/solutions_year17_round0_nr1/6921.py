#include <bits/stdc++.h>

#define sz(s) ((int) s.size ())

using namespace std;

int main () {
    #define name "A-large"
    freopen (name".in", "r", stdin);
    freopen (name".out", "w", stdout);
    int t; cin >> t;
    for (int tt = 1; tt <= t; tt++) {
        string s; cin >> s;
        int k; cin >> k;
        int n = sz (s);
        int ans = 0;
        for (int i = 0; i < n - k + 1; i++) {
            if (s[i] == '-') {
                ans++;
                for (int j = i; j < i + k; j++) {
                    if (s[j] == '-') {
                        s[j] = '+';
                    } else {
                        s[j] = '-';
                    }
                }
            }
        }
        bool f = 0;
        for (int i = 0; i < n; i++) {
            if (s[i] == '-') {
                f = 1;
                break;
            }
        }
        cout << "Case #" << tt << ": ";
        if (!f) {
            cout << ans << endl;
        } else {
            cout << "IMPOSSIBLE" << endl;
        }
    }
    return 0;
}
