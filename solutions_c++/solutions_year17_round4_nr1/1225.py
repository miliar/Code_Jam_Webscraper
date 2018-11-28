#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <algorithm>

using namespace std;

int N;
int G[110];
int P;
int pd[101][101][101][4];
int cnt[4];

void read() {
  scanf("%d%d", &N, &P);
  for (int i = 0; i < N; i++) {
    scanf("%d", &G[i]);
  }
}

int go(int r1, int r2, int r3, int mod) {
  if (pd[r1][r2][r3][mod] != -1) {
    return pd[r1][r2][r3][mod];
  }
  pd[r1][r2][r3][mod] = 0;

  if (r1 > 0) {
    pd[r1][r2][r3][mod] = max(pd[r1][r2][r3][mod], (mod == 0) + go(r1-1, r2, r3, mod == 0 ? P-1 : mod-1));
  }
  if (r2 > 0) {
    int pp = mod;
    int cc = 2;
    while (cc > 0) {
      if (pp == 0) pp = P;
      int s = min(pp, cc);
      cc -= s;
      pp -= s;
    }
    pd[r1][r2][r3][mod] = max(pd[r1][r2][r3][mod], (mod == 0) + go(r1, r2-1, r3, pp));
  }
  if (r3 > 0) {
    int pp = mod;
    int cc = 3;
    while (cc > 0) {
      if (pp == 0) pp = P;
      int s = min(pp, cc);
      cc -= s;
      pp -= s;
    }
    pd[r1][r2][r3][mod] = max(pd[r1][r2][r3][mod], (mod == 0) + go(r1, r2, r3-1, pp));
  }

  return pd[r1][r2][r3][mod];
}

void process() {
  for (int i = 0; i < 4; i++) {
    cnt[i] = 0;
  }
  for (int i = 0; i < N; i++) {
    cnt[G[i]%P]++;
  }
  memset(pd, -1, sizeof(pd));
  printf("%d\n", go(cnt[1], cnt[2], cnt[3], 0) + cnt[0]);
}

int main() {

  int cases;

  scanf("%d", &cases);

  for (int i = 1; i <= cases; i++) {
    printf("Case #%d: ", i);
    read();
    process();
  }

  return 0;
}
