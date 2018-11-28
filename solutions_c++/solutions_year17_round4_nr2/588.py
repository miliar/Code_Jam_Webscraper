// CONTEST SOURCE
#include <iostream>
#include <cstdlib>
#include <cstring>
#include <cstdio>
#include <vector>
#include <cmath>
#include <algorithm>
#include <map>
#include <queue>
#include <set>
#include <climits>
//#include <priority_queue>
using namespace std;
#define ll long long
#define x first
#define y second
#define pii pair<int, int>
#define pdd pair<double, double>
#define L(s) (int)(s).size()
#define VI vector<int>
#define all(s) (s).begin(), (s).end()
#define pb push_back
#define mp make_pair

const int V = 1005, E = 1000000;
struct MinCostFlow {
  int last[V + 1], nx[2 * E + 2], ver[2 * E + 2], pr[V + 1], S, T, ec;
  int cap[2 * E + 2], curcap[V + 1];
  int cost[2 * E + 2], ds[2 * E + 2];
  queue<pair<int, int> > q;
  inline void reset() {
    memset(last, -1, sizeof(last));
    ec = 0;
    while (!q.empty()) q.pop();
  }
  inline void addEdge(int v, int w, int cp, int cs) {
    ver[ec] = w;
    cap[ec] = cp;
    cost[ec] = cs;
    nx[ec] = last[v];
    last[v] = ec++;
    ver[ec] = v;
    cap[ec] = 0;
    cost[ec] = -cs;
    nx[ec] = last[w];
    last[w] = ec++;
  }
  inline bool dijkstra() {
    memset(pr, -1, sizeof(pr));
    memset(ds, 63, sizeof(ds));
    memset(curcap, 0, sizeof(curcap));
    int inf = 1e9;
    curcap[S] = inf;
    ds[S] = 0;
    while (!q.empty()) q.pop();
    q.push(make_pair(0, S));
    pr[S] = -1;
    while (!q.empty()) {
      int v = q.front().y;
      if (q.front().x != ds[v]) {
        q.pop();
        continue;
      }
      q.pop();
      for (int w = last[v]; w >= 0; w = nx[w]) {
        if (cap[w] && ds[v] + cost[w] < ds[ver[w]]) {
          pr[ver[w]] = w;
          ds[ver[w]] = ds[v] + cost[w];
          q.push(make_pair(ds[ver[w]], ver[w]));
          if (cap[w] < curcap[v])
            curcap[ver[w]] = cap[w];
          else
            curcap[ver[w]] = curcap[v];
        }
      }
    }
    return curcap[T] > 0;
  }
  inline pair<int, int> minCostFlow() {
    int fl = 0;
    int cs = 0;
    while (dijkstra()) {
      int add = curcap[T];
      fl += add;
      cs += ds[T] * add;
      int a = T, b = pr[T];
      while (b != -1) {
        cap[b] -= add;
        cap[b ^ 1] += add;
        a = ver[b ^ 1];
        b = pr[a];
      }
    }
    return make_pair(fl, cs);
  }
};
MinCostFlow F;

int t, n, m, c, cnt_who[1111], cnt_what[1111];
int main() {
  freopen("B-small-attempt0.in", "r", stdin);
  freopen("output.txt", "w", stdout);
  scanf("%d", &t);
  //t = 1;
  for(int tc = 1; tc <= t; ++tc) {
    cerr << tc << endl;
    scanf("%d%d%d", &n, &c, &m);
    //n = 1000; c = 1000; m = 1000;
    for(int i = 0; i < c; ++i) cnt_who[i] = 0;
    for(int i = 0; i < n; ++i) cnt_what[i] = 0;
    for(int i = 0; i < m; ++i) {
      int who, what;
      scanf("%d%d", &what, &who); --who; --what;
      //who = rand() % c; what = rand() % n;
      cnt_who[who]++;
      cnt_what[what]++;
    }
    int lbound = 0;
    for(int i = 0; i < c; ++i) lbound = max(lbound, cnt_who[i]);
    F.reset();
    F.S = n;
    F.T = n + 1;
    for(int i = 0; i < n; ++i) {
      F.addEdge(F.S, i, cnt_what[i], 0);
      F.addEdge(i, F.T, lbound, 0);
      for(int j = 0; j < i; ++j) {
        F.addEdge(i, j, m, 1);
      }
    }
    int tot_flow = 0;
    int tot_cost = 0;
    while(1) {
      pair<int, int> cur = F.minCostFlow();
      tot_flow += cur.x;
      tot_cost += cur.y;
      if (tot_flow == m) {
        cout << "Case #" << tc << ": " << lbound << " " << tot_cost << endl;
        break;
      } else {
        for(int i = 0; i < F.ec; ++i) {
          if (F.ver[i] == F.T) ++F.cap[i];
        }
        ++lbound;
      }
    }
  }
}
