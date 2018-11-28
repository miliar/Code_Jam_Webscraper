#include <bits/stdc++.h>
#define fr(a, b, c) for(int a = b, __ = c; a < __; ++a)
#define dbg(x) if(1) cerr << ">>>> " << x << endl;
#define _ << " , " <<

using namespace std;
typedef long long ll;
typedef pair<int, int> ii;

const int inf = 0x3f3f3f3f, mv = 10*1111, me = 2*(1000 + 1000 + 1000*1000 + 1000 + 5000) ;
int ant[me], adj[mv], from[me], cost[me], to[me], cap[me], z, nodes;
int fila[mv], level[mv], copy_adj[mv], copy_cap[me];

ll dist[mv], pot[mv], pai[mv];
set<ii> heap;

inline void add(int a, int b, int c, int d){
	ant[z] = adj[a], to[z] = b, from[z] = a, cap[z] = c, cost[z] = d, adj[a] = z++;
	swap(a, b);
	ant[z] = adj[a], to[z] = b, from[z] = a, cap[z] = 0, cost[z] = -d, adj[a] = z++;
}

int n, c, m, start;


void update(int no, ll ndist, int p){
	if(ndist >= dist[no]) return;
	if(dist[no] < inf) heap.erase(ii(dist[no], no));
	dist[no] = ndist;
	pai[no] = p;
	heap.insert(ii(dist[no], no));
}

ii top(){
	ii ret = *heap.begin();
	heap.erase(heap.begin());
	return ret;
}

bool dijkstra(int src, int sink){
	heap.clear();
	memset(dist, inf, sizeof dist);
	update(src, 0, -1);
	while(heap.size()){
		ii p = top();
		for(int i = adj[p.second]; i >= 0; i = ant[i])
			if(cap[i])
				update(to[i], p.first + cost[i] + pot[p.second] - pot[to[i]], i);
	}
	return dist[sink] < inf;
}

ii mcmf(int src, int sink){
	memset(pot, 0, sizeof pot);
	ll mc = 0, mf = 0;
	while(dijkstra(src, sink)){
		int flow = inf;
		for(int i = pai[sink]; ~i; i = pai[from[i]])
			flow = min(flow, cap[i]);
		for(int i = pai[sink]; ~i; i = pai[from[i]]){
			cap[i] -= flow;
			cap[i^1] += flow;
			mc += cost[i]*flow;
		}
		for(int i = 0; i < n; ++i) pot[i] += dist[i];
		mf += flow;
	}
	return ii(mc, mf);
}

int bfs(int src, int sink){
	memset(level, -1, sizeof level);
	level[src] = 0;
	int pos = 0, tam = 0;
	fila[tam++] = src;
	while(pos < tam){
		int now = fila[pos++];
		for(int i = adj[now]; i >= 0; i = ant[i]){
			if(cap[i] && level[to[i]] == -1){
				level[to[i]] = level[now] + 1;
				fila[tam++] = to[i];
			}
		}
	}
	return level[sink] != -1;
}

int dfs(int v, int sink, int flow){
	if(v == sink) return flow;
	int f;
	for(int &i = copy_adj[v]; i >= 0; i = ant[i]){
		if(cap[i] && level[to[i]] == level[v] + 1){
			f = dfs(to[i], sink, min(flow, cap[i]));
			if(f){
				cap[i] -= f;
				cap[i^1] += f;
				return f;
			}
		}
	}
	return 0;
}

int maxflow(int src, int sink){
	int ret = 0, flow;
	while(bfs(src, sink)){
		memcpy(copy_adj, adj, sizeof adj);
		while((flow = dfs(src, sink, 1 << 30))) 
			ret += flow;
	}
	return ret;
}

int src, sink;

bool can(int val){
	memcpy(cap, copy_cap, sizeof cap);
	fr(i, start, z){
		if(cap[i])
			cap[i] = val;	
	}
	int mf = maxflow(src, sink);
	return  mf == m;
}

int cnt[1111];

int main(){
	ios::sync_with_stdio(0);
	int t, cas= 1;
	cin >> t;
	while(t--){
		memset(adj, -1, sizeof adj);
		memset(cnt, 0, sizeof cnt);
		z = 0;
		int st = 1;
		cin >> n >> c >> m;
		src = n+m+c+10, sink = src + 20;
		fr(i, 0, c)
			add(src, i, inf, 0);
		fr(i, 0, m){
			int b, p;
			cin >> p >> b;
			add(b-1, c + i, 1, 0);
			fr(j, 0, p-1)
				add(c + i, c+m+j, 1, 1);
			add(c+i, c+m+p-1, 1, 0);
			
			cnt[b-1]++;
			st = max(cnt[b-1], st);
		}
		start = z;
		fr(i, 0, n){
			add(c+m+i, sink, 1, 0);
		}
		
		memcpy(copy_cap, cap, sizeof cap);
		
		int lo = st, hi = m;
		while(hi - lo > 1){
			int md = (lo + hi)/2;
			if(can(md)){
				hi = md;
			}
			else{
				lo = md;
			}
		}
		if(!can(lo))
			lo = hi;
		memcpy(cap, copy_cap, sizeof cap);
		fr(i, start, z){
			if(cap[i])
				cap[i] = lo;
		}
		ii ret = mcmf(src, sink);
		cout << "Case #" << cas++ << ": " << lo << " " << ret.first << endl;
	}
	return 0;
}
