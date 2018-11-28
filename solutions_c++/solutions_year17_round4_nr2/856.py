#include <bits/stdc++.h>
using namespace std;

const int maxn = 5000;
const int INF = 1005;

struct Edge {
  int from, to, cap, flow, cost;
  Edge(int u, int v, int c, int f, int w):from(u),to(v),cap(c),flow(f),cost(w) {}
};

struct MCMF {
  int n, m;
  vector<Edge> edges;
  vector<int> G[maxn];
  int inq[maxn];         
  int d[maxn];           
  int p[maxn];           
  int a[maxn];

  void init(int n) {
    this->n = n;
    for(int i = 0; i < n; i++) G[i].clear();
    edges.clear();
  }

  void AddEdge(int from, int to, int cap, int cost) {
  	// cout << from << " " << to << " " << cap << " " << cost << endl;
    edges.push_back(Edge(from, to, cap, 0, cost));
    edges.push_back(Edge(to, from, 0, 0, -cost));
    m = edges.size();
    G[from].push_back(m-2);
    G[to].push_back(m-1);
  }

  bool BellmanFord(int s, int t , int& flow, int& cost) {
    for(int i = 0; i < n; i++) d[i] = INF;
    memset(inq, 0, sizeof(inq));
    d[s] = 0; inq[s] = 1; p[s] = 0; a[s] = INF;

    queue<int> Q;
    Q.push(s);
    while(!Q.empty()) {
      int u = Q.front(); Q.pop();
      inq[u] = 0;
      for(int i = 0; i < G[u].size(); i++) {
        Edge& e = edges[G[u][i]];
        if(e.cap > e.flow && d[e.to] > d[u] + e.cost) {
          d[e.to] = d[u] + e.cost;
          p[e.to] = G[u][i];
          a[e.to] = min(a[u], e.cap - e.flow);
          if(!inq[e.to]) { Q.push(e.to); inq[e.to] = 1; }
        }
      }
    }
    if(d[t] == INF) return false;

    flow += a[t];
    cost += d[t] * a[t];
    for(int u = t; u != s; u = edges[p[u]].from) {
      edges[p[u]].flow += a[t];
      edges[p[u]^1].flow -= a[t];
    }
    return true;
  }

  int MincostFlow(int s, int t ,int& cost) {
    int flow = 0; cost = 0;
    while(BellmanFord(s, t , flow, cost));
    return flow;
  }

}solver;

vector<int> v[2];

int main() {
	int t , kase = 0;
	int st = INF * 2 , ed = INF * 2 + 1;
	scanf("%d" , &t);
	for( ; t--; ) {
		solver.init(maxn);
		for(int i = 0; i < 2; i++) {
			v[i].clear();
		}

		int n , m , k;
		scanf("%d%d%d" , &n , &m , &k);
		for(int i = 0; i < k; i++) {
			int x , y;
			scanf("%d%d" , &x , &y);
			v[y - 1].push_back(x);
		}

		for(int i = 0; i < v[0].size(); i++) {
			solver.AddEdge(st , v[0][i] , 1 , 0);
		}
		for(int i = 0; i < v[1].size(); i++) {		
			solver.AddEdge(v[1][i] + INF , ed , 1 , 0);
		}
		for(int i = 0; i < v[0].size(); i++) {
			for(int j = 0; j < v[1].size(); j++) {
				if(v[0][i] == v[1][j]) {
					if(v[0][i] != 1) solver.AddEdge(v[0][i] , v[1][j] + INF , 1 , 1);
				} else {
					solver.AddEdge(v[0][i] , v[1][j] + INF , 1 , 0);
				}
			}
		}
		int cost;
		int flow = solver.MincostFlow(st , ed , cost);
		printf("Case #%d: %d %d\n" , ++kase , flow + (k - flow * 2) , cost);
	}

  return 0;
}