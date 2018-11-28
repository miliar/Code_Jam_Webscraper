#include <bits/stdc++.h>
using namespace std;

typedef pair<int, int> pii;

#define GET_MACRO(_1, _2, _3, _4, NAME, ...) NAME

#define xrange_3(i, a, n, inc) for(int i = a; inc > 0 ? i < n : i > n; i += inc)
#define xrange_2(i, a, n) xrange_3(i, a, n, 1)
#define xrange_1(i, n) xrange_2(i, 0, n)
#define xrange(...) GET_MACRO(__VA_ARGS__, xrange_3, xrange_2, xrange_1)(__VA_ARGS__)

#define X first
#define Y second

#define rd(x) scanf("%d", &x)
#define wt(x) printf("%d ", x)
#define rdll(x) scanf("%lld", &x)
#define wtll(x) printf("%lld ", x)
#define nl printf("\n")

#define MAXN 105

long long D[MAXN][MAXN];
long double dp[MAXN][MAXN];
long long dist[MAXN][MAXN];
long long E[MAXN], S[MAXN];

int T, N, Q;

int main() {
	rd(T);
	xrange(t, 1, T + 1) {
		rd(N), rd(Q);
		xrange(i, N) {
			rdll(E[i]), rdll(S[i]);
		}
		xrange(i, N) {
			xrange(j, N) {
				rdll(D[i][j]);
				dist[i][j] = (D[i][j] == -1) ? 1000000000000000000LL : D[i][j];
			}
		}
		xrange(k, N) {
			xrange(i, N) {
				xrange(j, N) {
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j]);
				}
			}
		}
		xrange(i, N) {
			xrange(j, N) {
				if(E[i] >= dist[i][j]) {
					dp[i][j] = dist[i][j] / (S[i] * 1.0);
				} else {
					dp[i][j] = 1000000000000000000LL;
				}
			}
		}
		xrange(k, N) {
			xrange(i, N) {
				xrange(j, N) {
                    dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j]);
				}
			}
		}
		printf("Case #%d: ", t);
		xrange(i, Q) {
			int x, y;
			rd(x), rd(y);
			printf("%.10Lf ", dp[x - 1][y - 1]);		
		}
		nl;
	}
}