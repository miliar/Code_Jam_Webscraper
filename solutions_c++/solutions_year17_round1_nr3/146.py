#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <algorithm>
#include <cmath>
#include <set>
#include <queue>
#include <cstring>
#define ll long long
using namespace std;

struct data {
  int hd, ad, hk, ak, idx;
  data() {
    idx = 0;
  }
  data(int hd, int ad, int hk, int ak, int idx) {
    this->hd = hd;
    this->ad = ad;
    this->hk = hk;
    this->ak = ak;
    this->idx = idx;
  }
};

bool vis[101][101][101][101];

void init(data &now, int &nhd, int &nad, int &nhk, int &nak, int &nidx) {
  nhd = now.hd;
  nad = now.ad;
  nhk = now.hk;
  nak = now.ak;
  nidx = now.idx + 1;
}
int main() {
  int tk;
  cin >> tk;
  for (int tk1 = 1; tk1 <= tk; tk1++) {
    int hd, ad, hk, ak, b, d;
    cin >> hd >> ad >> hk >> ak >> b >> d;
    memset(vis, 0, sizeof(vis));
    int res = INT_MAX;

    queue<data> que;
    que.push(data(hd, ad, hk, ak, 0));
    vis[hd][ad][hk][ak] = true;
    int cnt = 0;
    while (!que.empty()) {
      cnt++;
      // if (cnt >= 1000000) {
      //   break;
      // }
      data now = que.front();
      // cout << now.hd << ", " << now.ad << ", " << now.hk << ", " << now.ak << endl;
      que.pop();
      int nhd = now.hd;
      int nad = now.ad;
      int nhk = now.hk;
      int nak = now.ak;
      int nidx = now.idx + 1;

      init(now, nhd, nad, nhk, nak, nidx);
      nhk -= nad;
      if (nhd > 0 && nhk <= 0) {
        res = now.idx;
        break;
      }
      nhd -= nak;
      if (nhd > 0 && !vis[nhd][nad][nhk][nak]) {
        que.push(data(nhd, nad, nhk, nak, nidx));
        vis[nhd][nad][nhk][nak] = true;
      }

      if (b > 0 && nad < 100) {
        init(now, nhd, nad, nhk, nak, nidx);
        nad += b;
        nad = min(nad, 100);
        nhd -= nak;
        if (nhd > 0 && !vis[nhd][nad][nhk][nak]) {
          que.push(data(nhd, nad, nhk, nak, nidx));
          vis[nhd][nad][nhk][nak] = true;
        }
      }

      if (d > 0 && nak > 0) {
        init(now, nhd, nad, nhk, nak, nidx);
        nak -= d;
        nak = max(0, nak);
        nhd -= nak;
        if (nhd > 0 && !vis[nhd][nad][nhk][nak]) {
          que.push(data(nhd, nad, nhk, nak, nidx));
          vis[nhd][nad][nhk][nak] = true;
        }
      }

      init(now, nhd, nad, nhk, nak, nidx);
      nhd = hd;
      nhd -= nak;
      if (nhd > 0 && !vis[nhd][nad][nhk][nak]) {
        que.push(data(nhd, nad, nhk, nak, nidx));
        vis[nhd][nad][nhk][nak] = true;
      }
    }


    if (res == INT_MAX) {
      cout << "Case #" << tk1 << ": IMPOSSIBLE" << endl;
      continue;
    }
    cout << "Case #" << tk1 << ": " << res + 1 << endl;
  }
  return 0;
}
