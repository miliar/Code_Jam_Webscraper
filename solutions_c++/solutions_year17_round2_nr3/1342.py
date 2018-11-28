#include <iostream>

using namespace std;

const int MAXN = 100;
const __int128 INF = 1e28;
const __int128 SHIFT = 1e10;

__int128 horse[MAXN];
__int128 speed[MAXN];
__int128 dist[MAXN];
__int128 ans[MAXN];

int main() {
  int T;
  cin >> T;
  for (int t = 1; t <= T; ++t) {
    cout << "Case #" << t << ": ";
    cerr << "Case #" << t << ": ";
    int n, q;
    cin >> n >> q;
    for (int i = 0; i < n; ++i) {
      int hh, ss;
      cin >> hh >> ss;
      horse[i] = hh * SHIFT;
      speed[i] = ss;
      ans[i] = INF;
    }
    ans[0] = 0;
    for (int i = 0; i < n; ++i)
      for (int j = 0; j < n; ++j) {
        if (j == i + 1) {
          int dd;
          cin >> dd;
          dist[i] = dd * SHIFT;
        }
        else
          cin >> q;
      }
    cin >> q >> q;
    for (int i = 0; i < n - 1; ++i) {
      __int128 sum = 0;
      for (int j = i + 1; j < n && (sum += dist[j - 1]) <= horse[i]; ++j)
        ans[j] = min(ans[j], ans[i] + sum / speed[i]);
    }
    cerr.precision(10);
    cerr << fixed;
    for (int i = 0; i < n; ++i)
      cerr << dist[i] / (double)SHIFT << " ";
    cerr << endl;
    for (int i = 0; i < n; ++i)
      cerr << ans[i] / (double)SHIFT << " ";
    cerr << endl;
    cout.precision(10);
    cout << fixed;
    cout << ans[n - 1] / (double)SHIFT << endl;
  }
  return 0;
}