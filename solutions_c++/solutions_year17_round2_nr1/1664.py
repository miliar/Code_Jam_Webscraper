#include <bits/stdc++.h>

using namespace std;
const int N = 1e3 + 3;
int main() {
#ifndef ONLINE_JUDGE
	freopen("input.in", "r", stdin);
	freopen("output.out", "w", stdout);
#endif
	int t;
	scanf("%d", &t);
	for (int test = 1; test <= t; ++test) {
		int d, n, k[N], s[N];
		scanf("%d %d", &d, &n);
		for (int i = 0; i < n; ++i) {
			scanf("%d %d", k + i, s + i);
		}
		
		double lower = 1e-6, upper = 1e15;
		for (int j = 0; j < 300; ++j) {
			double mid = (lower + upper) / 2;
			bool cool = true;
			for (int i = 0; i < n; ++i) {
				double meetingTime = k[i] / (mid - s[i]);
				if (mid - s[i] != 0 && meetingTime > 0 && meetingTime * mid < d) {
					cool = false;
					break;
				}
			}
			if (cool) {
				lower = mid;
			} else {
				upper = mid;
			}
		}
		printf("Case #%d: %.8lf\n", test, lower);
	}
	return 0;
}
