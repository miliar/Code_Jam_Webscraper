#include <bits/stdc++.h>

using namespace std;

int main() {
	int t;
	scanf("%d", &t);
	for (int tc = 0; tc < t; tc++) {
		double d, n;
		double start[1005];
		double speed[1005];
		scanf("%lf%lf", &d, &n);
		for(int i=0; i<n; i++) {
			scanf("%lf%lf", &start[i], &speed[i]);
		}
		double maks = 0;
		for(int i=0; i<n; i++) {
			double dist = d - start[i];
			double time = dist / speed[i];
			if (time > maks) {
				maks = time;
			}
		}
		double ans = d / maks;
		printf("Case #%d: %lf\n", tc+1, ans);
	}
	return 0;
}