#include <algorithm>
#include <cmath>
#include <cstdio>
#include <utility>

using namespace std;

#define REP(i,b) for (int i = 0; i < (b); i++)
#define FOR(i,a,b) for (int i = (a); i <= (b); i++)
#define FORD(i,a,b) for (int i = (a); i >= (b); i--)

const int MAXN = 1005;
pair<int, int> P[MAXN];

double dp[MAXN][MAXN]; // [number of pancakes][bottom index]

int main() {
	int T;
	scanf("%d", &T);
	for (int tc = 1; tc <= T; tc++) {
		int N, K;
		scanf("%d%d", &N, &K);
		REP(i, N) scanf("%d%d", &P[i].first, &P[i].second);
		sort(P, P+N);

		REP(i, N) REP(j, N) dp[i+1][j] = 0.0;

		double ans = 0.0;
		REP(i, N) { // bottom pancake
			FOR(j, 1, i+1) { // number of pancakes
				double area = 0.0;
				REP(k, i) area = max(area, dp[j-1][k] - 1.0 * P[k].first * P[k].first);
				area += 1.0 * P[i].first * P[i].first;
				area += 2.0 * P[i].first * P[i].second;
				dp[j][i] = area;
				if (j == K) {
					ans = max(ans, area);
				}
			}
		}

		printf("Case #%d: %lf\n", tc, M_PI * ans);
	}
	return 0;
}
