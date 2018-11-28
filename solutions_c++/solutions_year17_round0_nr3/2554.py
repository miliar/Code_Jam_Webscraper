#include <iostream>
#include <string>
#include <vector>
#include <stdio.h>
#include <string.h>
#include <map>
#include <set>
#include <queue>

#define REP(i, n) for (int (i) = 0; (i) < (n); ++(i))

typedef long long LL;

using namespace std;

void solve() {
  LL n, k;
  cin >> n >> k;

  map<LL, LL> M;
  set<LL> q;
  q.insert(-n);
  M[n] = 1;
  while(!q.empty()) {
    LL cur = -*q.begin();
    LL cnt = M[cur];
    q.erase(q.begin());
    if (cur == 0) continue;

    LL left = (cur - 1) / 2;
    LL right = cur - 1 - left;
    auto add = [&M, &q, cnt](LL x) {if (x) {M[x] += cnt; q.insert(-x);}};
    add(left);
    add(right);
  }

  --k;
  vector<pair<LL, LL>> a(M.rbegin(), M.rend());
  for (auto p: a) {
    LL v = p.first;
    LL c = p.second;
    if (k >= c) {
      k -= c;
    } else {
      if (v == 1) {
        cout << "0 0" << endl;
      } else {
        LL left = (v - 1) / 2;
        LL right = v - 1 - left;
        cout << right << " " << left << endl;
      }
      return;
    }
  }
}

int main() {
  int T;
  scanf("%d", &T);
  REP(i, T) {
    printf("Case #%d: ", i + 1);
    solve();
  }

  return 0;
}
