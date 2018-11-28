#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <utility>
using namespace std;

int T, N, P, g, countr[4], ans, used, total;

int main() {
  ifstream fin("A-large.in");
  ofstream fout("A-large.out");
  fin >> T;
  for (int t = 1 ; t <= T ; t++) {
    fin >> N >> P;
    for (int i = 0 ; i < P ; i++) {
      countr[i] = 0;
    }
    for (int i = 0 ; i < N ; i++) {
      fin >> g;
      countr[g % P]++;
    }
    ans = countr[0];
    if (P == 2) {
      ans += countr[1] / 2;
      if (countr[1] % 2 != 0) ans++;
    } else if (P == 3) {
      if (countr[1] <= countr[2]) {
        countr[2] -= countr[1];
        ans += countr[1] + (countr[2] / 3);
        if (countr[2] % 3 != 0) ans++;
      } else {
        countr[1] -= countr[2];
        ans += countr[2] + (countr[1] / 3);
        if (countr[1] % 3 != 0) ans++;
      }
    } else if (P == 4) {
      ans += countr[2] / 2;
      countr[2] = countr[2] % 2;
      if (countr[1] <= countr[3]) {
        countr[3] -= countr[1];
        if (countr[2] > 0 && countr[3] >= 2) {
          ans += 1;
          countr[2]--;
          countr[3] -= 2;
        }
        ans += countr[1] + (countr[3] / 4);
        if (countr[3] % 4 != 0 || countr[2] > 0) ans++;
      } else {
        countr[1] -= countr[3];
        if (countr[2] > 0 && countr[1] >= 2) {
          ans += 1;
          countr[2]--;
          countr[1] -= 2;
        }
        ans += countr[3] + (countr[1] / 4);
        if (countr[1] % 4 != 0 || countr[2] > 0) ans++;
      }
    }
    fout << "Case #" << t << ": " << ans << endl;
  }
  return 0;
}