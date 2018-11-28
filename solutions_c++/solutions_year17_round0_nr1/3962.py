#include <iostream>
#include <vector>
using namespace std;
int main() {
    int T; cin >> T;
    for (int t = 1; t <= T; t += 1) {
        string s; cin >> s;
        int k; cin >> k;
        int n = (int)s.size();
        vector<int> e(n);
        for (int i = 0; i < n; i += 1) {
            if (s[i] == '+') {
                e[i] = 1;
            } else {
                e[i] = 0;
            }
        }

        int result = 0;
        for (int i = 0; i + k <= n; i += 1) {
            if (e[i] == 0) {
                result += 1;
                for (int j = 0; j < k; j += 1) {
                    e[i + j] ^= 1;
                }
            }
        }

        bool ok = true;
        for (auto itr : e) {
            ok &= itr;
        }

        if (ok) {
            cout << "Case #" << t << ": " << result << '\n';
        } else {
            cout << "Case #" << t << ": " << "IMPOSSIBLE" << '\n';
        }
    }
}
