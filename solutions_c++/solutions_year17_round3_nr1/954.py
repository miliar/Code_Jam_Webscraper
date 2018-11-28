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

bool cf(pll a, pll b) {
	long long int pan1 = a.fi * a.se;
	long long int pan2 = b.fi * b.se;

	if (pan1 != pan2)
		return pan1 > pan2;

	return a.fi > b.fi;
}

int main() {
	int n, k, T;
	pll pan[1005];

	scanf("%d", &T);

	FORU(tc, 1, T) {
		scanf("%d %d", &n, &k);

		REP(i, n) {
			scanf("%lld %lld", &pan[i].fi, &pan[i].se);
		}

		sort(pan, pan + n, cf);

		long long int ans = 0;

		REP(i, n) {
			long long int currAns = pan[i].fi * pan[i].fi + 2LL * pan[i].fi * pan[i].se;
			int pickPan = 1;

			REP(j, n) {
				if (pickPan == k)
					break;

				if (pan[j].fi > pan[i].fi || i == j)
					continue;

				currAns += 2LL * pan[j].fi * pan[j].se;

				++pickPan;
			}

			if (pickPan == k) {
				ans = max(ans, currAns);
			}
		}

		double finalAns = (double) PI;
		finalAns *= (double) ans;

		printf("Case #%d: %.9lf\n", tc, finalAns);
	}

	return 0;
}