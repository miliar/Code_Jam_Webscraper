#include <iostream>
#include <cstdio>
#include <algorithm>
using namespace std;
struct gogo {
	double ki, si;
} G[1005];
bool cmp(const gogo A, const gogo B) {
	return A.ki < B.ki;
}
int main() {

	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int t, tc;
	cin >> tc;
	for (t = 1; t <= tc; t++) {
		double D, tm, mx=0, ans;
		long long N, i;
		cin >> D >> N;
		for (i = 0; i < N; i++) cin >> G[i].ki >> G[i].si;
		sort(G, G + N, cmp);
		for (i = N - 1; i >= 0; i--) {
			tm = (D - G[i].ki) / G[i].si;
			if (mx < tm) mx = tm;
		}
		ans = D / mx;
		printf("Case #%d: %.7lf\n", t, ans);
	}

	return 0;
}