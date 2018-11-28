#include <bits/stdc++.h>
using namespace std;

char rev(char x) {
    if (x == '+') return '-';
    if (x == '-') return '+';
    assert(false);
}

int main() {
    int T; cin >> T;
    string s;
    for (int _ = 1; _ <= T; ++_) {
        int ans = 0, k = -1;
        cin >> s >> k;
        for (int pl = 0; pl + k <= int(s.length()); ++pl) {
            if (s[pl] == '-') {
                ans += 1;
                for (int add = 0; add < k; ++add) {
                    s[pl + add] = rev(s[pl + add]);
                }
            }
        }
        bool ok = true;
        for (size_t pl = 0; pl < s.length(); ++pl) {
            if (s[pl] != '+') {
                ok = false;
                break;
            }
        }
        cout << "Case #" << _ << ": ";
        if (!ok) {
            cout << "IMPOSSIBLE" << endl;
        } else {
            cout << ans << endl;
        }
    }
}
