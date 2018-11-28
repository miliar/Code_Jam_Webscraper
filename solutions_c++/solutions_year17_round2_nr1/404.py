#include <iostream>
#include <cstdio>
#include <algorithm>
#include <set>
#include <map>
#include <queue>
#include <deque>
#include <vector>
#include <string>
#include <iomanip>
#include <functional>
#include <cassert>
#include <cstdlib>
#include <cmath>
#include <cstring>
using namespace std;


typedef long long lint, ll;
typedef long double ldouble, ld;

#ifdef LOCAL
	#define dbg(expr) cerr << "[" << __LINE__ << "] " << #expr << " = " << (expr) << '\n';
#else
	#define dbg(expr) (void) 0;
#endif


const double inf = 1e18;

void solve(int test_case) {
    lint d;
    int n;
    cin >> d >> n;
    vector<pair<lint, lint>> horses(n);
    for (int i = 0; i < n; i++)
        cin >> horses[i].first >> horses[i].second;
    sort(horses.begin(), horses.end());
    double min_v = inf;
    for (int i = 0; i < n; i++) {
        double t = (double)(d - horses[i].first) / horses[i].second;
        double v = d / t;
        min_v = min(min_v, v);
    }
    cout << fixed << setprecision(8);
    cout << "Case #" << test_case + 1 << ": " << min_v << endl;
}

int main() {
    cin.tie(0);
    ios_base::sync_with_stdio(false);

    int t;
    cin >> t;
    for (int i = 0; i < t; i++)
        solve(i);
}
