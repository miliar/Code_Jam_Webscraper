#include <sstream>
#include <cassert>
#include <iomanip>
#include <vector>
#include <algorithm>
#include <cmath>
#include <cstring>
#include <queue>
#include <list>
#include <iostream>
#include <cstdio>
#include <cstdlib>

using namespace std;

typedef long long tint;
typedef unsigned int uint;
const int MAXN = 1073741824;
const int MAX_INT = 2147483647;

int main() {
  int T;
  cin >> T;
  for (int tt = 1; tt <= T; tt++) {
    tint n, k;
    cin >> n >> k;

    vector<bool> v(n+2, false);
    v[0] = v[n+1] = true;
    vector<int> countl(n+2, 0), countr(n+2, 0);

    tint maxlr = 0, minlr = n;
    for (int i = 0; i < k; i++) {
      for (int i = 1; i <= n; i++) {
        if (v[i]) {
          countl[i] = 0;
          continue;
        }
        if (v[i-1]) countl[i] = 0;
        else countl[i] = countl[i-1] + 1;
      }
      for (int i = n; i > 0; i--) {
        if (v[i]) {
          countr[i] = 0;
          continue;
        }
        if (v[i+1]) countr[i] = 0;
        else countr[i] = countr[i+1] + 1;
      }


      // for (int i = 1; i <= n; i++) {
      //   cerr << countl[i] << "/" << countr[i];
      //   if (v[i]) cerr << "*";
      //   cerr << " ";
      // }
      // cerr << endl;

      maxlr = -1;
      minlr = -1;
      int pos = -1;
      for (int j = 1; j <= n; j++) {
        if (v[j]) continue;
        // if (pos == -1) pos = j;
        // cerr << "pos=" << j << " l=" << countl[j] << " r=" << countr[j] << " ";
        if (minlr < min(countl[j], countr[j])) {
          pos = j;
          minlr = min(countl[j], countr[j]);
          maxlr = max(countl[j], countr[j]);
        } else if (minlr == min(countl[j], countr[j])) {
          if (maxlr < max(countl[j], countr[j])) {
            minlr = min(countl[j], countr[j]);
            maxlr = max(countl[j], countr[j]);
            pos = j;
          }
        }
        // cerr << "minlr="<< minlr << " maxlr=" << maxlr << endl;
      }
      assert(1 <= pos && pos <= n);
      // cerr << i+1 << " => " << pos << " " << maxlr << "/" << minlr << endl;
      v[pos] = true;
    }

    cout << "Case #" << tt << ": ";
    cout << maxlr << " " << minlr << endl;

  }

  return 0;
}
