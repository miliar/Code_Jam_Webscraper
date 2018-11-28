#include <bits/stdc++.h>

using namespace std;

void solve(int t) {
    double d;
    int n;
    cin >> d >> n;
    double last = 0;
    for (int i = 0; i < n; ++i) {
        double k, s;
        cin >> k >> s;
        last = max(last, (d - k) / s);
    }
    cout << "Case #" << t << ": " << setprecision(32) << d / last << endl;
}

int main() {
    freopen("A-large.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    int t;
    cin >> t;
    for (int i = 1; i <= t; ++i) {
        solve(i);
    }
}
