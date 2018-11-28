#include <cstdio>
#include <string>
#include <iostream>
#define min(a, b) (a < b ? a : b)
using namespace std;

int e[1000], s[1000];
int dis[1000][1000];
long long d[1000];
double t[1000];

int main() {
  int T;
  cin >> T;

  for (int _ = 1; _ <= T; ++_) {
    cout << "Case #" << _ << ": ";

    int n, q;
    cin >> n >> q;
    for (int i = 0; i < n; ++i) {
      cin >> e[i] >> s[i];
    }
    for (int i = 0; i < n; ++i) {
      for (int j = 0; j < n; ++j) {
        cin >> dis[i][j];
      }
    }
    int a;
    cin >> a >> a;

    d[n - 1] = 0;
    for (int i = n - 2; i >= 0; --i) {
      d[i] = d[i + 1] + (long long)dis[i][i + 1];
    }

    t[n - 1] = 0;
    for (int i = n - 2; i >= 0; --i) {
      t[i] = 1e12;
      for (int j = i + 1; j < n; ++j) {
        if (e[i] >= d[i] - d[j]) {
          double tt = t[j] + double(d[i] - d[j]) / s[i];
          t[i] = min(t[i], tt);
        }
      }
    }

    printf("%0.9f\n", t[0]);
  }
  return 0;
}
