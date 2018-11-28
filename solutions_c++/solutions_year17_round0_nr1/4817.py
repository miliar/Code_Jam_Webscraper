#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main() {
    int T; cin >> T;
    for (int t = 1; t <= T; t++) {
        string s; cin >> s;
        int k; cin >> k;
        int a[1001];
        int n = s.size();
        for (int i = 0; i < n; i++) {
            if (s[i] == '-') {
                a[i] = 0;
            }
            else {
                a[i] = 1;
            }
        }
        int cnt = 0;
        for (int i = 0; i <= n-k; i++) {
            if (a[i] == 0) {
                cnt++;
                for (int j = i; j < i+k; j++) {
                    a[j] ^= 1;
                }
            }
        }
        bool ok = 1;
        for (int i = 0; i < n; i++) {
            if (a[i] == 0) {
                ok = 0;
                break;
            }
        }
        if (ok) {
            cout << "Case #" << t << ": " << cnt << '\n';
        }
        else {
            cout << "Case #" << t << ": IMPOSSIBLE\n";
        }
    }
    return 0;
}   