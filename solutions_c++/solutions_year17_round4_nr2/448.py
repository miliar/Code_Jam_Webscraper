#include <bits/stdc++.h>

using namespace std;

static const int MAX_NUM = 1 << 14;
int Test;
int N, C, M, P[MAX_NUM], B[MAX_NUM];
int PosC[MAX_NUM], PerC[MAX_NUM];

int main() {
   freopen("B-large.in", "r", stdin);
   freopen("B-large.out", "w", stdout);
  scanf("%d", &Test);
  for (int test = 1; test <= Test; ++test) {
    scanf("%d%d%d", &N, &C, &M);
    memset(PosC, 0x00, sizeof(PosC));
    memset(PerC, 0x00, sizeof(PerC));
    for (int i = 0; i < M; ++i) {
      scanf("%d%d", &P[i], &B[i]);
      --P[i];
      --B[i];
      PosC[P[i]]++;
      PerC[B[i]]++;
    }
    int cnt = *max_element(PerC, PerC + C);
    for (int i = 0; i < N; ++i) {
      if (i > 0) {
        PosC[i] += PosC[i - 1];
      }
      cnt = max(cnt, (PosC[i] + i) / (i + 1));
    }
    int change = 0;
    for (int i = 0; i < N; ++i) {
      int val = PosC[i];
      if (i > 0) {
        val -= PosC[i - 1];
      }
      if (val > cnt) {
        change += val - cnt;
      }
    }
    printf("Case #%d: %d %d\n", test, cnt, change);
  }
  return 0;
}
