#include <bits/stdc++.h>

using namespace std;

typedef long long LL;
typedef vector<int> VI;
typedef vector<LL> VL;
typedef pair<int, int> PII;

const int N = 300004;

int main() {
  int T;
  cin >> T;
  for (int t = 1; t <= T; ++t) {
    cout << "Case #" << t << ": ";
    LL n, k, res = -1, x, y;
    cin >> n >> k;
    map<LL, LL> M;
    M[n] = 1;
    while (k > 0) {
      map<LL, LL> G;
      for (auto it = M.rbegin(); it != M.rend() && k > 0; ++it) {
        tie(x, y) = *it;
        k -= y; res = --x;
        G[x / 2] += y;
        G[x - (x / 2)] += y;
      }
      M = G;
    }
    cout << (res - res / 2) << " " << (res / 2) << "\n";
  }
  return 0;
}