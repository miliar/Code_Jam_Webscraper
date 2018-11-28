#include <bits/stdc++.h>

using namespace std;

void solve(int num) {
    string s; int k;
    cin >> s >> k;
    int n = s.size();

    int ans = 0;
    for (int i = 0; i <= n - k; ++i) {
        if (s[i] == '-') {
            ++ans;
            for (int j = i; j < i + k; ++j) {
                if (s[j] == '-') s[j] = '+';
                else s[j] = '-';
            }
        }
    }
    if (count(s.begin(), s.end(), '-')) {
        cout << "Case #" << num << ": " << "IMPOSSIBLE\n";
    } else {
        cout << "Case #" << num << ": " << ans << "\n";
    }
}

signed main() {
    ios_base::sync_with_stdio(false); cin.tie(0);
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    int t;
    cin >> t;
    for (int i = 1; i <= t; ++i) {
        solve(i);
    }
}
