#include <stdio.h>
#include <string.h>

int main() {
  int tests;
  scanf("%d", &tests);
  for (int test = 0; test < tests; test++) {
    printf("Case #%d: ", test+1);
    char s[32];
    scanf("%s", s);
    int n = strlen(s);
    for (int i = n-1; i > 0; i--) {
      if (s[i] < s[i-1]) {
        s[i-1]--;
        for (int j = i; j < n; j++) {
          s[j] = '9';
        }
      }
    }

    char *p = s;
    while (*p == '0') {
      p++;
    }

    printf("%s\n", p);
  }
  return 0;
}
