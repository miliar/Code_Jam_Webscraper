#include <bits/stdc++.h>

using namespace std;

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int t;
    cin >> t;
    for (int tt = 1; tt <= t; ++tt) {
        string s;
        int k;
        cin >> s >> k;
        static int a[1010];
        int bal = 0, kol = 0;
        fill(a, a + s.size() + 2, 0);
        for (int i = 0; i < s.size(); ++i) {
            bal -= a[i];
            if (i + k <= s.size()) {
                if (s[i] == '-' && bal % 2 == 0)  {
                    bal++;
                    kol++;
                    a[i + k]++;
                } else if (s[i] == '+' && bal % 2 == 1) {
                    bal++;
                    kol++;
                    a[i + k]++;
                }
            }
            if (bal % 2) {
                s[i] = s[i] == '-' ? '+' : '-';
            }
        }
        cout << "Case #" << tt << ": ";
        if (find(s.begin(), s.end(), '-') != s.end()) {
            cout << "IMPOSSIBLE\n";
        } else {
            cout << kol << "\n";
        }
    }
}
