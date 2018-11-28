#include <stdio.h>
#include <functional>
#include <vector>
#include <algorithm>
#include <string.h>
#include <assert.h>
#include <limits.h>
#include <queue>
#include <string>
#include <iostream>
#include <cmath>

using namespace std;
typedef long long ll;

ll c[51][51];
double p[51];
double solve() {
	int K, N; scanf("%d %d", &K, &N);
	assert(K == N);
	double U; scanf("%lf", &U);

	for (int i = 0; i < N; i++) {
		scanf("%lf", p + i);
	}
	sort(p, p + N);

	for (int i = N - 1; i >= 0; i--) {
		double sum = 0;
		for (int j = i - 1; j >= 0; j--) {
			sum += p[i] - p[j];
		}
		if (sum <= U) {
			double ans = 1;
			for (int j = 0; j <= i; j++) {
				ans *= (p[i] + (U-sum) / double(i + 1));
			}
			for (int j = i + 1; j < N; j++) {
				ans *= p[j];
			}
			return ans;
		}
	}
}
int main(void) {
	freopen("C-small-1-attempt0.in", "r", stdin);
	freopen("output.txt", "w", stdout);

	c[0][0] = c[1][0] = c[1][1] = 1;
	for (ll i = 2; i <= 50; i++) {
		c[i][0] = 1;
		for (ll j = 1; j <= 50; j++) {
			c[i][j] = c[i - 1][j] + c[i-1][j - 1];
		}
	}


	int T; scanf("%d\n", &T);
	for (int tc = 1; tc <= T; tc++) {
		printf("Case #%d: ", tc);
		

		printf("%.10lf\n", solve());
	}

}