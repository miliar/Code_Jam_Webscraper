#include <bits/stdc++.h>

using namespace std;
using ll = long long;
using ld = long double;
constexpr int MAXN = 100005;

int d, n;
pair<int, int> data [MAXN];

bool check(ld val) {
	ld time_needed = d / val;

	for (int i = 0; i < n; i++) {
		ld horse_time = (d - data[i].first) / (ld) data[i].second;

		if (horse_time > time_needed) {
			return false;
		}
	}

	return true;
}

ld solve() {
	scanf("%d%d", &d, &n);

	for (int i = 0; i < n; i++) {
		int k, s;
		scanf("%d%d", &k, &s);
		data[i] = make_pair(k, s);
	}

	ld l = 0.0, r = 1e18, mid;
	for (int i = 0; i < 2000; i++) {
		mid = (l+r)/2.0;
		//printf("%Lf\n", mid);

		if (check(mid)) {
			l = mid;
		} else {
			r = mid;
		}
	}
	return (l+r)/2.0;
}

void report(int i, ld ans) {
	printf("Case #%d: %.6f\n", i, (double) ans);
}

int main(void) {
	int t;
	scanf("%d", &t);

	for (int i = 0; i < t; i++) {
		report(i+1, solve());
	}

	return 0;
}