#include <cstdio>
#include <cassert>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <complex>
#include <numeric>
#include <ext/numeric>
#include <iostream>
#include <algorithm>
#include <set>
#include <string>
#include <map>
#include <functional>
#include <utility>
#include <vector>
#include <list>
#include <queue>
#include <bitset>
#include <tuple>
#include <boost/format.hpp>

using namespace std;
using namespace __gnu_cxx;

typedef unsigned long long ullong;
typedef long long llong;

struct Edge {
  int a, b;
  long double c;
  Edge(int a, int b, long double c) : a(a), b(b), c(c) {}
};

typedef list<Edge> EdgeList;
typedef vector<EdgeList> AdjList;
typedef pair<int, int> ii;
typedef pair<llong, llong> ll;
typedef vector<ii> vii;
typedef complex<double> Point;
#define X(p) real(p)
#define Y(p) imag(p)

#define FOR_EDGE(adj,v,it) for (EdgeList::iterator it = adj[v].begin(); \
    it != adj[v].end(); ++it)
#define FOR(v, it) for (auto it = v.begin(); it != v.end(); ++it)

int n, q;
llong mat[128][128];
llong apsp[128][128];
AdjList adj;
ll horses[128];
long double dists[128];

struct PQNode {
  long double dist;
  int v;
  PQNode(long double dist, int v): dist(dist), v(v) {}
  bool operator<(PQNode const& other) const {
    return tie(dist, v) > tie(other.dist, other.v);
  }
};

int main() {
  cin.tie(nullptr);
  ios_base::sync_with_stdio(false);
  int n_cases;
  scanf("%d", &n_cases);
  for (int ctr = 0; ctr < n_cases; ++ctr) {
    adj.clear();
    scanf("%d %d", &n, &q);
    memset(mat, 0, sizeof(mat));
    for (int i = 0; i < n; ++i) {
      scanf("%lld %lld", &horses[i].first, &horses[i].second);
    }
    for (int i = 0; i < n; ++i) {
      for (int j = 0; j < n; ++j) {
        scanf("%lld", &mat[i][j]);
        apsp[i][j] = mat[i][j];
      }
    }

    for (int k = 0; k < n; ++k) {
      for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
          if (i == j) continue;
          if (apsp[i][k] == -1 || apsp[k][j] == -1) continue;
          if (apsp[i][j] == -1 || apsp[i][j] > apsp[i][k] + apsp[k][j]) {
            apsp[i][j] = apsp[i][k] + apsp[k][j];
          }
        }
      }
    }

    #ifdef  DEBUG
    puts("matrix");
    for (int i = 0; i < n; ++i) {
      for (int j = 0; j < n; ++j) {
        printf(" %lld", mat[i][j]);
      }
      puts("");
    }
    puts("apsp");
    for (int i = 0; i < n; ++i) {
      for (int j = 0; j < n; ++j) {
        printf(" %lld", apsp[i][j]);
      }
      puts("");
    }
    #endif

    adj.resize(n);
    for (int i = 0; i < n; ++i) {
      llong energy;
      llong speed;
      tie(energy, speed) = horses[i];
      for (int j = 0; j < n; ++j) {
        if (i == j) continue;
        if (apsp[i][j] != -1 && apsp[i][j] <= energy) {
          adj[i].push_back(Edge(i, j, apsp[i][j]/(long double)speed));
        }
      }
    }
    #ifdef  DEBUG
    puts("adj");
    for (int v = 0; v < n; ++v) {
      printf("%d (%d): ", v, adj[v].size());
      FOR_EDGE(adj, v, it) {
        auto e = *it;
        printf("(%d, %Lf) ", e.b, e.c);
      }
      puts("");
    }
    #endif

    printf("Case #%d:", ctr+1);

    for (int i = 0; i < q; ++i) {
      int start, dest;
      scanf("%d %d", &start, &dest);
      --start; --dest;
      fill(dists, dists+n, -1);
      priority_queue<PQNode> pq;
      pq.push(PQNode(0, start));
      while (pq.size()) {
        auto top = pq.top();
        long double dist = top.dist;
        int v = top.v;
        pq.pop();
        if (dists[v] != -1) continue;
        dists[v] = dist;
        if (v == dest) break;
        FOR_EDGE(adj, v, it) {
          int o = it->b;
          long double c = it->c;
          if (dists[o] != -1) continue;
          pq.push(PQNode(dist + c, o));
        }
      }

      printf(" %.6Lf", dists[dest]);
    }
    puts("");

  }
  return 0;
}
