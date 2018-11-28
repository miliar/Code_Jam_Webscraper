#include <algorithm>
#include <iomanip>
#include <iostream>
#include <map>
#include <set>
#include <vector>
using namespace std;

void solve()
{
    double d;
    int n;
    cin >> d >> n;

    vector<pair<double, double> > hs(n);
    for (auto& h : hs)
        cin >> h.first >> h.second;

    // sort(h.begin(), h.end());
    double last = 0;
    for (auto& h : hs) {
        double cur = (d - h.first) / h.second;
        last = max(last, cur);
    }

    double ans = d / last;
    cout << setiosflags(ios::fixed) << setprecision(12) << ans << endl;
}

int main()
{
    int t;
    cin >> t;
    for (int i = 0; i < t; i++) {
        cout << "Case #" << i + 1 << ": ";
        solve();
    }
    return 0;
}