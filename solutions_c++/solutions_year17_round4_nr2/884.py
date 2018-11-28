#include <bits/stdc++.h>
using namespace std;

#define fi first
#define se second
#define ALL(a) begin(a), end(a)
#define SZ(a) ((int)(a).size())

#ifdef __DEBUG
#define debug if (true)
#else
#define debug if (false)
#endif

typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);
  int T;
  cin >> T;
  while (T--) {
    int n, c, m;
    cin >> n >> c >> m;
    vector<pii> a(m);
    for (int i = 0; i < m; i++) {
      cin >> a[i].fi >> a[i].se;
      a[i].se--;
    }
    sort(ALL(a));
    vector<set<int>> trains;
    for (int i = 0; i < m; i++) {
      int pos = -1;
      for (int j = 0; j < SZ(trains); j++) {
        if (SZ(trains[j]) < a[i].fi && trains[j].count(a[i].se) == 0) {
          pos = j;
        }
      }
      if (pos == -1) {
        trains.push_back({});
        pos = SZ(trains) - 1;
      }
      trains[pos].insert(a[i].se);
    }
    int cnt = SZ(trains);
    for (auto &it : trains) {
      it.clear();
    }
    vi minPos(cnt, 1e9);
    int cost = 0;
    for (int i = m - 1; i >= 0; i--) {
      int pos = -1;
      for (int j = 0; j < SZ(trains); j++) {
        if (pos == -1 || minPos[pos] < minPos[j]) {
          pos = j;
        }
      }
      if (minPos[pos] > a[i].fi) {
        minPos[pos] = a[i].fi;
      } else {
        cost++;
      }
    }
    static int caseNo = 1;
    printf("Case #%d: %d %d\n", caseNo++, cnt, cost);
  }
  return 0;
}

