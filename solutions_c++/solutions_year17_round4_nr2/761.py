#include <bits/stdc++.h>
#define mp make_pair
#define pb push_back
#define x first
#define y second
#define sz(a) ((int)(a).size())
#define rep(i, a, b) for(int (i) = (a); (i) < (b); (i)++)
#define dec(i, a, b) for (int (i) = (a); (i) >= (b); (i)--)
#define clr(a,v) memset(a, v, sizeof(a))
#define all(a) (a).begin(),(a).end()
#define ler freopen("in", "r", stdin)
#define fcin ios_base::sync_with_stdio(false)
#define EPS 1e-7
#define MAXN 1010
#define LOGN 18
using namespace std;
typedef long long ll;
typedef long double ld;
typedef pair <int, int> pii;

int par[2*MAXN], dist[2*MAXN], INF = 1e9;
vector<int> adj[2*MAXN];

bool bsf() {
	queue<int> q;
	rep(i, 1, 2*MAXN) {
		if(par[i] == 0) {
			dist[i] = 0;
			q.push(i);
		}
		else dist[i] = INF;
	}
	dist[0] = INF;
	while(!q.empty()) {
		int v = q.front(); q.pop();
		rep(i, 0, sz(adj[v])) {
			int u = adj[v][i];
			if(dist[par[u]] == INF) {
				dist[par[u]] = dist[v] + 1;
				q.push(par[u]);
			}
		}
	}
	return (dist[0] != INF);
}

bool dfs(int v){
	if(!v) return 1;
	rep(i, 0, sz(adj[v])) {
		int u = adj[v][i];
		if(dist[par[u]] == dist[v] + 1 && dfs(par[u])) {
			par[u] = v;
			par[v] = u;
			return 1;
		}
	}
	dist[v] = INF;
	return 0;
}

int hopcroftKarp() {
	rep(i,1,2*MAXN) par[i]=0;
	int matching = 0;
	while(bsf()) rep(i, 1, 2*MAXN) if(!par[i] && dfs(i)) matching++;
	return matching;
}

int t, n, c, m;

int main(){
	scanf("%d", &t);
	rep(caso,1,t+1){
		vector<int> val[2];
		rep(i,0,2*MAXN) adj[i].clear();
		scanf("%d%d%d", &n, &c, &m);
		rep(i,0,m){
			int v, q;
			scanf("%d %d", &v, &q); q--;
			val[q].pb(v);
		}
		if(sz(val[0]) > sz(val[1])) swap(val[0],val[1]);
		rep(i,0,sz(val[0])) rep(j,0,sz(val[1]))
			if(val[0][i] != val[1][j])
				adj[i+1].pb(j+MAXN), adj[j+MAXN].pb(i+1);
		hopcroftKarp();
		int ans1 = sz(val[1]), ans2 = 0;
		rep(i,0,sz(val[0])) if(!par[i+1]){
			if(val[0][i] == 1) ans1++;
			else ans2++;
		}
		printf("Case #%d: %d %d\n", caso, ans1, ans2);
	}
}

