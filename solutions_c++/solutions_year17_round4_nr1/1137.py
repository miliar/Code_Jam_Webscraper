#include <iostream>
#include <vector>
#include <cassert>
#include <algorithm>
#include <iomanip>
#include <map>

using namespace std;


int main() {
  int T;
  cin >> T;
  for (int t = 0; t < T; t++) {
    int N, P;
    cin >> N >> P;

    map<int, int> ds;
    for (int i = 0; i < N; i++) {
      int g;
      cin >> g;
      ds[g % P] += 1;
    }

    int z = 0;
    if (P == 2) {
      z += ds[0] + (ds[1] + 1) / 2;
    } else if (P == 3) {
      z += ds[0];
      ds[0] = 0;

      // 1 + 2 = 0
      int w = min(ds[1], ds[2]);
      z += w;
      ds[1] -= w;
      ds[2] -= w;

      // 3 * x = 0
      z += (ds[1] + 2) / 3;
      z += (ds[2] + 2) / 3;
    } else if (P == 4) {
      z += ds[0];
      ds[0] = 0;

      // 1 + 3 = 0
      int w = min(ds[1], ds[3]);
      z += w;
      ds[1] -= w;
      ds[3] -= w;

      // 2 + 2 = 0
      int w2 = ds[2] / 2;
      z += w2;
      ds[2] -= 2 * w2;

      // 2 * odd + 2 = 0
      int odd = ds[1] ? 1 : 3;
      int w3 = min(ds[odd] / 2, ds[2]);
      z += w3;
      ds[odd] -= 2 * w3;
      ds[2] -= w3;

      // 4 * x = 0
      int w4 = ds[odd] / 4;
      z += w4;
      ds[odd] -= 4 * w4;


      // remainder
      if (ds[0] + ds[1] + ds[2] + ds[3]) {
        z += 1;
      }
    }


    cout << "Case #" << (t + 1) << ": " << z << endl;
  }

  return 0;
}
