#include <iostream>
#include <string>
#include <vector>
#include <map>
#define ll long long
using namespace std;

int main() {
  int tk;
  cin >> tk;
  for (int tk1 = 1; tk1 <= tk; tk1++) {
    int n, m;
    cin >> n >> m;
    vector<string> a(n);
    for (int i = 0; i < n; i++) {
      cin >> a[i];
    }
    vector<bool> vis(n);
    for (int i = 0; i < n; i++) {
      for (int j = 0; j < m; j++) {
        if (a[i][j] != '?') {
          vis[i] = true;
        }
      }
    }
    vector<vector<char> > res(n, vector<char>(m));
    for (int i = 0; i < n; i++) {
      if (vis[i]) {
        char now = 0;
        for (int j = 0; j < m; j++) {
          if (a[i][j] != '?') {
            now = a[i][j];
          }
          res[i][j] = now;
        }
        for (int j = m - 1; j >= 0; j--) {
          if (a[i][j] != '?') {
            now = a[i][j];
          }
          res[i][j] = now;
        }
      }
    }
    vector<char> now;
    for (int i = 0; i < n; i++) {
      if (vis[i]) {
        now = res[i];
      }
      res[i] = now;
    }
    for (int i = n - 1; i >= 0; i--) {
      if (vis[i]) {
        now = res[i];
      }
      res[i] = now;
    }
    cout << "Case #" << tk1 << ":" << endl;
    for (int i = 0; i < n; i++) {
      for (int j = 0; j < m; j++) {
        cout << res[i][j];
      }
      cout << endl;
    }
  }
  return 0;
}
