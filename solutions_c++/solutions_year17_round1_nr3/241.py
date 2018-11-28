#ifdef DEBUG
//#define _GLIBCXX_DEBUG
#endif
#include <iostream>
#include <iomanip>
#include <fstream>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <deque>
#include <string>
#include <cstring>
#include <sstream>
#include <cmath>
#include <algorithm>
#include <ctime>
#include <cassert>
#include <functional>
#include <complex>

using namespace std;
typedef long double LD;
typedef long long LL;

const int kInf = 1e9;

int hd, ad, hk, ak, b, d;

int TryStrategy(int qd, int qb) {
  int chd = hd;
  int cad = ad;
  int chk = hk;
  int cak = ak;
  int ret = 0, heal = 0;
  while (chk > 0 && chd > 0) {
    if (heal * 100 > ret * 99) {
      return kInf;
    }
    if (cad >= chk) {
      return ret + 1;
    }
    ++ret;
    if ((chd <= cak && qd == 0) || (chd <= std::max(0, cak - d) && qd > 0)) {
      ++heal;
      chd = hd;
    } else if (qd) {
      --qd;
      cak -= d;
      cak = max(cak, 0);
    } else if (qb) {
      --qb;
      cad += b;
    } else if (cad == 0) {
      return kInf;
    } else {
      chk -= cad;
    }
    chd -= cak;
  }
  if (chk > 0) {
    return kInf;
  }
  return ret;
}

void Solve() {
  int ret = kInf;
  cin >> hd >> ad >> hk >> ak >> b >> d;
  for (int qb = 0; qb < 101; ++qb) {
    for (int qd = 0; qd < 101; ++qd) {
      ret = std::min(ret, TryStrategy(qd, qb));
    }
  }
  if (ret == kInf) {
    cout << "IMPOSSIBLE" << endl;
  } else {
    cout << ret << endl;
  }
}

int main() {
    freopen("c.in", "r", stdin);
    freopen("c.out", "w", stdout);
    int T;
    cin >> T;
    for (int i = 0; i < T; ++i) {
        printf("Case #%d: ", i + 1);
        Solve();
    }
    return 0;
}
