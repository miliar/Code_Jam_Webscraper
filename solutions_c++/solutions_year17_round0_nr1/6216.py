#include <iostream>
#include <vector>
#include <fstream>

using namespace std;

int solve(const string &s, int k) {
    int n = s.size();
    vector<int> b(n + 1, 0);
    int ans = 0;
    int now = 0;
    for (int i = 0; i < n; ++i) {
        now += b[i];
        bool ok = s[i] == '+';
        if (now % 2) {
            ok = !ok;
        }
        if (!ok) {
            if (i + k - 1 >= n) {
                return -1;
            }
            ++ans;
            b[i + 1]++;
            b[i + k]--;
        }
    }
    return ans;
}

int main() {
    freopen("A-large.in", "r", stdin);
    freopen("test.out", "w", stdout);
    int test;
    cin >> test;
    for (int tt = 0; tt < test; ++tt) {
        cout << "Case #" << tt + 1 << ": ";
        string s;
        cin >> s;
        int k;
        cin >> k;
        int ans = solve(s, k);
        if (ans == -1) {
            cout << "IMPOSSIBLE\n";
        } else {
            cout << ans << "\n";
        }
    }
    return 0;
}
//code.google.com/codejam
