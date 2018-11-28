#include <set>
#include <map>
#include <vector>
#include <iomanip>
#include <iostream>
#include <algorithm>

using namespace std;

typedef long long LL;
void solve(int cs) {
    LL n, d;
    cin >> d >> n;
    vector < pair <LL, LL> > h(n);
    vector <double> t(n + 1, 0);
    for (int i = 0; i < n; ++i) {
        cin >> h[i].first >> h[i].second;
    }
    sort(h.begin(), h.end());
    for (LL i = n - 1; i >= 0; --i) {
        t[i] = max(t[i + 1], 1.0 * (d - h[i].first) / h[i].second);
    }
    cout << setprecision(8) << std::fixed;
    cout << "Case #" << cs << ": " << d / t[0] << endl;
}
int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    int t;
    cin >> t;
    for (int i = 1; i <= t; ++i) {
        solve(i);
    }
    return 0;
}
