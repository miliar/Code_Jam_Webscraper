#include <bits/stdc++.h>
using namespace std;

int T;
long long N, K;
string s;

int main() {
    #ifndef ONLINE_JUDGE
    freopen("a.in", "r", stdin);
    freopen("a.out", "w", stdout);
    #endif // ONLINE_JUDGE

    cin >> T;
    for (int q = 1; q <= T; ++q) {
        cin >> s >> K;
        int ok = 1, sol = 0;

        for (int i = 0; i < s.size(); ++i) {
            if (s[i] == '-' && i + K - 1 < s.size()) {
                int limit = i + K - 1;
                for (int j = i; j <= limit; ++j) {
                    if (s[j] == '-') {
                        s[j] = '+';
                    } else {
                        s[j] = '-';
                    }
                }

                ++sol;
            }
        }

        for (int i = 0; i < s.size(); ++i) {
            if (s[i] == '-') {
                ok = 0;
            }
        }

        cout << "Case #" << q << ": ";
        if (!ok) {
            cout << "IMPOSSIBLE\n";
        } else {
            cout << sol << '\n';
        }
    }
    return 0;
}
