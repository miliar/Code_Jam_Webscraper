#include <algorithm>
#include <cassert>
#include <cstdio>

using namespace std;

#define REP(i,b) for (int i = 0; i < (b); i++)
#define FOR(i,a,b) for (int i = (a); i <= (b); i++)
#define FORD(i,a,b) for (int i = (a); i >= (b); i--)

const int MAXN = 105;
const int MAXQ = 105;

int E[MAXN], S[MAXN];
int D[MAXN][MAXN];
int U[MAXQ], V[MAXQ];
double dp[MAXN][MAXN]; // dp[city][last_horse] = time
int dist[MAXN];

int main() {
	int T;
	scanf("%d", &T);
	FOR(tc, 1, T) {
		int N, Q;
		scanf("%d%d", &N, &Q);
		REP(i, N) scanf("%d%d", &E[i], &S[i]);
		REP(i, N) REP(j, N) scanf("%d", &D[i][j]);
		REP(i, Q) { scanf("%d%d", &U[i], &V[i]); U[i]--; V[i]--; }
		assert(Q == 1 && U[0] == 0 && V[0] == N-1);
		dp[0][0] = 0;
		dist[0] = 0;
		FOR(i, 1, N-1) {
			dist[i] = dist[i-1] + D[i-1][i];
			FOR(j, 0, i) dp[i][j] = 1e18;
			FOR(j, 0, i-1) {
				if (dist[i] - dist[j] > E[j]) continue;
				double t = dp[i-1][j] + ((double) D[i-1][i]) / S[j];
				dp[i][j] = min(dp[i][j], t);
				dp[i][i] = min(dp[i][i], t);
			}
		}
		printf("Case #%d: %lf\n", tc, dp[N-1][N-1]);
	}
	return 0;
}
