#include <cstring>
#include <cstdio>

int main() {
  int N;
  scanf("%d", &N);
  for (int i = 0; i < N; ++i) {
    char s[1001];
    int K;
    scanf("%1000s%d", s, &K);
    int len = strlen(s), out = 0;
    for (int j = 0; j <= len - K; ++j) {
      if (s[j] == '-') {
        ++out;
        for (int k = 0; k < K; ++k) {
          if (s[j + k] == '-') {
            s[j + k] = '+';
          } else {
            s[j + k] = '-';
          }
        }
      }
    }
    for (int j = 0; j < len; ++j) {
      if (s[j] != '+') {
        printf("Case #%d: IMPOSSIBLE\n", i + 1);
        goto nextcase;
      }
    }
    printf("Case #%d: %d\n", i + 1, out);
nextcase:
    ;
  }
}
