#include<cstdio>
using namespace std;

const int maxN = 25 + 7;
int T, r, c;
char mtx[maxN][maxN];

void solve() {
  int st = 0;
  for (int i = 0; i < r; i ++) {
    char x = '?';
    for (int j = 0; j < c; j ++)
      if (mtx[i][j] != '?') {
        if (x == '?') for (int k = 0; k < j; k ++) mtx[i][k] = mtx[i][j];
        x = mtx[i][j];
      } else mtx[i][j] = x;
    if (x == '?') {
      if (i == st) {
        st = i + 1;
      } else {
        for (int j = 0; j < c; j ++) mtx[i][j] = mtx[i - 1][j];
      }
    }
  }
  for (int i = st - 1; i >= 0; i --)
    for (int j = 0; j < c; j ++) mtx[i][j] = mtx[i + 1][j];
}

int main() {
  scanf("%d", &T);
  for (int cou = 1; cou <= T; cou ++) {
    scanf("%d%d", &r, &c);
    for (int i = 0; i < r; i ++) scanf("%s", mtx[i]);
    solve();
    printf("Case #%d:\n", cou);
    for (int i = 0; i < r; i ++) printf("%s\n", mtx[i]);
  }
}
