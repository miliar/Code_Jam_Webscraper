#include <bits/stdc++.h>
#define f(a, n) for (int a=0; a<n; a++)
#define F(a, n) for (int a=1; a<=n; a++)
using namespace std;
typedef long long LL;

struct Edge {
  int u, v;
  LL cap, flow;
  Edge() {}
  Edge(int u, int v, LL cap): u(u), v(v), cap(cap), flow(0) {}
};

struct Dinic {
  int N;
  vector<Edge> E;
  vector<vector<int>> g;
  vector<int> d, pt;
  
  Dinic(int N): N(N), E(0), g(N), d(N), pt(N) {}

  void Clear() {
  	N=0;
  	E.clear();
  	for (auto &x: g) x.clear();
  	g.clear();
  	d.clear();
  	pt.clear();
  }

  void AddEdge(int u, int v, LL cap) {
    if (u != v) {
      E.emplace_back(Edge(u, v, cap));
      g[u].emplace_back(E.size() - 1);
      E.emplace_back(Edge(v, u, 0));
      g[v].emplace_back(E.size() - 1);
    }
  }

  bool BFS(int S, int T) {
    queue<int> q({S});
    fill(d.begin(), d.end(), N + 1);
    d[S] = 0;
    while(!q.empty()) {
      int u = q.front(); q.pop();
      if (u == T) break;
      for (int k: g[u]) {
        Edge &e = E[k];
        if (e.flow < e.cap && d[e.v] > d[e.u] + 1) {
          d[e.v] = d[e.u] + 1;
          q.emplace(e.v);
        }
      }
    }
    return d[T] != N + 1;
  }

  LL DFS(int u, int T, LL flow = -1) {
    if (u == T || flow == 0) return flow;
    for (int &i = pt[u]; i < g[u].size(); ++i) {
      Edge &e = E[g[u][i]];
      Edge &oe = E[g[u][i]^1];
      if (d[e.v] == d[e.u] + 1) {
        LL amt = e.cap - e.flow;
        if (flow != -1 && amt > flow) amt = flow;
        if (LL pushed = DFS(e.v, T, amt)) {
          e.flow += pushed;
          oe.flow -= pushed;
          return pushed;
        }
      }
    }
    return 0;
  }

  LL MaxFlow(int S, int T) {
    LL total = 0;
    while (BFS(S, T)) {
      fill(pt.begin(), pt.end(), 0);
      while (LL flow = DFS(S, T))
        total += flow;
    }
    return total;
  }
};
int T, n, R, O, Y, Gr, B, V, curr;
char dict[7] = {'X', 'R', 'O', 'Y', 'G', 'B', 'V'};
int main(){
	cin.tie(NULL);
	ios::sync_with_stdio(0);
	ifstream inp;
	ofstream oup;
	inp.open("b.in");
	oup.open("b.out");
	oup<<setprecision(9)<<fixed;
	inp>>T;
	
	F(t, T){
		inp>>n>>R>>O>>Y>>Gr>>B>>V;
		if (R) curr = 1;
		if (O) curr = 2;
		if (Y) curr = 3;
		if (Gr) curr = 4;
		if (B) curr = 5;
		if (V) curr = 6;
		
		Dinic G = Dinic(20);
		G.AddEdge(0, 1, R);
		G.AddEdge(0, 2, O);
		G.AddEdge(0, 3, Y);
		G.AddEdge(0, 4, Gr);
		G.AddEdge(0, 5, B);
		G.AddEdge(0, 6, V);
		
		G.AddEdge(1, 13, 1337);
		G.AddEdge(1, 14, 1337);
		G.AddEdge(1, 15, 1337);
		
		G.AddEdge(3, 11, 1337);
		G.AddEdge(3, 15, 1337);
		G.AddEdge(3, 16, 1337);
		
		G.AddEdge(5, 11, 1337);
		G.AddEdge(5, 12, 1337);
		G.AddEdge(5, 13, 1337);
		
		G.AddEdge(2, 15, 1337);
		G.AddEdge(4, 11, 1337);
		G.AddEdge(6, 13, 1337);
		
		G.AddEdge(11, 19, R);
		G.AddEdge(12, 19, O);
		G.AddEdge(13, 19, Y);
		G.AddEdge(14, 19, Gr);
		G.AddEdge(15, 19, B);
		G.AddEdge(16, 19, V);
		
		oup<<"Case #"<<t<<": ";
		if (G.MaxFlow(0, 19)<n){
			oup<<"IMPOSSIBLE"<<endl;
		}
		else{
			while (n--){
				oup<<dict[curr];
				for (int x: G.g[curr]){
					if (G.E[x].v==0) continue;
					if (G.E[x].flow>0){
						G.E[x].flow--;
						curr = G.E[x].v-10;
						break;
					}
				}
			}
			oup<<endl;
		}
	}
}

