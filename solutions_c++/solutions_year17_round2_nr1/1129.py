#include <algorithm>
#include <cstdio>

using namespace std;

#define REP(i,b) for (int i = 0; i < (b); i++)
#define FOR(i,a,b) for (int i = (a); i <= (b); i++)
#define FORD(i,a,b) for (int i = (a); i >= (b); i--)

int main() {
	int T;
	scanf("%d", &T);
	for (int tc = 1; tc <= T; tc++) {
		int D, N;
		scanf("%d%d", &D, &N);
		double ans = 1e18;
		REP(i, N) {
			int K, S;
			scanf("%d%d", &K, &S);
			double t = ((double) (D - K)) / S;
			ans = min(ans, D / t);
		}
		printf("Case #%d: %lf\n", tc, ans);
	}
	return 0;
}
