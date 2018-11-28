#include <bits/stdc++.h>

using namespace std;

int t, d, n, td, ts;

int main() {
	freopen ("inn","r",stdin);
	freopen ("myfile.txt","w",stdout);
	scanf("%d", &t);
	for (int kk = 1; kk <= t; kk++) {
		double tn = -1;
		scanf("%d%d", &d, &n);
		while (n--) {
			scanf("%d%d", &td, &ts);
			tn = max(tn, double(d - td) / double(ts));
		}
		printf("Case #%d: %.8lf\n", kk, d/tn);
	}
	return 0;
}
