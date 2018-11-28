#include <iostream>
#include <iomanip>
#include <vector>

using namespace std;

int main() {
    int T; cin >> T; int test_id = 0;
    while (test_id < T) { test_id++;
        cout << "Case #" << test_id << ": ";
        int n, k;
        cin >> n >> k;
        vector<long double> p(n);
        long double u; cin >> u;
        for(int i = 0; i < n; i++) cin >> p[i];
        sort(p.begin(), p.end());
        p.push_back(1);
        for(int i = 0; i < n; i++) {
            long double v = max(min(u, (p[i + 1] - p[i]) * (i + 1)), (long double)0.0);
            u -= v;
            for(int j = 0; j <= i; j++)
                p[j] += v / (i + 1);
        }
        long double ans = 1;
        for(int i = 0; i < n; i++) {
            ans *= p[i];
        }
        cout << fixed << setprecision(12) << ans << endl;
    }
}
