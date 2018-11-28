#include <bits/stdc++.h>

using namespace std;

struct Solution {
    void run() {
        string s;
        int k;
        cin >> s >> k;
        int n = (int)s.length();
        int ans = 0;
        for (int i = 0; i + k <= n; i++)
            if (s[i] == '-') {
                ans++;
                for (int j = i; j < i + k; j++)
                    s[j] = s[j] == '-' ? '+' : '-';
            }
        for (int i = 0; i < n; i++)
            if (s[i] == '-') {
                cout << "IMPOSSIBLE\n";
                return;
            }
        cout << ans << "\n";
    }
};

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(nullptr);
    cout.setf(ios::fixed);
    cout.precision(10);
    int tests;
    cin >> tests;
    for (int t = 1; t <= tests; t++) {
        cout << "Case #" << t << ": ";
        Solution sol;
        sol.run();
    }
}
