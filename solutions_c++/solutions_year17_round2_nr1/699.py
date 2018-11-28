#include <bits/stdc++.h>

using namespace std;
typedef long long li;

void solve() {
    static int casenum = 1;
    li d, n;
    cin >> d >> n;

    double latest = 0;
    for (int i = 0; i < n; ++i) {
        li k, s;
        cin >> k >> s;
        latest = max(latest, (double) (d - k) / s);
    }
    cout.precision(16);
    cout << "Case #" << casenum << ": " << fixed << d / latest << endl;
    casenum += 1;
}

int main() {
    li t;
    cin >> t;
    while (t--) {
        solve();
    }
    return 0;
}