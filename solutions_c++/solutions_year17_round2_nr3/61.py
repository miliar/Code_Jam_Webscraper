#include <algorithm>
#include <iostream>
#include <string>
#include <utility>
#include <vector>
using namespace std;

typedef long long ll;
typedef long double ld;
typedef vector<ll> Vi;
typedef vector<Vi> Mi;
typedef vector<ld> Vd;
typedef vector<Vd> Md;

const ll INF = 1000000000000000000LL;

int main() {
  cout.setf(ios::fixed);
  cout.precision(9);

  int tcas;
  cin >> tcas;
  for (int cas = 1; cas <= tcas; ++cas) {
    int n, q;
    cin >> n >> q;
    Vi e(n), s(n);
    for (int i = 0; i < n; ++i) {
      cin >> e[i] >> s[i];
    }
    Mi d(n, Vi(n));
    for (int i = 0; i < n; ++i) {
      for (int j = 0; j < n; ++j) {
        cin >> d[i][j];
      }
    }

    Mi dist(n, Vi(n, INF));
    for (int i = 0; i < n; ++i) {
      dist[i][i] = 0;
    }
    for (int i = 0; i < n; ++i) {
      for (int j = 0; j < n; ++j) {
        if (d[i][j] != -1) {
          dist[i][j] = d[i][j];
        }
      }
    }
    for (int k = 0; k < n; ++k) {
      for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
          if (dist[i][j] > dist[i][k] + dist[k][j]) {
            dist[i][j] = dist[i][k] + dist[k][j];
          }
        }
      }
    }

    Md temps(n, Vd(n, INF));
    for (int i = 0; i < n; ++i) {
      temps[i][i] = 0;
    }
    for (int i = 0; i < n; ++i) {
      for (int j = 0; j < n; ++j) {
        if (e[i] >= dist[i][j]) {
          temps[i][j] = ld(dist[i][j])/ld(s[i]);
        }
      }
    }
    for (int k = 0; k < n; ++k) {
      for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
          if (temps[i][j] > temps[i][k] + temps[k][j]) {
            temps[i][j] = temps[i][k] + temps[k][j];
          }
        }
      }
    }

    cout << "Case #" << cas << ":";
    for (int i = 0; i < q; ++i) {
      int x, y;
      cin >> x >> y;
      --x; --y;
      cout << " " << temps[x][y];
    }
    cout << endl;
  }
}
