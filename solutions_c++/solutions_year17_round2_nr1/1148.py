#include <bits/stdc++.h>
#define Int long long
using namespace std;
int main() {
	int cnt_tests;
	scanf("%d", &cnt_tests);

	for(int cs = 1; cs <= cnt_tests; cs++) {
		int d, n;
		scanf("%d%d", &d, &n);

		double ans = 0;
		for(int i = 0; i < n; i++) {
			int k, s;
			scanf("%d%d", &k, &s);
			
			if(i == 0) {
				ans = (d - k) / (double)s;
			}
			else {
				ans = max(ans, (d - k) / (double)s);
			}
		}

		printf("Case #%d: %f\n", cs, d / ans);
	}

	return 0;
}
