#include <stdio.h>
#include <vector>
#include <string.h>
#include <algorithm>
#include <assert.h>
#include <limits.h>
#include <queue>
using namespace std;


int main(void) {
	freopen("c:\\cdj\\A-large.in", "r", stdin);
	freopen("c:\\cdj\\A-large.txt", "w", stdout);
	int T; scanf("%d\n", &T);
	for (int tc = 1; tc <= T; tc++) {
		double ans = 0;
		double D; int N; scanf("%lf %d", &D, &N);

		double max_time = 0;
		for (int i = 0; i < N; i++) {
			double K, S; scanf("%lf %lf", &K, &S);

			double now = (D - K) / S;
			if (max_time < now) {
				max_time = now;
			}
		}
		ans = D / max_time;

		printf("Case #%d: %.10lf\n", tc, ans);
	}

}