#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>
#include <iomanip>
using namespace std;

int solve() {
    int d, n;
    cin >> d >> n;

    long double max_time = 0;
    for (int i = 0; i < n; i++) {
        int pos, speed;
        cin >> pos >> speed;
        max_time = max(max_time, (long double)1.0 * (d - pos) / speed);
    }

    cout << fixed << setprecision(10);
    cout << d / max_time << endl;
}

int main()
{
    freopen("A.in", "r", stdin);
    freopen("A.out", "w", stdout);
    int t;
    cin >> t;
    for (int i = 1; i <= t; i++) {
        cout << "Case #" << i << ": ";
        solve();
    }
    return 0;
}
