#include <bits/stdc++.h>
//#include <boost/range/irange.hpp>
//#include <boost/range.hpp>
#include "../../prettyprint.hpp"
using namespace std;

#ifdef NDEBUG
#include <boost/iostreams/stream.hpp>
#include <boost/iostreams/device/null.hpp>
boost::iostreams::stream<boost::iostreams::null_sink> logs((boost::iostreams::null_sink()));
#else
auto& logs = cerr;
#endif

using int_ = int;
#define int int_fast64_t

struct node {
  vector<pair<int, int> > adj;
  int last_used=0;
  int maxdist, speed;

  friend ostream& operator<<(ostream& os, node const& n) {
    return os << "(node " << n.adj << " " << n.last_used << " " << n.maxdist << " " << n.speed << ")";
  }
};

vector<int> dijkstra(vector<node> const& g, int a) {
  priority_queue<pair<int, int>,
                 vector<pair<int, int> >,
                 greater<pair<int, int>> > pq;
  pq.emplace(0, a);
  vector<int> dist(g.size(), -1);
  while (!pq.empty()) {
    int n, d; tie(d, n) = pq.top(); pq.pop();
    if (dist[n] != -1)
      continue;
    dist[n] = d;
    for (auto& nb : g[n].adj)
      pq.emplace(d + nb.second, nb.first);
  }
  return dist;
}

double dijkstra2(vector<node>& g, int a, int b) {
  for (auto& n : g)
    n.last_used = -1;
  struct mycmp {
    bool operator()(tuple<double, int, int, int> a,
                    tuple<double, int, int, int> b) {
      double a1; int a2, a3, a4; tie(a1, a2, a3, a4) = a;
      double b1; int b2, b3, b4; tie(b1, b2, b3, b4) = b;
      // minimize dist, maximize speed, maximize remaining dist, don't care about node
      return make_tuple(-a1, a2, a3, a4)
        <    make_tuple(-b1, b2, b3, b4);
    }
  };

  //                   dist,curr speed,remaining dist,node
  priority_queue<tuple<double, int, int, int>,
                 vector<tuple<double, int, int, int> >,
                 mycmp> pq;
  pq.emplace(0, 0, 0, a);
  while (!pq.empty()) {

    double t; int speed, cap, nd;
    tie(t, speed, cap, nd) = pq.top();
    //cout << "at " << pq.top() << '\n';
    pq.pop();

    auto& n = g[nd];

    if (nd == b) {
      //cout << "return " << t << '\n';
      return t;
    }

    if (n.last_used == -1) {
      for (auto& nb : g[nd].adj)
        if (nb.second <= n.maxdist)
          pq.emplace(t + nb.second/(double)n.speed,
                     n.speed,
                     n.maxdist - nb.second,
                     nb.first);
      n.last_used = 0;
    }
  }

  return -1;
}

int solve() {
  int n, q; cin >> n >> q;
  vector<node> g(n);
  for (int i=0; i<n; ++i)
    cin >> g[i].maxdist >> g[i].speed;
  for (int i=0; i<n; ++i) {
    for (int j=0; j<n; ++j) {
      int x; cin >> x;
      if (x==-1)
        continue;
      g[i].adj.emplace_back(j, x);
    }
  }

  {
    vector<vector<int> > dists(n);
    for (int i=0; i<n; ++i)
      dists[i] = dijkstra(g, i);
    for (int i=0; i<n; ++i) {
      g[i].adj.clear();
      for (int j=0; j<n; ++j)
        if (i != j && dists[i][j] != -1)
          g[i].adj.emplace_back(j, dists[i][j]);
      sort(g[i].adj.begin(), g[i].adj.end(),
           [&](pair<int, int> lhs,
               pair<int, int> rhs) {
             int a1, a2, b1, b2;
             tie(a1, a2) = lhs;
             tie(b1, b2) = rhs;
             return make_pair(a2, a1) < make_pair(b2, b1);
           });
    }
  }

  //cout << g << '\n';

  while (q--) {
    int u, v;
    cin >> u >> v;
    cout << " " << dijkstra2(g, u-1, v-1);
  }
  return 0;
}

int_ main() {
  int testcases; cin >> testcases;
  for (int i=1; i<=testcases; ++i) {
    cout << "Case #" << i << ":" << setprecision(10);
    solve();
    cout << '\n';
  }
}

/*
 * Local variables:
 * compile-command:"g++ -D_GLIBCXX_DEBUG -g3 -ggdb3 -O0 -Wall -Wextra -std=c++14 c.cc -o c && for f in *.in; do echo \"--- $f -------------\"; ./c <$f; done"
 * end:
 */
