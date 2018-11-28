#include <iostream>
#include <vector>

using namespace std;

void solve() {
    double d = 0;
    cin >> d;
    int n = 0;
    cin >> n;
    vector < pair < long double, long double > > s;
    double ans = 0;
    for (int i = 0; i < n; ++i) {
        double c1, c2;
        cin >> c1 >> c2;
        c1 = d - c1;
        ans = max(ans, c1 / c2);
    }
    cout.precision(7);
    ans = d / ans;
    cout << fixed << ans << endl;
}

int main() {
    int test = 0;
    cin >> test;
    for (int t_id = 1; t_id <= test; t_id++) {
        cout << "Case #" << t_id << ": ";
        solve();
    }
    return 0;
}