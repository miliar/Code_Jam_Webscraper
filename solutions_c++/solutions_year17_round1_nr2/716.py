#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef pair<int, int> ii;
typedef vector<ll> vi;
typedef vector<ii> vii;
typedef vector<vi> vvi;

#define INF 1e9
#define FOR(i, a, b) for(int i=int(a); i<int(b); i++)
#define FORC(cont, it) for(decltype((cont).begin()) it = (cont).begin(); it != (cont).end(); it++)
#define pb push_back

struct Edge {
  int weight;
  Edge(int weight = 1) : weight(weight) { }
};

struct MatrixGraph {
  int V; bool undirected;
  vector<vector<Edge> > edges;
  MatrixGraph(int v, bool undirected) : V(v), undirected(undirected) {
    edges.assign(V, vector<Edge>(V, Edge(0)));
  }
  void connect(int from, int to, Edge edge = Edge(1)) {
    edges[from][to] = edge;
    if(undirected) edges[to][from] = edge;
  }
};

int augment(MatrixGraph &g, int flow, vi &parent, int source, int cv, int minEdge) {
  if(cv == source)
    return minEdge;
  if(parent[cv] != -1) {
    flow = augment(g, flow, parent, source, parent[cv], min(minEdge, g.edges[parent[cv]][cv].weight));
    g.edges[parent[cv]][cv].weight -= flow;
    g.edges[cv][parent[cv]].weight += flow;
  }
  return flow;
}

int maxFlow(MatrixGraph &g, int source, int sink) {
  int mf = 0, flow = -1;
  while(flow) {
    vi distanceTo(g.V, INF);
    distanceTo[source] = 0;
    queue<int> q; q.push(source);
    vi parent(g.V, -1);
    while(!q.empty()) {
      int cv = q.front(); q.pop();
      if(cv == sink) break;
      FOR(i, 0, g.V)
        if(g.edges[cv][i].weight > 0 && distanceTo[i] == INF)
          distanceTo[i] = distanceTo[cv] + 1, q.push(i), parent[i] = cv;
    }
    mf += flow = augment(g, 0, parent, source, sink, INF);
  }
  return mf;
}

typedef vector<vii> vvii;
ii getRange(int total, int grams) {
  double a = total/1.1;
  double b = total/0.9;
  return ii(ceil(a/grams), floor(b/grams));
}

bool validRange(ii range) {
  return range.first <= range.second;
}

bool rangesMatch(ii range1, ii range2) {
  return range1.second >= range2.first && range1.first <= range2.second;
}

int n, p;
vvii ranges;
int solve() {
  MatrixGraph g(n*p + 2, false);
  FOR(i, 0, p)
    if (validRange(ranges[0][i]))
      g.connect(0, i + 1);
  FOR(i, 0, n - 1)
    FOR(j, 0, p)
      if (validRange(ranges[i][j]))
        FOR(k, 0, p)
          if (validRange(ranges[i + 1][k]))
            if (rangesMatch(ranges[i][j], ranges[i + 1][k]))
              g.connect(i*p + j + 1, (i + 1)*p + k + 1);
  FOR(i, 0, p)
    if (validRange(ranges[n - 1][i]))
      g.connect((n - 1)*p + i + 1, n*p + 1);
  return maxFlow(g, 0, n*p + 1);
}

int main() {
  ios::sync_with_stdio(false);
  int t;
  cin >> t;
  FOR(tc, 1, t+1) {
    int c, r = -1;
    cin >> n >> p;
    vi grams(n);
    ranges = vvii(n, vii(p));
    FOR(i, 0, n)
      cin >> grams[i];
    FOR(i, 0, n)
      FOR(j, 0, p) {
        cin >> c;
        ranges[i][j] = getRange(c, grams[i]);
      }
    r = solve();
    cout << "Case #" << tc << ": " << r << endl;
  }
}
