#include <bits/stdc++.h>
using namespace std;

int main() {
    int T;
    cin >> T;
    for (int t = 1; t <= T; t++) {
        string s;
        int k;
        cin >> s >> k;
        int ans = 0;
        for (size_t i = 0; i < s.size(); i++) {
            if (s[i] == '-') {
                if (i + k <= s.size()) {
                    ans++;
                    for (int j = 0; j < k; j++) {
                        s[i + j] = (s[i + j] == '-' ? '+' : '-');
                    }
                } else {
                    ans = -1;
                    break;
                }
            }
        }
        if (ans != -1) {
            cout << "Case #" << t << ": " << ans << endl;
        } else {
            cout << "Case #" << t << ": IMPOSSIBLE" << endl;
        }
    }
}
