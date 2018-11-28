#include <bits/stdc++.h>

#define DEBUG(x) cerr << #x << " = " << x << endl

using namespace std;

typedef long double ld;
typedef long long ll;
typedef vector<int> VI;
typedef vector<VI> V2I;
typedef vector<V2I> V3I;
typedef vector<V3I> V4I;

template <class Ta, class Tb> inline Tb cast(Ta a) {
  stringstream ss;
  ss << a;
  Tb b;
  ss >> b;
  return b;
};

vector<int> state(int hd, int bc, int hk, int dc) {
  vector<int> v(4);
  v[0] = hd;
  v[1] = bc;
  v[2] = hk;
  v[3] = dc;
  return v;
}

int main() {
  int T;
  cin >> T;
  for (int ca = 1; ca <= T; ++ca) {
    cout << "Case #" << ca << ": ";
    int hd0, ad0, hk0, ak0, b, d;
    cin >> hd0 >> ad0 >> hk0 >> ak0 >> b >> d;
    V4I dist(hd0 + 1, V3I(hk0, V2I(hk0 + 1, VI(ak0 + 1, -1))));
    queue<vector<int> > q;
    dist[hd0][0][hk0][0] = 0;
    q.push(state(hd0, 0, hk0, 0));
    int ans = -1;
    for (; !q.empty() && ans == -1;) {
      vector<int> cur = q.front();
      q.pop();
      int hd = cur[0];
      int bc = cur[1];
      int hk = cur[2];
      int dc = cur[3];

      if (hd == 0) {
        continue;
      }

      vector<vector<int> > nxt;
      int ad = ad0 + b * bc;
      nxt.push_back(state(hd, bc, max(0, hk - ad), dc));
      if (bc + 1 < int(dist[0].size())) {
        nxt.push_back(state(hd, bc + 1, hk, dc));
      }
      nxt.push_back(state(hd0, bc, hk, dc));
      if (dc + 1 < int(dist[0][0].size())) {
        nxt.push_back(state(hd, bc, hk, dc + 1));
      }

      for (int i = 0; i < int(nxt.size()); ++i) {
        if (nxt[i][2] > 0) {
          int ak = max(0, ak0 - nxt[i][3] * d);
          nxt[i][0] = max(0, nxt[i][0] - ak);
        } else {
          ans = dist[hd][bc][hk][dc] + 1;
        }
        if (dist[nxt[i][0]][nxt[i][1]][nxt[i][2]][nxt[i][3]] == -1) {
          dist[nxt[i][0]][nxt[i][1]][nxt[i][2]][nxt[i][3]] = dist[hd][bc][hk][dc] + 1;
          q.push(nxt[i]);
        }
      }
    }
    if (ans == -1) {
      cout << "IMPOSSIBLE";
    } else {
      cout << ans;
    }
    cout << endl;
  }
}
