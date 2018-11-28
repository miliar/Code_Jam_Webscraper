#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <set>
#include <map>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <queue>
#include <deque>
#include <cassert>

// O = R + Y
// G = Y + B
// V = R + B


// R: B, Y, G
// Y: R, B, V
// B: Y, R, O
// O: B
// G: R
// V: Y

using namespace std;

const std::string impossible = "IMPOSSIBLE";
double INFD = 1e18;
long long INF = INFD;

struct Char {
  char a, b;
  int n, m;
};

long long dists[200][200];

void solve() {
  unsigned int n, q;
  cin >> n >> q;
  vector<int> e(n), s(n);
  for (int i=0;i<n;++i)
    cin >> e[i] >> s[i];
  for (int i=0;i<n;++i)
    for (int j=0;j<n;++j) {
      cin >> dists[i][j];
      if (dists[i][j] == -1)
        dists[i][j] = INF;
    }
  vector<int> u(n), v(n);
  for (int i=0;i<q;++i)
    cin >> u[i] >> v[i];
  for (int k=0;k<n;++k)
    for (int i=0;i<n;++i)
      for (int j=0;j<n;++j)
        dists[i][j] = min(dists[i][j], dists[i][k] + dists[k][j]);
  vector<int> w;
  for (int t=0;t<q;++t) {
    vector<double> d(n * n, INFD);
    priority_queue < pair<double,int> > qu;
    int start = (u[t]-1) * n + (u[t]-1);
    d[start] = 0;
    qu.push(make_pair(0., start));
    while (!qu.empty()) {
      int cur = qu.top().second;
      int cur_h = cur / n;
      int cur_c = cur % n;
      double val = -qu.top().first;
      qu.pop();
      if (val > d[cur])
        continue;
      for (int j=0; j<n; ++j) {
        if (dists[cur_h][j] > e[cur_h] || dists[cur_h][j] == INF)
          continue;
        int next1 = cur_h * n + j;
        double next_v = d[cur] + 1.0 * dists[cur_h][j] / s[cur_h];
        int next2 = j * n + j;
        if (next_v < d[next1]) {
          d[next1] = next_v;
          qu.push(make_pair(-next_v, next1));
        }
        if (next_v < d[next2]) {
          d[next2] = next_v;
          qu.push(make_pair(-next_v, next2));
        }
      }
    }
    double res = INFD;
    for (int i=0;i<n;++i)
      res = min(res, d[i * n + v[t] - 1]);
    printf(" %.10f", res);
  }
}

int main() {
#ifdef LOCAL_RUN
  freopen("input.txt", "r", stdin);
#endif
  int t;
  cin >> t;
  for (int i=1;i<=t;++i) {
    cout << "Case #" << i << ":";
    solve();
    cout << endl;
  }
  return 0;
}