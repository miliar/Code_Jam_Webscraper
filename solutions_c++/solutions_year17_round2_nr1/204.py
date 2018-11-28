#include <bits/stdc++.h>

using namespace std;

double solve() {
    int d, n;
    cin >> d >> n;

    double max_time = 0.0;

    for (int i = 0; i < n; i++) {
        int k, s;
        cin >> k >> s;
        double time = double(d - k) / s;
        max_time = max(max_time, time);
    }

    return d / max_time;
}

int main() {
    int t;
    cin >> t;

    cout << fixed;
    cout.precision(12);

    for (int c = 1; c <= t; c++) {
        cout << "Case #" << c << ": " << solve() << endl;
    }
}
