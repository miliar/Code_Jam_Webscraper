#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef pair<int, int> ii;
typedef vector<int> vi;
typedef vector<ii> vii;

typedef pair<double, int> di;
typedef pair<di, ii> state;
// state is time, loc, horse, remaining energy

int T, N, Q, E[110], S[110];
vector<vii> adjList;

double calc(int x, int y) {
	priority_queue<state, vector<state>, greater<state> > pq;
	bool vis[110][110];
	pq.push(state(di(0.0, x), ii(x, E[x])));
	memset(vis, false, sizeof vis);
	while (!pq.empty()) {
		double t = pq.top().first.first;
		int u = pq.top().first.second;
		int h = pq.top().second.first;
		int e = pq.top().second.second;
		int s = S[h];
		int ne = E[u];
		int ns = S[u];
		pq.pop();
		if (u == y) return t;
		if (vis[u][h]) continue;
		vis[u][h] = true;
		for (int i=0; i<(int)adjList[u].size(); i++) {
			int v = adjList[u][i].first;
			int d = adjList[u][i].second;
			if ((ne > e || ns > s) && ne >= d && !vis[v][u]) {
				pq.push(state(di(t + 1.0*d/(1.0*ns), v), ii(u, ne-d)));
			}
			if ((e >= ne || s >= ns) && e >= d && !vis[v][h]) {
				pq.push(state(di(t + 1.0*d/(1.0*s), v), ii(h, e-d)));
			}
		}
	}
	return 0;
}


int main() {
	int t=1, i, j, x, y;
	scanf("%d", &T);
	while (T--) {
		scanf("%d %d", &N, &Q);
		adjList.assign(N+10, vii());
		for (i=1; i<=N; i++) {
			scanf("%d %d", &E[i], &S[i]);
		}
		for (i=1; i<=N; i++) {
			for (j=1; j<=N; j++) {
				scanf("%d", &x);
				if (x == -1) continue;
				adjList[i].push_back(ii(j, x));
			}
		}
		printf("Case #%d:", t++);
		while (Q--) {
			scanf("%d %d", &x, &y);
			printf(" %.10lf", calc(x, y));
		}
		printf("\n");
	}
	return 0;
}