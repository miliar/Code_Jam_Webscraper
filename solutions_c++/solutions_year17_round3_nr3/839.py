#include <cstdio>
#include <queue>
#include <vector>
#include <cstdlib>
#include <cmath>

using namespace std;

typedef long double ld;
typedef pair<ld,int> pdi;

int comp(ld a, ld b = 0.0) {
  if(fabs(a - b) < 1e-8) return 0;
  if(a > b) return -1;
  return 1;
}

vector<pdi> seq;

int main() {
  int t, n, k; scanf("%d", &t);
  ld tt, u;
  for(int cas = 1; cas <= t; ++cas) {
    scanf("%d %d", &n, &k);
    scanf("%Lf", &u);
    seq.clear();
    for(int i = 0; i < n; ++i) {
      scanf("%Lf", &tt);
      bool found = false;
      for(int j = 0; j < seq.size() && !found; ++j)
        if(comp(seq[j].first, tt) == 0) {
          found = true;
          seq[j] = {tt, seq[j].second + 1};
        }
      if(!found)
        seq.push_back({tt, 1});
    }
    priority_queue<pdi, vector<pdi>, greater<pdi> > fila;
    for(int i = 0; i < seq.size(); ++i)
      fila.push(seq[i]);
    while(comp(u) != 0) {
      pdi top = fila.top(); fila.pop();
      if(fila.empty()) {
        top = {top.first + u/top.second, top.second};
        fila.push(top);
        u = 0.0;
      } else {
        ld k = min((fila.top().first - top.first)*top.second, u);
        top = {top.first + k/top.second, top.second};
        u -= k;
        if(comp(fila.top().first, top.first) == 0) {
          top.second = top.second + fila.top().second;
          fila.pop();
          fila.push(top);
        } else {
          fila.push(top);
        }
      }
    }
    ld ans = 1.0;
    while(!fila.empty()) {
      pdi top = fila.top(); fila.pop();
      for(int i = 0; i < top.second; ++i) ans *= top.first;
    }
    printf("Case #%d: %.9Lf\n", cas, ans);
  }
  return 0;
}