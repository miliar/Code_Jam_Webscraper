#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <queue>
#include <map>

#define fi first
#define se second

#define SIZE 1005
#define INF (2e9)

using namespace std;

typedef long long ll;
typedef pair<int, int> pii;

pii A[SIZE];

int main()
{
	int T, D, N;
	scanf("%d", &T);
	for (int _c = 0; _c < T; _c ++) {
		printf("Case #%d: ", _c + 1);
		scanf("%d%d", &D, &N);
		for (int i = 0; i < N; i ++) {
			scanf("%d%d", &A[i].fi, &A[i].se);
		}
		sort(A, A + N);

		int last_s = INF;
		double last_p = INF;
		double last_t = 0;
		double max_t = 0;
		for (int i = N - 1; i > -1; i --) {
			if (A[i] == A[i + 1]) {
				continue;
			}
			double cur_t = 1.0 * (D - A[i].fi) / A[i].se;

			if (i < N - 1 && A[i].se > A[i + 1].se &&
			    A[i].fi + last_t * A[i].se >= last_p) {
				double tt = (last_p - A[i].fi) / (A[i].se - A[i + 1].se);
				if (cur_t < tt) {
					cur_t = tt;
					last_p = min(last_p, tt * A[i].se + A[i].fi);
					last_t = max(last_t, tt);
					last_s = min(last_s, A[i].se);
				}
			} else {
				last_p = min(last_p, 1.0 * A[i].fi);
				last_t = max(last_t, 0.0);
				last_s = A[i].se;
			}
			max_t = max(max_t, last_t + 1.0 * (D - last_p) / last_s);
			//printf("%lf %lf %lf %d\n", cur_t, last_p, last_t, last_s);
		}
		printf("%lf\n", 1.0 * D / max_t);
	}
	return 0;
}