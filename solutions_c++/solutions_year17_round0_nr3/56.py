#include <iostream>
#include <vector>
#include <algorithm>
#include <map>
#include <set>
#include <queue>
#include <cstdio>

using namespace std;

int main() {
  int T; cin >> T;
  for (int t = 1; t <= T; t++) {
    long long N, K;
    cin >> N >> K;

    long long B = N;
    long long C0 = 1;
    long long C1 = 0;

    cout << "Case #" << t << ": ";
    for (;;) {
      long long NB = (B - 1) / 2;
      if (K <= C1) {
        cout << ((B + 1) / 2) << ' ' << B / 2 << endl;
        break;
      } else if (K <= C0 + C1) {
        cout << B / 2 << ' ' << (B - 1) / 2 << endl;
        break;
      }
      K -= C0 + C1;

      long long NC0, NC1;
      if (B % 2 == 0) {
        NC0 = C0;
        NC1 = C0 + 2 * C1;
      } else {
        NC0 = 2 * C0 + C1;
        NC1 = C1;
      }
      B = NB;
      C0 = NC0;
      C1 = NC1;
    }
  }
  return 0;
}
