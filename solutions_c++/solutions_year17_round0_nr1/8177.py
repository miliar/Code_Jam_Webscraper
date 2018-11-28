#include <stdio.h>
#include <string.h>

int main() {
  int tests;
  scanf("%d", &tests);
  for (int test = 0; test < tests; test++) {
    char s[1024];
    scanf("%s", s);
    int k;
    scanf("%d", &k);
    int n = strlen(s);
    int moves = 0;
    for (int i = 0; i+k <= n; i++) {
      if (s[i] == '-') {
        for (int j = i; j < i+k; j++) {
          s[j] = s[j] == '+' ? '-' : '+';
        }
        moves++;
      }
    }
    int ok = 1;
    for (int i = 0; i < n; i++) {
      if (s[i] == '-') {
        ok = 0;
        break;
      }
    }

    printf("Case #%d: ", test+1);

    if (!ok) {
      printf("IMPOSSIBLE\n");
      continue;
    }

    printf("%d\n", moves);
  }
}
