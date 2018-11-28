#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <set>
#include <map>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <queue>
#include <deque>
#include <cstring>

using namespace std;

int d[2][1500][1500][2];
int acs[2][200][2];
size_t al[2];

int solve() {
  cin >> al[0] >> al[1];
  for (int k=0;k<2;++k)
    for (int i=0;i<al[k];++i)
      cin >> acs[k][i][0] >> acs[k][i][1];
  for (int p=0;p<2;++p) {
    d[p][0][0][1-p] = 1000000000;
    for (int i = 1; i <= 1440; ++i) {
      for (int k = 0; k < 2; ++k) {
        bool good = true;
        for (int z = 0; z < al[k]; ++z) {
          good = good && (acs[k][z][0] > i || acs[k][z][1] <= i);
        }
        for (int j = 0; j <= i; ++j) {
          int &rs = d[p][i][j][k];
          rs = 1000000000;
          if (!good)
            continue;
          if (j > 0)
            rs = min(rs, d[p][i - 1][j - 1][k]);
          if (j > 0 && i != j)
            rs = min(rs, d[p][i - 1][i - j][1 - k] + 1);
        }
      }
    }
  }
  int rs1 = min(d[0][1440][720][0], d[1][1440][720][1]);
  int rs2 = min(d[0][1440][720][1], d[1][1440][720][0]) + 1;
  return min(rs1, rs2);
}

int main() {
#ifdef LOCAL_RUN
  freopen("input.txt", "r", stdin);
#endif
  int t;
  cin >> t;
  for (int i=1;i<=t;++i) {
    cout << "Case #" << i << ": " << solve() << endl;
  }
  return 0;
}