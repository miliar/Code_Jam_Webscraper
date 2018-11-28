
// I copied the max bipartite matching algorithm from
// http://www.geeksforgeeks.org/maximum-bipartite-matching/

#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <unordered_map>
#include <unordered_set>
#include <algorithm>
#include <utility>
#include <memory>
#include <cstring>

using namespace std;

bool bpm(vector<vector<bool>> &bpGraph, int u, vector<bool> &seen, vector<int> &matchR) {
  auto N = bpGraph.size();
  for (int v = 0; v < N; v++) {
    if (bpGraph[u][v] && !seen[v]) {
      seen[v] = true;
      if (matchR[v] < 0 || bpm(bpGraph, matchR[v], seen, matchR)) {
        matchR[v] = u;
        return true;
      }
    }
  }
  return false;
}

vector<int> maxBPM(vector<vector<bool>> &bpGraph) {
  auto N = bpGraph.size();
  vector<int> matchR(N, -1);
  for (int u = 0; u < N; u++) {
    vector<bool> seen(N, false);
    bpm(bpGraph, u, seen, matchR);
  }
  return matchR;
}

using row = vector<char>;
using grid = vector<row>;

int main() {
  freopen("in", "r", stdin);
  freopen("out", "w", stdout);

  int cases; cin >> cases;
  for (int cas = 1; cas <= cases; ++cas) {
    int n, m; cin >> n >> m;
    grid init = grid(n, row(n, '.'));
    for (int i = 0; i < m; ++i) {
      char x; int r, c; cin >> x >> r >> c;
      --r; --c;
      init[r][c] = x;
    }
    auto init2 = init;

    // make the thing
    vector<vector<bool>> thing(n, vector<bool>(n, true));
    for (int r = 0; r < n; ++r) {
      for (int c = 0; c < n; ++c) {
        char ch = init[r][c];
        if (ch == 'x' || ch == 'o') {
          for (int i = 0; i < n; ++i) {
            thing[r][i] = thing[i][c] = false;
          }
        }
      }
    }

    // diagonal rotation
    auto rc_to_ab = [=](int r, int c) {
      return make_pair(r + c, n - 1 - r + c);
    };
    auto ab_to_rc = [=](int a, int b) {
      return make_pair((a - b + n - 1) / 2, (a + b - n + 1)/2);
    };

    // make the other thing
    int nn = 2 * n - 1;
    vector<vector<bool>> thing2(nn, vector<bool>(nn, false));
    for (int r = 0; r < n; ++r) {
      for (int c = 0; c < n; ++c) {
        char ch = init[r][c];
        auto ab = rc_to_ab(r, c);
        thing2[ab.first][ab.second] = thing2[ab.second][ab.first] = true;
      }
    }
    for (int r = 0; r < n; ++r) {
      for (int c = 0; c < n; ++c) {
        char ch = init[r][c];
        if (ch == '+' || ch == 'o') {
          auto ab = rc_to_ab(r, c);
          for (int i = 0; i < nn; ++i) {
            thing2[ab.first][i] = thing2[i][ab.second] = false;
          }
        }
      }
    }
    /*
    for (int a = 0; a < nn; ++a) {
      for (int b = 0; b < nn; ++b) {
        cout << thing2[a][b];
      }
      cout << endl;
    }
    cout << "\n----\n\n";

    for (int r = 0; r < n; ++r) {
      for (int c = 0; c < n; ++c) {
        cout << init[r][c];
      }
      cout << endl;
    }
    cout << "\n----\n\n";
    */

    auto xs = maxBPM(thing);
    auto ps = maxBPM(thing2);
    /*for (int i = 0; i < ps.size(); ++i) {
      cout << ":" << ps[i];
    }
    cout << "\n\n";*/
    for (int c = 0; c < xs.size(); ++c) {
      if (xs[c] == -1) continue;
      if (init[xs[c]][c] == '.') {
        init[xs[c]][c] = 'x';
      } else {
        init[xs[c]][c] = 'o';
      }
    }
    for (int b = 0; b < ps.size(); ++b) {
      if (ps[b] == -1) continue;
      int r, c;
      tie(r, c) = ab_to_rc(ps[b], b);
      if (init[r][c] == '.') {
        init[r][c] = '+';
      } else {
        init[r][c] = 'o';
      }
    }

    /*for (int r = 0; r < n; ++r) {
      for (int c = 0; c < n; ++c) {
        cout << init[r][c];
      }
      cout << endl;
    }
    cout << "\n\n";*/

    int score = 0;
    vector<int> addr, addc;
    vector<char> addch;
    for (int r = 0; r < n; ++r) {
      for (int c = 0; c < n; ++c) {
        char x = init[r][c];
        if (x == '+' || x == 'x') score += 1;
        if (x == 'o') score += 2;
        if (x != init2[r][c]) {
          addr.push_back(r);
          addc.push_back(c);
          addch.push_back(x);
        }
      }
    }

    cout << "Case #" << cas << ": " << score << " " << addr.size() << endl;
    for (int i = 0; i < addr.size(); ++i) {
      cout << addch[i] << " " << (addr[i] + 1) << " " <<
        (addc[i] + 1) << endl;
    }
  }
  return 0;
}
