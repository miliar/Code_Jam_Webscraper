#include <bits/stdc++.h>

using namespace std;

const int maxn = 200200;

int main() {
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);

    ios_base::sync_with_stdio(false);
    cin.tie(0);

    int t;
    cin >> t;
    for (int z = 0; z < t; ++z) {
        string s;
        cin >> s;
        int k;
        cin >> k;
        bool ok = true;
        int n = s.size();
        int ans = 0;
        for (int i = 0; i < n; ++i) {
            if (s[i] == '-') {
                if (n - i < k) {
                    ok = false;
                } else {
                    for (int j = i; j < i + k; ++j) {
                        if (s[j] == '-') s[j] = '+';
                        else s[j] = '-';
                    }
                    ans++;
                }
            }
        }
        cout << "Case #" << z + 1 << ": ";
        if (ok) {
            cout << ans << "\n";
        } else {
            cout << "IMPOSSIBLE\n";
        }
    }

    return 0;
}
