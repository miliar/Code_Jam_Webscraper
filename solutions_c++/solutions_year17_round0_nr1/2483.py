#include <bits/stdc++.h>
using namespace std;

int main() {
  freopen("A-large.in", "r", stdin);
  freopen("A-large.out", "w+", stdout);
  int T, n, K, f;
  char S[1003];
  scanf("%d", &T);
  for (int t = 1; t <= T; t++) {
    scanf("%s %d", S, &K);
    n = strlen(S);
    f = 0;
    for (int i = 0; i <= n-K; i++) {
      if (S[i] == '-') {
        f++;
        for (int j = 0; j < K; j++) {
          if (S[i+j] == '+') S[i+j] = '-';
          else S[i+j] = '+';
        }
      }
    }
    for (int i = n-K+1; i < n; i++) {
      if (S[i] == '-') {
        f = -1;
        break;
      }
    }
    if (f < 0) {
      printf("Case #%d: IMPOSSIBLE\n", t);
    } else {
      printf("Case #%d: %d\n", t, f);
    }
  }
  return 0;
}

