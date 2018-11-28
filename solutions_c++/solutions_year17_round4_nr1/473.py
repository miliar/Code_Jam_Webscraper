#include <bits/stdc++.h>

using namespace std;

int Test;
int N, P, C[4];

int main() {
   freopen("A-large.in", "r", stdin);
   freopen("A-large.out", "w", stdout);
  scanf("%d", &Test);
  for (int test = 1; test <= Test; ++test) {
    scanf("%d%d", &N, &P);
    memset(C, 0x00, sizeof(C));
    for (int i = 0, A; i < N; ++i) {
      scanf("%d", &A);
      C[A % P]++;
    }
    int ans = 0;
    if (P == 2) {
      ans = C[0] + (C[1] + 1) / 2;
    } else if (P == 3) {
      ans = C[0];
      if (C[1] == C[2]) {
        ans += C[1];
      } else if (C[1] > C[2]) {
        ans += C[2] + (C[1] - C[2] + 2) / 3;
      } else {
        ans += C[1] + (C[2] - C[1] + 2) / 3;
      }
    } else {
      ans = C[0];
      int d = min(C[1], C[3]);
      C[1] -= d;
      C[3] -= d;
      ans += d;
      d = (C[1] + C[3]) / 2 + C[2];
      ans += d / 2;
      if (((C[1] + C[3]) & 1) || (d & 1)) {
        ++ans;
      }
    }
    printf("Case #%d: %d\n", test, ans);
  }
  return 0;
}
