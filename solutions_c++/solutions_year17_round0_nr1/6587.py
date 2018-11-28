#include<stdio.h>
#include<stdlib.h>
#include<string.h>

int main() {
  int t;
  int k;
  char s[1010];

  scanf("%d", &t);
  for (int o = 0; o < t; o++) {
    scanf("%s %d", s, &k);
    int l = strlen(s);
    int c = 0;
    for (int i = 0; i <= l - k; i++) {
      if (s[i] == '-') {
        for (int j = i; j < i + k; j++) {
          if (s[j] == '-') {
            s[j] = '+';
          } else {
            s[j] = '-';
          }
        }
        c++;
      }
    }
    for (int i = 0; i < l; i++) {
      if (s[i] == '-') {
        c = -1;
      }
    }
    if (c == -1) {
      printf("Case #%d: IMPOSSIBLE\n", o + 1);
    } else {
      printf("Case #%d: %d\n", o + 1, c);
    }
  }

  return 0;
}
