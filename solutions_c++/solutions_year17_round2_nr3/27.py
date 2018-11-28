#include "bits/stdc++.h"
using namespace std;
#define rep(i,n) for(int (i)=0;(i)<(int)(n);++(i))
#define rer(i,l,u) for(int (i)=(int)(l);(i)<=(int)(u);++(i))
#define reu(i,l,u) for(int (i)=(int)(l);(i)<(int)(u);++(i))
static const int INF = 0x3f3f3f3f; static const long long INFL = 0x3f3f3f3f3f3f3f3fLL;
typedef vector<int> vi; typedef pair<int, int> pii; typedef vector<pair<int, int> > vpii; typedef long long ll;
template<typename T, typename U> static void amin(T &x, U y) { if (y < x) x = y; }
template<typename T, typename U> static void amax(T &x, U y) { if (x < y) x = y; }

int main() {
	int T;
	scanf("%d", &T);
	for (int ii = 0; ii < T; ++ ii) {
		int N; int Q;
		scanf("%d%d", &N, &Q);
		vector<int> E(N);
		vector<int> S(N);
		for (int i = 0; i < N; ++ i)
			scanf("%d%d", &E[i], &S[i]);
		vector<vector<ll>> dist(N, vector<ll>(N, INFL));
		rep(i, N) dist[i][i] = 0;
		for (int i = 0; i < N; ++ i) for (int j = 0; j < N; ++ j) {
			int D;
			scanf("%d", &D);
			if (D != -1)
				amin(dist[i][j], D);
		}
		rep(k, N) rep(i, N) rep(j, N)
			amin(dist[i][j], dist[i][k] + dist[k][j]);
		vector<vector<double>> time(N, vector<double>(N, 1e99));
		rep(i, N)
			time[i][i] = 0;
		rep(i, N) {
			rep(j, N) if(dist[i][j] <= E[i])
				amin(time[i][j], dist[i][j] * 1. / S[i]);
		}
		rep(k, N) rep(i, N) rep(j, N)
			amin(time[i][j], time[i][k] + time[k][j]);
		printf("Case #%d:", ii + 1);
		rep(i, Q) {
			int u; int v;
			scanf("%d%d", &u, &v), -- u, -- v;
			printf(" %.10f", time[u][v]);
		}
		puts("");
	}
	return 0;
}
