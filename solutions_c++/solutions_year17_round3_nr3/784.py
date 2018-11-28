#include <stdio.h>
#include <string.h>
#include <math.h>
#include <algorithm>
#include <utility>
#include <vector>

#define fi first
#define se second
#define mp make_pair
#define pb push_back
#define PI acos(-1);
#define INF 1023123123
#define pll pair <long long int, long long int>
#define REP(a, b) for (int a = 0; a < b; ++a)
#define FORU(a, b, c) for (int a = b; a <= c; ++a)
#define FORD(a, b, c) for (int a = b; a >= c; --a)

using namespace std;

int main() {
	int N, K, T;
	double U, core[55];

	scanf("%d", &T);

	FORU(tc, 1, T) {
		scanf("%d %d", &N, &K);

		scanf("%lf", &U);

		REP(i, N)
			scanf("%lf", &core[i]);

		sort(core, core + N);

		core[N] = 1.0;

		int pos = 0;

		while (U != 0 && U > 1e-9) {
			if (core[pos] != core[pos+1]) {
				double delta = core[pos+1] - core[pos];
				double restU = U / (double) (pos + 1);

				if (restU < delta) {
					REP(i, pos + 1)
						core[i] += restU;

					U = 0;
				}
				else {
					REP(i, pos + 1)
						core[i] = core[pos+1];

					U -= delta * (double) (pos + 1);
				}
			}

			++pos;
		}

		double ans = 1.0;

		REP(i, N)
			ans *= core[i];

		printf("Case #%d: %.9lf\n", tc, ans);
	}

	return 0;
}