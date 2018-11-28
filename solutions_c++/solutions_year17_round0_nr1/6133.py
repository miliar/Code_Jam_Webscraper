#include <cstdio>
#include <cstdlib>
#include <cstring>

char str[1024];
char flip[1024];

int main(void) {
  int TT;
  scanf("%d", &TT);
  for (int T = 1; T <= TT; ++T) {
    int K;
    scanf("%s%d", str, &K);
    int N = strlen(str);
    memset(flip, 0, N);

    int sum = 0;
    int result = 0;
    bool ok = true;
    for (int i = 0; i < N; ++i) {
      // printf("i=%d %c sum=%d flip=%d\n", i, str[i], sum, flip[i]);
      sum ^= flip[i];
      int curr = sum ^ (str[i] == '-');
      if (curr) {
        if (i > N - K) {
          ok = false;
          break;
        }
        ++result;
        sum ^= 1;
        if (i + K < N)
          flip[i + K] ^= 1;
      }
    }
    if (ok)
      printf("Case #%d: %d\n", T, result);
    else
      printf("Case #%d: IMPOSSIBLE\n", T);
  }
  return 0;
}
