#include <iostream>
#include <stdio.h>
#include <vector>
#include <string>
#include <math.h>
#include <algorithm>
#include <map>
#include <set>
#include <set>

#define sz(x) ((int)x.size())
#define all(x) (x).begin(), (x).end()
#define pb(x) push_back(x)
#define mp(x, y) make_pair(x, y)

typedef long long int64;

using namespace std;

void solve() {
    int64 d, n;
	cin >> d >> n;
	long double ans = 0;
	for (int64 i = 0; i < n; ++i) {
		int64 k, s;
		cin >> k >> s;
		long double t = (long double)(d - k) / s;
		long double res = d / t;
		if (i == 0) {
			ans = res;
		} else {
			ans = min(ans, res);
		}
	}
	cout.precision(21);
	cout << ans << endl;
}

int main() {
    int tests;
    cin >> tests;
    for (int test = 1; test <= tests; ++test) {
        cout << "Case #" << test << ": ";
        solve();
    }
    return 0;
}
