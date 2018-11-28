#include <iostream>
#include <stdio.h>

using namespace std;

int main() {
    freopen("/home/nimloth/coding/6sem/codejam/A-large (3).in", "r", stdin);
    freopen("output.txt", "w", stdout);
    int T;
    cin >> T;
    for (int t = 0; t < T; t++) {
        string s;
        int k;
        cin >> s >> k;
        int ans = 0;
        for (int i = 0; i < s.length(); i++) {
            if (s[i] == '-') {
                for (int j = 0; j < k; j++) {
                    if (i + j > s.length() - 1) {
                        ans = -1;
                    } else {
                        if (s[i + j] == '-') {
                            s[i + j] = '+';
                        } else {
                            s[i + j] = '-';
                        }
                    }
                }
                if (ans == -1) {
                    break;
                } else {
                    ans = ans + 1;
                }
            }
        }
        if (ans != -1) {
            cout << "Case #" << t + 1 << ": " << ans << "\n";
        } else {
            cout << "Case #" << t + 1 << ": " << "IMPOSSIBLE" << "\n";
        }
    }
    return 0;
}