#include <cstdio>
#include <algorithm>

using namespace std;

const long long INF = 999999999999LL;
const int MAXN = 105;

int E[MAXN], S[MAXN];
long long D[MAXN][MAXN];
long long T[MAXN];
int cases, N, Q;
double ans[MAXN];
bool flag[MAXN];

double gao(int x, int y) {
	for(int i = 0; i < N; ++i)
		ans[i] = INF;
	ans[x] = 0;
	memset(flag, false, sizeof(flag));
	for(int i = 0; i < N; ++i) {
		double mins = INF;
		int minv;
		for(int j = 0; j < N; ++j)
			if(!flag[j] && ans[j] < mins) {
				mins = ans[j];
				minv = j;
			}
		flag[minv] = true;
		for(int j = 0; j < N; ++j)
			if(!flag[j]) {
				if(D[minv][j] <= E[minv]) {
					ans[j] = min(ans[j], ans[minv] + D[minv][j] * 1.0 / S[minv]);
				}
			}
	}
	return ans[y];
}

int main() {
	scanf("%d", &cases);
	for(int xx = 1; xx <= cases; ++xx) {
		scanf("%d%d", &N, &Q);
		for(int i = 0; i < N; ++i) {
			scanf("%d%d", &E[i], &S[i]);
		}
		for(int i = 0; i < N; ++i)
			for(int j = 0; j < N; ++j) {
				scanf("%lld", &D[i][j]);
				if(D[i][j] == -1) D[i][j] = INF;
			}
		for(int k = 0; k < N; ++k)
			for(int i = 0; i < N; ++i)
				for(int j = 0; j < N; ++j)
					if(D[i][k] + D[k][j] < D[i][j])
						D[i][j] = D[i][k] + D[k][j];
		printf("Case #%d: ", xx);
		for(int i = 0; i < Q; ++i) {
			int x, y;
			scanf("%d%d", &x, &y);
			--x; --y;
			printf("%.10lf%c", gao(x, y), (i == Q - 1) ? '\n' : ' ');
		}
	}
}

