#include <bits/stdc++.h>
using namespace std;
#define ULL unsigned long long
#define LL long long
#define rep(i,n) for(int i = 0; i < n; ++i)
#define Rep(i,n) for(int i = 1; i <= n; ++i)

const int INF = 0x3f3f3f3f;
const int N = 53;
const int M = 5003*53;

struct dinic{
	int first[N*N], dis[N*N], cur[N*N], nxt[M], vv[M], cap[M], tot, s, t;
	void init(int _t) {
		memset(first, -1, sizeof(first));
		tot = 0; s = _t+1; t = _t+2;
	}
	
	void add(int u, int v, int c) {
		vv[tot] = v; cap[tot] = c; nxt[tot] = first[u]; first[u] = tot++;
		vv[tot] = u; cap[tot] = 0; nxt[tot] = first[v]; first[v] = tot++;
	}
	
	bool bfs() {
		memset(dis, 0x3f, sizeof(dis));
		dis[s] = 0;
		queue<int>q;
		q.push(s);
		while(!q.empty()) {
			int u = q.front(); q.pop();
			for(int i = first[u]; ~i; i = nxt[i]) {
				int v = vv[i];
				if(dis[v] == INF && cap[i]) {
					dis[v] = dis[u] + 1;
					q.push(v);
				}
			}
		}
		return dis[t] < INF;
	}
	
	int dfs(int u, int a) {
		if(u == t || !a) return a;
		int flow = 0, f;
		for(int& i = cur[u]; ~i; i = nxt[i]) {
			int v = vv[i];
			if(dis[v] == dis[u] + 1 && (f = dfs(v, min(a, cap[i])))) {
				cap[i] -= f;
				cap[i^1] += f;
				flow += f;
				a -= f;
				if(!a) break;
			}
		}
		return flow;
	}
	
	int maxflow() {
		int flow = 0;
		while(bfs()) {
			memcpy(cur, first, sizeof(first));
			flow += dfs(s, INF);
		}
		return flow;
	}
} solve;

int a[N], l[N][N], r[N][N], id[N][N];

int main()
{
	int t, cas = 0;
	cin >> t;
	while(cas++ < t) {
		int n, m;
		cin >> n >> m;
		Rep(i, n) scanf("%d", a+i);
		int num;
		Rep(i, n) Rep(j, m) {
			scanf("%d", &num);
			r[i][j] = num*10 / (a[i]*9);
			l[i][j] = (num*10+a[i]*11-1) / (a[i]*11);
		}
		num = 0;
		Rep(i, n) Rep(j, m) id[i][j] = ++num;
		int s = n*m+1, t = s+1;
		solve.init(n*m);
		Rep(i, m) {
			if(l[1][i] <= r[1][i]) solve.add(s, id[1][i], 1);
		}
		Rep(i, n-1) Rep(j, m) {
			if(l[i][j] <= r[i][j]) Rep(k, m) {
				if(l[i+1][k] <= r[i+1][k] && l[i][j] <= r[i+1][k] && l[i+1][k] <= r[i][j])
					solve.add(id[i][j], id[i+1][k], 1);
			}
		}
		Rep(i, m) {
			if(l[n][i] <= r[n][i]) solve.add(id[n][i], t, 1);
		}
		printf("Case #%d: %d\n", cas, solve.maxflow());
	}
	return 0;
}

