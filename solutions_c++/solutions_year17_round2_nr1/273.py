#include <bits/stdc++.h>

using namespace std;

using ll = long long;

struct Solver {
    void run() {
        ll d;
        int n;
        cin >> d >> n;
        double ans = 1e100;
        for (int i = 0; i < n; i++) {
            ll k, s;
            cin >> k >> s;
            double t = (d - k) * 1.0 / s;
            ans = min(ans, d / t);
        }
        cout << ans << endl;
    }
};

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(nullptr);
    cout.setf(ios::fixed);
    cout.precision(20);

    int ts;
    cin >> ts;
    for (int t = 1; t <= ts; t++) {
        cout << "Case #" << t << ": ";
        Solver solver;
        solver.run();
    }
}
