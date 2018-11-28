#include <iostream>
#include <vector>
#include <cassert>
#include <algorithm>
#include <iomanip>

using namespace std;

struct rec {
  int u;
  int v;
  int who;
};

struct {
  bool operator()(rec a, rec b) { return a.u < b.u; }
} compareRec;

int rem(int a, int b) {
  return (a + b) % b;
}

int main() {
  int T;
  cin >> T;
  for (int t = 0; t < T; t++) {
    int tas, tbs;
    cin >> tas >> tbs;
    vector<rec> ws;
    for (int i = 0; i < tas; i++) {
      rec w;
      cin >> w.u >> w.v;
      w.who = 0;
      ws.push_back(w);
    }
    for (int i = 0; i < tbs; i++) {
      rec w;
      cin >> w.u >> w.v;
      w.who = 1;
      ws.push_back(w);
    }

    sort(ws.begin(), ws.end(), compareRec);


    // switch
    vector<vector<int> > fgaps(2);

    // same
    vector<vector<int> > ggaps(2);

    int switchCount = 0;

    // remaining required activity time
    int gone[2];
    gone[0] = 720;
    gone[1] = 720;

    for (int i = 0; i < ws.size(); i++) {
      auto a = ws[rem(i - 1, ws.size())];
      auto b = ws[i];
      gone[b.who] -= b.v - b.u;

      int gap = rem(b.u - a.v, 1440);
      if (a.who == b.who) {
        if (gap) ggaps[b.who].push_back(gap);
      } else {
        if (gap) fgaps[b.who].push_back(gap);
        switchCount += 1;
      }
    }


    for (int k = 0; k < 2; k++) {
      sort(ggaps[k].begin(), ggaps[k].end());
    }

    for (int k = 0; k < 2; k++) {
      for (int i = 0; i < ggaps[k].size(); i++) {
        int gap = ggaps[k][i];
        if (gone[k] - gap >= 0) {
          gone[k] -= ggaps[k][i];
        } else {
          switchCount += 2;
        }
      }
    }

    cout << setprecision(11);
    cout << "Case #" << (t + 1) << ": " << switchCount << endl;
  }

  return 0;
}
