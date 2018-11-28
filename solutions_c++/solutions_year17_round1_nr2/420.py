#include <bits/stdc++.h>
using namespace std;
#define SZ(c) int((c).size())
#define ALL(c) (c).begin(),(c).end()
#define REP(i,n) for(int i=0;i<int(n);++i)
template<class T>inline void check_min(T&a,T b){if(b<a)a=b;}
template<class T>inline void check_max(T&a,T b){if(a<b)a=b;}
typedef long long int64;

const int N = 64;
const int INF = ~0U >> 2;

int n, p, r[N], q[N][N];
vector<pair<int, int>> qs[N];
priority_queue<int, vector<int>, greater<int>> pq[N];

void solve() {
  scanf("%d%d", &n, &p);
  for (int i = 1; i <= n; ++i) {
    scanf("%d", &r[i]);
    qs[i].clear();
    while (!pq[i].empty()) pq[i].pop();
  }
  for (int i = 1; i <= n; ++i) {
    for (int j = 1; j <= p; ++j) {
      scanf("%d", &q[i][j]);
      int lx = q[i][j] / (1.1 * r[i]);
      while (!(10LL * q[i][j] <= 11LL * lx * r[i])) ++lx;
      while (10LL * q[i][j] <= 11LL * (lx - 1) * r[i]) --lx;
      int rx = q[i][j] / (0.9 * r[i]);
      while (!(9LL * rx * r[i] <= 10LL * q[i][j])) --rx;
      while (9LL * (rx + 1) * r[i] <= 10LL * q[i][j]) ++rx;
      if (lx <= rx) qs[i].push_back(make_pair(lx, rx));
    }
    sort(ALL(qs[i]));
  }

  int ans = 0;
  while (true) {
    bool ah = true;
    for (int i = 1; i <= n; ++i) if (pq[i].empty()) {
      ah = false;
      break;
    }
    if (ah) {
      ++ans;
      for (int i = 1; i <= n; ++i) pq[i].pop();
      continue;
    }

    int o = 0;
    for (int i = 1; i <= n; ++i) {
      if (qs[i].empty()) continue;
      if (o == 0 || qs[i][0] < qs[o][0]) o = i;
    }
    if (o == 0) break;

    for (int i = 1; i <= n; ++i) {
      while (!pq[i].empty() && pq[i].top() < qs[o][0].first) {
        pq[i].pop();
      }
    }

    pq[o].push(qs[o][0].second);
    qs[o].erase(qs[o].begin());
  }

  printf("%d\n", ans);
}

int main() {
  int n_case;
  scanf("%d", &n_case);
  for (int index = 1; index <= n_case; ++index) {
    printf("Case #%d: ", index);
    solve();
  }
  return 0;
}
