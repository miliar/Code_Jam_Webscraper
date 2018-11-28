#include <iostream>
#include <vector>
#include <deque>
#include <algorithm>
#include <queue>
#include <iomanip>
#include <set>
#include <cmath>
#include <map>

using namespace std;

typedef long long ll;


void solve() {
    ll n, d;
    cin >> d >> n;
    double ans = 0;
    for (int i = 0; i < n; ++i) {
        double k, s;
        cin >> k >> s;
        ans = max(ans, (d - k) / s);
    }
    cout << d / ans << endl;
}

int main() {
    iostream::sync_with_stdio(false);
    cout.precision(20);
    int t;
    cin >> t;
    for (int i = 1; i <= t; ++i)
        cout << "Case #" << i << ": ", solve();
}

