#include <bits/stdc++.h>
using namespace std;

int T, K, N;
char S[1005];

int solve() {
  int ans = 0;
  for (int i = 0; i <= N-K; ++i) {
    if (S[i] == '-') {
      ++ans;
      for (int j = 0; j < K; ++j) {
	S[i + j] = (S[i + j] == '+' ? '-' : '+');
      }
    }
  }
  for (int i = N-K+1; i < N; ++i) {
    if (S[i] == '-') return -1;
  }
  return ans;
}

int main() {
  scanf("%d",&T);
  for (int i = 1; i <= T; ++i) {
    scanf("%s%d",S,&K);
    N = strlen(S);
    int ans = solve();
    if (ans != -1) {
      printf("Case #%d: %d\n", i, ans);
    } else {
      printf("Case #%d: IMPOSSIBLE\n", i);
    }
  }
  return 0;
}
