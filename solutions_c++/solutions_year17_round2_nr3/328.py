#include<bits/stdc++.h>
using namespace std;
#define FOR(i,s,e) for (int i=s;i<e;i++)
#define FOE(i,s,e) for (int i=s;i<=e;i++)
#define FOD(i,s,e) for (int i=s;i>=e;i--)
#define SET(a,e) memset(a,e,sizeof(a))
#define LL long long
#define LD long double
#define pb push_back
#define x first
#define y second
#define PII pair<int,int>
#define PLI pair<LL,int>
#define PIL pair<int,LL>
#define PLL pair<LL,LL>
#define PDD pair<LD,LD>
#define eps 1e-9
#define HH1 402653189
#define HH2 1610612741

int TC;
FILE *OUT;

struct node {
	int v, di;
	bool operator < (node const &T) const {
		return di > T.di;
	};
};

int n, m, e[105], dist[105][105];
LD s[105], cost[105][105];
vector<PII> ed[105];

void init() {
	SET(dist, 0);
	SET(cost, -1);
	
	FOR(i, 0, 105) cost[i][i] = 0;
	
	SET(e, 0);
	SET(s, 0);
	FOR(i, 0, 105) ed[i].clear();
}

void dijk(int st) {
	priority_queue<node> q;
	q.push((node){st, 0});
	
	int D[n + 1];
	SET(D, -1);
	
	D[st] = 0;
	
	while (!q.empty()) {
		node T = q.top(); q.pop();
		if (T.di != D[T.v]) continue;
		FOR(j, 0, ed[T.v].size()) {
			int to = ed[T.v][j].x;
			int todi = T.di + ed[T.v][j].y;
			if (todi > e[st]) continue;
			if (D[to] == -1 || todi < D[to]) {
				D[to] = todi;
				q.push((node){to, todi});
			}
		}
	}
	
	FOE(i, 1, n) 
		if (D[i] == -1) cost[st][i] = -1;
		else cost[st][i] = D[i] / s[st];
	
}

void solve() {
	scanf("%d%d", &n, &m);
	FOE(i, 1, n) scanf("%d%Lf", &e[i], &s[i]);
	FOE(i, 1, n) FOE(j, 1, n) {
		scanf("%d", &dist[i][j]);
		if (dist[i][j] != -1) ed[i].pb((PII){j, dist[i][j]});
	}
	
	FOE(i, 1, n) dijk(i);
	
	FOE(k, 1, n) FOE(i, 1, n) FOE(j, 1, n) {
		if (cost[i][k] != -1 && cost[k][j] != -1) {
			LD tot = cost[i][k] + cost[k][j];
			if (tot < cost[i][j] || cost[i][j] == -1)
				cost[i][j] = tot;
		}
	}
	
	while (m--) {
		int x, y;
		scanf("%d%d", &x, &y);
		fprintf(OUT, " %.10Lf", cost[x][y]);
	}
}

int main () {
	
	scanf("%d", &TC);
	
	OUT = fopen("c.out", "w");
	
	FOE(ttc, 1, TC) {
		
		printf("Processing on Case #%d...\n", ttc);
		
		init();
		
		fprintf(OUT, "Case #%d:", ttc);
		
		solve();
		
		fprintf(OUT, "\n");
		
	}
	
	return 0;
	
}
