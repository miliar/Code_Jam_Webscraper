#include "bits/stdc++.h"
using namespace std;

int main() {
    freopen ("inp.in", "r", stdin);
    freopen ("A.out", "w", stdout);
    int t; cin >> t;
    for (int qq = 1; qq <= t; qq++) {
        string s; cin >> s;
        int k; cin >> k;
        int n = s.size();
        int ans = 0;
        for (int i = 0; i < n - k + 1; i++) {
            if (s[i] == '-') {
                ans++;
                for (int j = i; j < i + k; j++)
                    s[j] = (s[j] == '-') ? ('+') : ('-');
            }
        }
        bool rekt = false;
        for (int i = 0; i < n; i++) {
            if (s[i] == '-') {
                rekt = true;
            }
        }
        cout << "Case #" << qq << ": ";
        if (rekt) {
            cout << "IMPOSSIBLE\n";
        } else {
            cout << ans << "\n";
        }
    }
}