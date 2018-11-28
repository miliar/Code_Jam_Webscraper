#include <iostream>
#include <algorithm>
#include <utility>
#include <cmath>
#include <vector>

using namespace std;

const int MAX_N = 55;

int Q[MAX_N][MAX_N];
int R[MAX_N];

vector<int> ids;

bool good(int q, int r, int n) {
  double low = 0.9*r*n;
  double high = 1.1*r*n;
  double qq = q;

  // if (n == 5) {
  //   cout << "low " << low << " high " << high << endl;
  //   cout << "qq " << qq << endl;
  // }

  bool ans = low-1e-9 <= qq && qq <= high+1e-9;
  // if (n == 5)
  //   cout << " ans " << ans << endl;

  return ans;
}

bool good(int n) {
  for (int i = 0; i < (int) ids.size(); i++)
    if (!good(Q[i][ids[i]], R[i], n)) return false;
  return true;
}

pair<double, double> calc(int q, int r) {
  // cout << "q " << q << " r " << r << endl;

  double ll = 1.0 * q / (1.1 * r);
  double hh = 1.0 * q / (0.9 * r);

  return make_pair(ll, hh);

  // cout << "ll " << ll << " hh " << hh << endl;

  // int l = ceil(ll) + .1;
  // int h = floor(hh) + .1;

  // if (l > 1 && good(q, r, l - 1))
  //   l--;
  // if (good(q, r, h + 1))
  //   h++;

  // if (!good(q, r, l) && good(q, r, l + 1))
  //   l++;
  // if (h > 1 && !good(q, r, h) && good(q, r, h - 1))
  //   h--;

  // return make_pair(l, h);

  // int low = 1;
  // while (!good(q, r, low) && low < 1000000) low++;
  // int high = 1000000;
  // while (!good(q, r, high) && high > 0) high--;

  // return make_pair(low, high);
}

int main() {
  int t; cin >> t;
  int test = 0;
  while (t--) {
    int n, p; cin >> n >> p;

    for (int i = 0; i < n; i++)
      cin >> R[i];

    for (int i = 0; i < n; i++)
      for (int j = 0; j < p; j++)
        cin >> Q[i][j];

    for (int i = 0; i < n; i++)
      sort(Q[i], Q[i] + p);

    ids = vector<int>(n, 0);
    int ans = 0;
    while (true) {
      double lower = 0, upper = 10000000;
      int min_id = -1;
      double min_val = 10000000;
      // cout << endl;
      for (int i = 0; i < n; i++) {
        auto range = calc(Q[i][ids[i]], R[i]);

        if (range.first < min_val) {
          min_val = range.first;
          min_id = i;
        }

        // cout << "range is " << range.first << ", " << range.second << endl;
        // cout << "q " << Q[i][ids[i]] << endl;
        // cout << "for r " << R[i] << endl;

        lower = max(lower, range.first);
        upper = min(upper, range.second);
      }

      int Lower = ceil(lower) + .1;
      int Upper = floor(upper + 1e-9) + .1;

      bool is_good = true;

      // if (Lower > 1 && good(Lower - 1)) Lower--;
      // if (!good(Lower) && good(Lower + 1)) Lower++;

      // if (good(Upper + 1)) Upper++;
      // if (Upper > 1 && !good(Upper) && good(Upper - 1)) Upper--;

      // if (Lower > 0 && !good(Lower)) is_good = false;
      // if (Upper > 0 && !good(Upper)) is_good = false;

      // if (test == 34) {
      //   cout << "lower " << lower << " upper " << upper << endl;
      //   cout << "Lower " << Lower << " Upper " << Upper << endl;
      // }

      if (Lower <= Upper && Lower > 0 && is_good) {
        ans++;
        bool done = false;
        for (int i = 0; i < n; i++) {
          // cout << "ids " << i << " is " << ids[i] << endl;
          // cout << "i " << i << " q " << Q[i][ids[i]] << endl;
          ids[i]++;
          if (ids[i] == p)
            done = true;
        }
        if (done) break;
      } else {
        ids[min_id]++;
        if (ids[min_id] == p)
          break;
      }
    }

    cout << "Case #" << ++test << ": " << ans << endl;
  }
}
