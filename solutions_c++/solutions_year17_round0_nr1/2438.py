#include <vector>
#include <string>
#include <iostream>
#include <algorithm>
#include <numeric>
#include <map>
#include <set>
#include <string.h>

typedef long long ll;
using namespace std;

int solve(char *S, int K) {
  int n = strlen(S);
  int r = 0;
  for (int i = 0; i < n-K+1; i++) {
    if (S[i] == '-') {
      r++;
      for (int j = i; j < i+K; j++) {
        S[j] = S[j] == '-' ? '+' : '-';
      }
    }
  }
  for (int i = n-K; i < n; i++) {
    if (S[i] != '+')
      return -1;
  }
  return r;
}

int main()
{
  int T;
  scanf("%d", &T);
  for (int i = 0; i < T; i++) {
    char S[1019] = {};
    int K;
    scanf("%s", S);
    scanf("%d", &K);
    int ans = solve(S, K);
    printf("Case #%d: ", i+1);
    if (ans < 0) {
      printf("IMPOSSIBLE\n");
    } else {
      printf("%d\n", ans);
    }
  }
}
