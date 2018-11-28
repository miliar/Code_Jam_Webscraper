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
	int n, k;
	cin >> n >> k;
	long double u;
	cin >> u;
	vector<long double> p(n);
	for (int i = 0; i < n; ++i) {
		cin >> p[i];
	}
	p.pb(1);
	++n;
	while (u > 1e-10 && p[0] + 1e-10 < 1) {
	    sort(all(p));
		int j = 0;
		for (j = 1; j < n; ++j) {
		    if (p[j] > p[0] + 1e-10) {
				break;
			}
		}
		long double add = min(u / j, p[j] - p[0]);
		u -= j * add;
		for (int i = 0; i < j; ++i) p[i] += add;
	}
	long double ans = 1;
	for (int i = 0; i < n; ++i) {
		ans *= p[i];
	}
	printf("%.15lf\n", (double)ans);
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
