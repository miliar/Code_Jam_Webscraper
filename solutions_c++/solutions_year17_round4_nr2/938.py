#include <bits/stdc++.h>
#include <boost/range/irange.hpp>
#include <boost/range.hpp>
#include "../../prettyprint.hpp"
using namespace std;
using boost::irange;
using boost::make_iterator_range;

#ifdef NDEBUG
#include <boost/iostreams/stream.hpp>
#include <boost/iostreams/device/null.hpp>
boost::iostreams::stream<boost::iostreams::null_sink> logs((boost::iostreams::null_sink()));
#else
auto& logs = cerr;
#endif

typedef vector<int> VI;
typedef vector<VI> VVI;
typedef int L;
typedef vector<L> VL;
typedef vector<VL> VVL;
typedef pair<int, int> PII;
typedef vector<PII> VPII;

const L INF = numeric_limits<L>::max() / 4;

struct MinCostMaxFlow {
  int N;
  VVL cap, flow, cost;
  VI found;
  VL dist, pi, width;
  VPII dad;

  MinCostMaxFlow(int N) :
    N(N), cap(N, VL(N)), flow(N, VL(N)), cost(N, VL(N)),
    found(N), dist(N), pi(N), width(N), dad(N) {}

  void AddEdge(int from, int to, L cap, L cost) {
    this->cap[from][to] = cap;
    this->cost[from][to] = cost;
  }

  void Relax(int s, int k, L cap, L cost, int dir) {
    L val = dist[s] + pi[s] - pi[k] + cost;
    if (cap && val < dist[k]) {
      dist[k] = val;
      dad[k] = make_pair(s, dir);
      width[k] = min(cap, width[s]);
    }
  }

  L Dijkstra(int s, int t) {
    fill(found.begin(), found.end(), false);
    fill(dist.begin(), dist.end(), INF);
    fill(width.begin(), width.end(), 0);
    dist[s] = 0;
    width[s] = INF;

    while (s != -1) {
      int best = -1;
      found[s] = true;
      for (int k = 0; k < N; k++) {
        if (found[k]) continue;
        Relax(s, k, cap[s][k] - flow[s][k], cost[s][k], 1);
        Relax(s, k, flow[k][s], -cost[k][s], -1);
        if (best == -1 || dist[k] < dist[best]) best = k;
      }
      s = best;
    }

    for (int k = 0; k < N; k++)
      pi[k] = min(pi[k] + dist[k], INF);
    return width[t];
  }

  pair<L, L> GetMaxFlow(int s, int t) {
    L totflow = 0, totcost = 0;
    while (L amt = Dijkstra(s, t)) {
      totflow += amt;
      for (int x = t; x != s; x = dad[x].first) {
        if (dad[x].second == 1) {
          flow[dad[x].first][x] += amt;
          totcost += amt * cost[dad[x].first][x];
        } else {
          flow[x][dad[x].first] -= amt;
          totcost -= amt * cost[x][dad[x].first];
        }
      }
    }
    return make_pair(totflow, totcost);
  }
};


void solve() {
  int n, c, m; cin >> n >> c >> m;
  vector<vector<int> > customers(c);
  int l=0, r=m;
  for (auto _ : irange(int(0), m)) {
    (void)_;
    int p, b; cin >> p >> b;
    --b; --p;
    customers[b].push_back(p);
    l = max(l, (int)customers[b].size());
  }
  for (auto& s : customers) sort(s.begin(), s.end());
  --l;
  if (c != 2) {
    cout << "N/A";
    return;
  }

  if (customers[0].size() < customers[1].size())
    swap(customers[0], customers[1]);

  int k=customers[0].size();
  int source=0;
  int sink=1;
  auto ticket=[&](int i){return 2+i;};
  auto day=[&](int i){return 2+k+i; };
  MinCostMaxFlow d(2+k+k);
  for (int i=0; i<customers[1].size(); ++i) {
    d.AddEdge(source, ticket(i), 1, 0);
    for (int j=0; j<customers[0].size(); ++j) {
      if (customers[1][i] == customers[0][j]) {
        if (customers[0][j] != 0) {
          d.AddEdge(ticket(i), day(j), 1, 1);
        }
      } else {
        d.AddEdge(ticket(i), day(j), 1, 0);
      }
    }
  }
  for (int i=0; i<customers[0].size(); ++i) {
    d.AddEdge(day(i), sink, 1, 0);
  }
  auto mf = d.GetMaxFlow(source, sink);
  int special = customers[1].size() - mf.first;
  cout << customers[0].size() + special << " " << mf.second;
}

int main() {
  int testcases; cin >> testcases;
  for (auto i : irange(int(1), testcases+1)) {;
    cout << "Case #" << i << ": ";
    solve();
    cout << '\n' << flush;
  }
}

/*
 * Local variables:
 * compile-command:"g++ -D_GLIBCXX_DEBUG -g3 -ggdb3 -O0 -Wall -Wextra -std=c++14 b.cc -o b && for f in *.in; do echo \"--- $f -------------\"; ./b <$f; done"
 * end:
 */

