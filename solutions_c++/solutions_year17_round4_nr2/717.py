#include <algorithm>
#include <chrono>
#include <iostream>
#include <vector>

using namespace std;
using namespace std::chrono;

int main() {
  auto start = high_resolution_clock::now();

  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);

  int tests;
  cin >> tests;
  for (int test = 1; test <= tests; ++test) {
    int n, c, m;
    cin >> n >> c >> m;

    vector<vector<int>> cnt(c, vector<int>(n, 0));
    for (int i = 0; i < m; ++i) {
      int pos, id;
      cin >> pos >> id;
      --pos;
      --id;
      ++cnt[id][pos];
    }

    int rides = 0, promotions = 0;

    if (c == 2) {
      int b1 = 0, b2 = 0;
      for (int pos = 0; pos < n; ++pos) {
        b1 += cnt[0][pos];
        b2 += cnt[1][pos];
      }
      rides = max(b1, b2);

      for (int pos = 0; pos < n; ++pos) {
        if (cnt[0][pos] + cnt[1][pos] > rides) {
          if (pos == 0) {
            rides = cnt[0][pos] + cnt[1][pos];
            b1 -= cnt[0][pos] + cnt[1][pos];
            b2 -= cnt[1][pos] + cnt[0][pos];
            rides += max(0, max(b1, b2));
            break;
          } else {
            promotions = cnt[0][pos] + cnt[1][pos] - rides;
            break;
          }
        }
      }

    } else {
      rides = promotions = -1;
    }

    cout << "Case #" << test << ": " << rides << " " << promotions << endl;
  }

  cerr << "Total execution time : " << duration_cast<milliseconds>(high_resolution_clock::now() - start).count() << " ms" << endl;

  return 0;
}
