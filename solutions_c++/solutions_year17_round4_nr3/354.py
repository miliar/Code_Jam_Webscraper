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

void dfs(vector<pair<int, int> > &b, int idx, vector<int> &now, bool &done, int n, int m, vector<string> & a) {
  if (idx == b.size()) {
    for (int i = 0; i < n; i++) {
      for (int j = 0; j < m; j++) {
        if (a[i][j] == '.') {
          bool found = false;
          for (int k = 0; k < b.size(); k++) {
            if (b[k].first == i && now[k] == -1) {
              int mi = min(j, b[k].second), ma = max(j, b[k].second);
              bool blocked = false;
              for (int l = mi + 1; l < ma; l++) {
                if (a[b[k].first][l] == '#') {
                  blocked = true;
                  break;
                }
              }
              if (blocked) {
                continue;
              }
              found = true;
            }
            if (b[k].second == j && now[k] == 1) {
              int mi = min(i, b[k].first), ma = max(j, b[k].first);
              bool blocked = false;
              for (int l = mi + 1; l < ma; l++) {
                if (a[l][b[k].second] == '#') {
                  blocked = true;
                  break;
                }
              }
              if (blocked) {
                continue;
              }
              found = true;
            }
          }
          if (!found) {
            return;
          }
        }
      }
    }
    done = true;
    return;
  }
  if (now[idx] <= 0) {
    bool succ = true;
    for (int i = 0; i < b.size(); i++) {
      if (i != idx && b[i].first == b[idx].first) {
        int mi = min(b[i].second, b[idx].second), ma = max(b[i].second, b[idx].second);
        bool blocked = false;
        for (int j = mi + 1; j < ma; j++) {
          if (a[b[i].first][j] == '#') {
            blocked = true;
            break;
          }
        }
        if (blocked) {
          continue;
        }
        succ = false;
      }
    }
    if (succ) {
      int diff = now[idx] + 1;
      now[idx] -= diff;
      dfs(b, idx + 1, now, done, n, m, a);
      if (done) {
        return;
      }
      now[idx] += diff;
    }
  }
  if (now[idx] >= 0) {
    bool succ = true;
    for (int i = 0; i < idx; i++) {
      if (i != idx && b[i].second == b[idx].second) {
        int mi = min(b[i].first, b[idx].first), ma = max(b[i].first, b[idx].first);
        bool blocked = false;
        for (int j = mi + 1; j < ma; j++) {
          if (a[j][b[i].second] == '#') {
            blocked = true;
            break;
          }
        }
        if (blocked) {
          continue;
        }
        succ = false;
      }
    }
    if (succ) {
      int diff = now[idx] - 1;
      now[idx] -= diff;
      dfs(b, idx + 1, now, done, n, m, a);
      if (done) {
        return;
      }
      now[idx] += diff;
    }
  }
}
int main() {
  int tk;
  cin >> tk;
  for (int tk1 = 1; tk1 <= tk; tk1++) {
    cerr << "tk1 = " << tk1 << endl;
    int n, m;
    cin >> n >> m;
    vector<string> a(n);
    for (int i = 0; i < n; i++) {
      cin >> a[i];
    }
    vector<pair<int, int> > b;
    for (int i = 0; i < n; i++) {
      for (int j = 0; j < m; j++) {
        if (a[i][j] == '-' || a[i][j] == '|') {
          b.push_back(make_pair(i, j));
        }
      }
    }
    vector<int> now(b.size());
    bool fail = false;
    for (int i = 0; i < n; i++) {
      for (int j = 0; j < m; j++) {
        if (a[i][j] == '.') {
          int cnt = 0, idx = -1;
          for (int k = 0; k < b.size(); k++) {
            if (b[k].first == i) {
              int mi = min(j, b[k].second), ma = max(j, b[k].second);
              bool blocked = false;
              for (int l = mi + 1; l < ma; l++) {
                if (a[b[k].first][l] == '#') {
                  blocked = true;
                  break;
                }
              }
              if (blocked) {
                continue;
              }
              cnt++;
              idx = -(k + 1);
            }
            if (b[k].second == j) {
              int mi = min(i, b[k].first), ma = max(i, b[k].first);
              bool blocked = false;
              for (int l = mi + 1; l < ma; l++) {
                if (a[l][b[k].second] == '#') {
                  blocked = true;
                  break;
                }
              }
              if (blocked) {
                continue;
              }
              cnt++;
              idx = k + 1;
            }
          }
          if (cnt == 0) {
            fail = true;
          }
          if (cnt == 1) {
            now[abs(idx) - 1] = (idx > 0 ? 1 : -1);
          }
        }
      }
    }
    bool done = false;
    // cout << "fail = " << fail << endl;
    if (!fail) {
      dfs(b, 0, now, done, n, m, a);
    }
    cout << "Case #" << tk1 << ": ";
    if (done) {
      cout << "POSSIBLE" << endl;
      for (int i = 0; i < b.size(); i++) {
        if (now[i] == -1) {
          a[b[i].first][b[i].second] = '-';
        } else {
          a[b[i].first][b[i].second] = '|';
        }
      }
      for (int i = 0; i < n; i++) {
        cout << a[i] << endl;
      }
    } else {
      cout << "IMPOSSIBLE" << endl;;
    }
  }
  return 0;
}
