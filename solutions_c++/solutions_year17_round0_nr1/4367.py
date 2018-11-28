#include <bits/stdc++.h>

using namespace std;

inline void solve() {
    string s;
    int k;
    cin >> s >> k;
    int n = (int)s.size();
    int ans = 0;
    for (int i = 0; i < n; i++)
        if (s[i] != '+') {
            if (i + k > n) {
                cout << "IMPOSSIBLE" << endl;
                return;
            } else {
                ans++;
                for (int j = 0; j < k; j++)
                    s[i + j] = (s[i + j] == '+' ? '-' : '+');
            }
        }
    cout << ans << endl;
}

int main() {
    ios_base::sync_with_stdio(false);

#ifdef SCHEMTSCHIK
    //freopen("input.txt", "r", stdin);
    //freopen("output.txt", "w", stdout);
#else

#endif

    int T;
    cin >> T;

    for (int I = 0; I < T; I++) {
        cout << "Case #" << I + 1 << ": ";
        solve();
    }

    return 0;
}
