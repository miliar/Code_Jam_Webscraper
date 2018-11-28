#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

int main() {
    freopen("in.in", "r", stdin);
    freopen("out.out", "w", stdout);

    int t;
    cin >> t;

    string s;
    int n, cnt;

    for (int k = 1; k <= t; ++k) {
        cin >> s >> n;
        cnt = 0;

        for (int i = 0; i <= s.size() - n; ++i) {
            if (s[i] == '-') {
                for (int j = 0; j < n; ++j) {
                    if (s[i + j] == '-') {
                        s[i + j] = '+';
                    } else {
                        s[i + j] = '-';
                    }
                }

                ++cnt;
            }
        }

        for (int i = s.size() - n + 1; i < s.size(); ++i) {
            if (s[i] == '-') {
                cnt = -1;
            }
        }

        cout << "Case #" << k << ": ";
        if (cnt == -1) {
            cout << "IMPOSSIBLE" << endl;
        } else {
            cout << cnt << endl;
        }
    }

    return 0;
}
