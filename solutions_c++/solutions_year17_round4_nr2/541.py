#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef vector<int> vi;
typedef vector<ll> vl;
typedef vector<vi> vvi;
typedef vector<vl> vvl;
typedef long double ld;
typedef vector<double> vd;
typedef pair<int, int> pii;
typedef pair<double, double> pdd;
typedef vector<pii> vii;
typedef vector<string> vs;
//typedef long long int;

struct TEdge {
  int from, to;
  ll capacity, flow;
  ll cost;
  TEdge* reverse;
};

TEdge edgePool[1000000];
int edgePoolPtr = 0;

typedef vector<TEdge*> ve;
vector< ve > edges; //resize

int SOURCE, TARGET; //assign

TEdge* AddEdge(int from, int to, ll capacity, ll cost = 0) {
  TEdge* e1 = &edgePool[edgePoolPtr++];
  TEdge* e2 = &edgePool[edgePoolPtr++];
  TEdge fw = {from, to, capacity, 0, cost, e2};
  TEdge bw = {to, from, 0, 0, cost, e1};
  *e1 = fw;
  *e2 = bw;
  edges[from].push_back(e1);
  edges[to].push_back(e2);
  return e1;
}

void maxFlowMinCost(int so, int ta, int & flow, int & cost) {
  flow = 0;
  cost = 0;
  const int inf = (int)1e+9;
  while (1) {
    vi pvert(edges.size()), pedge(edges.size()), d(edges.size(), inf), id(edges.size());
    deque<int> q;
    q.push_back(so);
    id[so] = 1;
    d[so] = 0;
    while (!q.empty()) {
      int v = q.front();
      q.pop_front();
      id[v] = 2;
      for (size_t i = 0; i < edges[v].size(); ++i) {
        TEdge & ed = *edges[v][i];
        if (ed.flow < ed.capacity && d[v] + ed.cost < d[ed.to]) {
          d[ed.to] = d[v] + ed.cost;
          if (id[ed.to] == 0) {
            q.push_back(ed.to);
          } else if (id[ed.to] == 2) {
            q.push_front(ed.to);
          }
          id[ed.to] = 1;
          pvert[ed.to] = v;
          pedge[ed.to] = i;
        }
      }
    }
    if (d[ta] == inf) break;
    ll dflow = inf;
    for (int v = ta; v != so; v = pvert[v]) {
      TEdge & ed = *edges[pvert[v]][pedge[v]];
      dflow = min(dflow, ed.capacity - ed.flow);
    }
    for (int v = ta; v != so; v = pvert[v]) {
      TEdge & ed = *edges[pvert[v]][pedge[v]];
      TEdge & inved = *ed.reverse;
      //TEdge & inved = *edges[ed.to][ed.backInd];
      ed.flow += dflow;
      inved.flow -= dflow;
      cost += ed.cost * dflow;
    }
    flow += dflow;
  }
}

int n,c,m;

void f(int & flow, int & cost, const vvi & g, int r) {
//  TARGET = SOURCE + 1;
//  edges.assign(TARGET + 1, ve());
  vi c(n);
  for (int i = 0; i < g.size(); ++i) for (int x : g[i]) ++c[x];
  flow = 0;
  cost = 0;
  for (int i = 0; i < n; ++i) {
    cost += max(0, c[i] - r);
    flow += c[i];
    if (flow > (i + 1) * r) {
      flow = 0;
      break;
    }
  }
}

int main() {
  int T;
  cin >> T;
  for (int test = 1; test <= T; ++test) {
    printf("Case #%d: ", test);
    cin >> n >> c >> m;
    vvi g(c);
    for (int i = 0; i < m; ++i) {
      int a,b;
      cin >> a >> b;
      --a; --b;
      g[b].push_back(a);
    }
    int flow = 0, cost = 0, l = 0, r = m;
    for (int i = 0; i < g.size(); ++i) l = max(l, (int)g[i].size() - 1);
    while (r - l > 1) {
      int x = (l + r) / 2;
      f(flow, cost, g, x);
      if (flow >= m) {
        r = x;
      } else {
        l = x;
      }
    }
    f(flow, cost, g, r);
    cout << r << ' ' << cost << endl;
  }
  return 0;
}
