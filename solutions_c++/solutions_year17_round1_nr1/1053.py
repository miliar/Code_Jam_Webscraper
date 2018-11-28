#include <iostream>
#include <fstream>
#include <cmath>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <stack>
#include <queue>
#include <cstdlib>
#include <cstdio>
#include <string>
#include <cstring>
#include <cassert>
#include <utility>
#include <iomanip>

using namespace std;

const int MAXN = 105;

int tn;
int n, m;
char c[MAXN][MAXN];

bool emp(char &c) {
  return c == '?';
}

void copyLine(int i, int ii) {
  for (int j = 1; j <= m; j++) {
    c[ii][j] = c[i][j];
  }
}

int main() {
  //assert(freopen("input.txt","r",stdin));
  //assert(freopen("output.txt","w",stdout));

  scanf("%d", &tn);

  for (int test = 1; test <= tn; test++) {
    scanf("%d %d\n", &n, &m);
    for (int i = 1; i <= n; i++) {
      for (int j = 1; j <= m; j++) {
        scanf("%c", &c[i][j]);
      }
      scanf("\n");
    }

    int p = -1;

    for (int i = 1; i <= n; i++) {
      bool f = true;
      for (int j = 1; j <= m; j++) {
        if (!emp(c[i][j])) {
          f = false;
        }
      }
      if (f) {
        if (p == -1) {
          continue;
        }
        copyLine(p, i);
        continue;
      }

      for (int j = 1; j <= m; j++) {
        if (emp(c[i][j]))
          continue;
        int l = j - 1, r = j + 1;
        while (l >= 1 && emp(c[i][l])) {
          c[i][l] = c[i][j];
          l--;
        }
        while (r <= m && emp(c[i][r])) {
          c[i][r] = c[i][j];
          r++;
        }
      }

      if (p == -1) {
        int ii = i - 1;
        while (ii >= 1) {
          copyLine(i, ii);
          ii--;
        }
      }
      p = i;
    }

    printf("Case #%d:\n", test);
    for (int i = 1; i <= n; i++) {
      for (int j = 1; j <= m; j++) {
        printf("%c", c[i][j]);
      }
      printf("\n");
    }

  }

  return 0;
}