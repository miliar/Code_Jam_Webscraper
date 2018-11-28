#include <iostream>
#include <vector>

using namespace std;

int main() {
    int t;
    cin >> t;
    
    for (int kase = 1; kase <= t; kase++) {
        int k;
        string s;
        cin >> s;
        cin >> k;
        int n = s.length();
        vector<int> f(n, 0);
        int sum = 0;
        bool success = true;
        for (int i = 0; i + k <= n; i++) {
            int odd = (s[i] == '+' ? 0 : 1);
            if ((sum + odd) % 2 != 0) {
                f[i] = 1;
                sum++;
            }
            if (i - k + 1 >= 0) {
                sum -= f[i - k + 1];
            }
        }
        for (int i = n - k + 1; i < n; i++) {
            int odd = (s[i] == '+' ? 0 : 1);
            if ((sum + odd) % 2 != 0) {
                success = false;
                break;
            }
            if (i - k + 1 >= 0) {
                sum -= f[i - k + 1];
            }
        }
        int ans = 0;
        for (int i = 0; i < n; i++) {
            ans += f[i];
        }
        if (success) {
            cout << "Case #" << kase << ": " << ans << endl;
        } else {
            cout << "Case #" << kase << ": " << "IMPOSSIBLE" << endl;
        }
    }
}