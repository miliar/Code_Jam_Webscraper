#include <bits/stdc++.h>

#define eb emplace_back
#define pb push_back
#define mp make_pair
#define fi first
#define se second
#define INF 0x3f3f3f3f

using namespace std;

typedef long long ll;
typedef pair<double, int> pii;
typedef vector<int> vi;
const int N = 110;

int n, q; 
ll dist[N][N];
double ans[N][N];
int e[N], s[N];
void dijkstra (int so, double *ans) {
	for (int i = 1; i <= n; i++) ans[i] = 100000000000000000.;
	ans[so] = 0;
	priority_queue <pii, vector<pii>, greater<pii> > pq;
	pq.emplace(0., so);
	while (!pq.empty()) {
		double d = pq.top().fi;
		int u = pq.top().se;
		pq.pop();
		for (int i = 1; i <= n; i++) {
			if (e[u] >= dist[u][i]) {
				double nova = dist[u][i] / (1. * s[u]);
				if (nova + d + 1e-7 < ans[i]) {
					ans[i] = nova + d;
					pq.emplace(ans[i], i);
				}
			}
		}
	}
}
int main (void) {
	int t; scanf("%d", &t);
	for (int tt = 1; tt <= t; tt++) {
		scanf("%d %d", &n, &q);
		for (int i = 1; i <= n; i++) {
			scanf("%d %d", e + i, s + i);	
		}
		for (int i = 1; i <= n; i++) {
			for (int j = 1; j <= n; j++) {
				scanf("%lld", &dist[i][j]);
				if (dist[i][j] == -1) dist[i][j] = 100000000000000000LL;
			}
		}
		for (int k = 1; k <= n; k++) {
			for (int i = 1; i <= n; i++) {
				for (int j = 1; j <= n; j++) {
					if (dist[i][k] + dist[k][j] < dist[i][j])
						dist[i][j] = dist[i][k] + dist[k][j];
				}
			}
		}
		for (int i = 1; i <= n; i++) {
			dijkstra (i, ans[i]);
		}
		printf("Case #%d:", tt);
		while (q--) {
			int x, y; scanf("%d %d", &x, &y);
			printf(" %.9lf", ans[x][y]);
		}
		cout << endl;
	}
	return 0;
}

