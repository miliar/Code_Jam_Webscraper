#include <bits/stdc++.h>
#include <iomanip>
#include <iostream>
#include <memory>
#include <string>
#include <vector>

using std::cin;
using std::cout;
using std::endl;
using std::string;
using std::vector;

using ll = long long;
using ld = long double;
const string filename = "";

template <class T>
T sqr(T x) {
  return x * x;
}

void solve() {
  int T;
  cin >> T;
  for (int i = 0; i < T; ++i) {
    int N;
    int R, O, Y, G, B, V;
    cin >> N;
    cin >> R >> O >> Y >> G >> B >> V;
    vector<std::pair<ll, char>> colors = {{R, 'R'}, {Y, 'Y'}, {B, 'B'}};
    std::sort(colors.rbegin(), colors.rend());
    cout << "Case #" << i + 1 << ": ";
    if (colors[0].first > (1.0 * N) / 2) {
      cout << "IMPOSSIBLE" << endl;
    } else {
      // 2 2 1
      // RBRBG
      int triplets = colors[0].first;
      int cur_t = 0;
      while (cur_t < triplets) {
        cout << colors[0].second;
        if (cur_t < colors[1].first) {
          cout << colors[1].second;
        }
        if (triplets - cur_t <= colors[2].first) {
          cout << colors[2].second;
        }
        cur_t++;
      }
      cout << endl;
    }
  }
}

int main() {
#ifdef DEBUG
#else
  if (!filename.empty()) {
    freopen((filename + ".in").c_str(), "r", stdin);
    freopen((filename + ".out").c_str(), "w", stdout);
  }

#endif

  cin.sync_with_stdio(false);
  cout << std::fixed << std::setprecision(10);
  solve();
  return 0;
}
