#include <iostream>
#include <string>
#include <cstdio>

using namespace std;

int main() {
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    int n;
    cin >> n;
    for (int qwe = 1; qwe <= n; ++qwe) {
        string s;
        cin >> s;
        int k;
        cin >> k;
        int ans = 0;
        for (int j = 0; j + k - 1 < s.size(); ++j) {
            if (s[j] == '-') {
                ++ans;
                for (int i = 0; i < k; ++i) {
                    if (s[i + j] == '-') {
                        s[i + j] = '+';
                    } else {
                        s[i + j] = '-';
                    }
                }
            }
        }
        bool fl = 0;
        for (int i = 0; i < s.size(); ++i) {
            if (s[i] == '-') {
                fl = 1;
                break;
            }
        }
        cout << "Case #" << qwe << ": ";
        if (fl) {
            cout << "IMPOSSIBLE" << endl;
        } else {
            cout << ans << endl;
        }
    }
    return 0;
}
