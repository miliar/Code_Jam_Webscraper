#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <algorithm>
#include <cmath>
#define ll long long
using namespace std;

int main() {
  int tk;
  cin >> tk;
  for (int tk1 = 1; tk1 <= tk; tk1++) {
    int n, p;
    cin >> n >> p;
    vector<int> need(n);
    for (int i = 0; i < n; i++) {
      cin >> need[i];
    }
    vector<vector<int> > a(n, vector<int>(p));
    vector<vector<bool> > used(n, vector<bool>(p));
    for (int i = 0; i < n; i++) {
      for (int j = 0; j < p; j++) {
        cin >> a[i][j];
      }
      sort(a[i].begin(), a[i].end());
    }
    int res = 0;
    for (int i = 0; i < p; i++) {
      int low = ceil((double)(a[0][i] * 10) / (need[0] * 11));
      int high = floor((double)(a[0][i] * 10) / (need[0] * 9));
      // cout << "low, high = " << low << ", " << high << endl;
      vector<int> indices(n);
      for (int num = low; num <= high; num++) {
        bool succ = true;
        for (int j = 1; j < n; j++) {
          int lo = ceil((double)need[j] * num * 9 / 10);
          int hi = floor((double)need[j] * num * 11 / 10);
          int idx = lower_bound(a[j].begin(), a[j].end(), lo) - a[j].begin();
          // cout << "j, lo, hi, idx = " << j << ", " << lo << ", " << hi << ", " << idx << endl;
          while (idx < p && used[j][idx]) {
            idx++;
          }
          if (idx == p || a[j][idx] > hi) {
            succ = false;
            break;
          } else {
            indices[j] = idx;
          }
        }
        if (succ) {
          res++;
          for (int j = 1; j < n; j++) {
            used[j][indices[j]] = true;
          }
          break;
        }
      }
    }

    cout << "Case #" << tk1 << ": " << res << endl;
  }
  return 0;
}
