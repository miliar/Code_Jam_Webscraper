#include <bits/stdc++.h>

using namespace std;

int tc, k;
string s;

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    ios::sync_with_stdio(0);
    cin.tie(0);
    cin >> tc;
    for (int t = 0; t < tc; t++) {
        cout << "Case #" << t + 1 << ": ";
        cin >> s >> k;
        int cnt = 0;
        for (int i = 0; i + k <= s.size(); i++) {
            if (s[i] == '-') {
                for (int j = i; j < i + k; j++) {
                    if (s[j] == '-') {
                        s[j] = '+';
                    } else {
                        s[j] = '-';
                    }
                }
                cnt++;
            }
        }
        for (int i = 0; i < s.size(); i++) {
            if (s[i] == '-') {
                cout << "IMPOSSIBLE\n";
                break;
            }
            if (i == s.size() - 1) {
                cout << cnt << "\n";
            }
        }
    }
}
