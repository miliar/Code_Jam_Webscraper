// C.cpp

#include <iostream>
#include <queue>
#include <vector>
using namespace std;

struct Horse {
  int e, s;
  Horse(int _e, int _s) : e(_e), s(_s) {}
};

const int MAXN = 100;
long long d[MAXN + 1][MAXN + 1];
double f[MAXN + 1][MAXN + 1];

int main() {
  int t, kase = 0;
  cin >> t;
  while (t--) {
    int n, q;
    cin >> n >> q;
    vector<Horse> horses;
    horses.push_back(Horse(-1, -1));
    for (int i = 1; i <= n; i++) {
      int e, s;
      cin >> e >> s;
      horses.push_back(Horse(e, s));
    }
    for (int i = 1; i <= n; i++) {
      for (int j = 1; j <= n; j++) {
        cin >> d[i][j];
      }
    }
    for (int k = 1; k <= n; k++) {
      for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= n; j++) {
          if (d[i][k] != -1 && d[k][j] != -1) {
            if (d[i][j] == -1) {
              d[i][j] = d[i][k] + d[k][j];
            } else {
              d[i][j] = min(d[i][j], d[i][k] + d[k][j]);
            }
          }
        }
      }
    }
    cout << "Case #" << ++kase << ": ";
    while (q--) {
      int u, v;
      cin >> u >> v;
      for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= n; j++) {
          f[i][j] = -1;
        }
      }
      double min_time[MAXN];
      for (int i = 1; i <= n; i++) {
        min_time[i] = 1e20;
      }
      queue<pair<int, double>> q;
      q.push(make_pair(u, 0));
      min_time[u] = 0;
      while (!q.empty()) {
        pair<int, double> curr = q.front();
        q.pop();
        // cout << curr.first << " " << curr.second << endl;
        for (int i = 1; i <= n; i++) {
          if (d[curr.first][i] != -1) {
            if (horses[curr.first].e >= d[curr.first][i]) {
              double t =
                  curr.second + 1.0 * d[curr.first][i] / horses[curr.first].s;
              if (min_time[i] > t) {
                min_time[i] = t;
                /*
                printf(
                    "curr.first = %d, curr.second = %lf, min_time[%d] = %lf\n",
                    curr.first, curr.second, i, t);
                */
                q.push(make_pair(i, t));
              }
            }
          }
        }
      }
      printf("%.6lf ", min_time[v]);
    }
    cout << endl;
  }
  return 0;
}