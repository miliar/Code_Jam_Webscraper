#include <stdio.h>
#include <vector>
#include <set>
#include <iostream>

using namespace std;

int a[2010];

void solve(int idx) {
    memset(a, 0, sizeof a);
    string s;
    int k;
    cin >> s >> k;
    int n = s.length();
    int bal = 0;
    int ans = 0;
    for (int i = 0; i <= n - k; ++i) {
        bal ^= a[i];
        if (bal == 1) {
            if (s[i] == '+') {
                s[i] = '-';
            } else {
                s[i] = '+';
            }
        }
        if (s[i] == '-') {
            ++ans;
            bal ^= 1;
            a[i + k] ^= 1;
            s[i] = '+';
        }
    }
    cout << "Case #" << idx << ": ";
    for (int i = n - k + 1; i < n; ++i) {
        bal ^= a[i];
        if (bal == 1) {
            if (s[i] == '+') {
                s[i] = '-';
            } else {
                s[i] = '+';
            }
        }
        if (s[i] == '-') {
            cout << "IMPOSSIBLE\n";
            return;
        }
    }
    cout << ans << '\n';
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    int t;
    cin >> t;
    for (int i = 1; i <= t; ++i) {
        solve(i);
    }
    return 0;
}
