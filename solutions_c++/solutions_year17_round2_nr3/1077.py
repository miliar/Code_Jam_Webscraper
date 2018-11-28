#include <iostream>
#include <algorithm>
#include <stdio.h>
#include <vector>
#include <map>
#include <set>
#include <stdlib.h>
#include <string>
#include <iomanip>
#include <queue>
#include <unordered_map>
using namespace std;

const int N = 1000;

pair <long long, long long> horses[N];
long long g[N][N];

int main() {

  freopen("in", "r", stdin);
  freopen("out", "w", stdout);

  int testN; cin >> testN;

  for (int t = 1; t <= testN; t++) {
    cout << "Case #" << t << ": ";
    int n, q; cin >> n >> q;
    for (int i = 1; i <= n; i++) {
      cin >> horses[i].first >> horses[i].second;
    }
    for (int i = 1; i <= n; i++) {
      for (int j = 1; j <= n; j++) {
        cin >> g[i][j];
      }
    }

    int u, v; cin >> u >> v;
    vector <double> d(n + 1);
    d[1] = 0;
    for (int i = 2; i <= n; i++) {
      d[i] = -1;
      long long distance = 0;
      for (int j = i - 1; j > 0; j--) {
        distance += (long long) g[j][j + 1];
        if (distance <= horses[j].first) {
          if (d[i] == -1) d[i] = d[j] + distance / (double) horses[j].second;
          else d[i] = min(d[i], d[j] + distance / (double) horses[j].second);
        }
      }
    }

    cout << fixed << setprecision(10) << d[n] << "\n";
  }

  return 0;
}
