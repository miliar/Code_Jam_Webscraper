#include <bits/stdc++.h>

using namespace std;

#define int long long

bool good(int x) {
    int prev = 10;
    while (x > 0) {
        if (x % 10 > prev) {
            return false;
        }
        prev = x % 10;
        x /= 10;
    }
    return true;
}

void solve(int case_number) {
    int n;
    cin >> n;
    for (int i = n; i >= 1; --i) {
        if (good(i)) {
            cout << "Case #" << case_number << ": " << i << '\n';
            return;
        }
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
