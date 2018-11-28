#include <stdio.h>
#include <string.h>

int main() {
  int T; scanf("%d", &T);
  char s[32];
  for (int t = 0; t < T; ++t) {
    scanf("%s", s);
    int l = strlen(s);
    for (int i = 0; i < l - 1; ++i) {
      if (s[i] > s[i + 1]) {
        for (int j = i + 1; j < l; ++j) {
          s[j] = '9';
        }
        s[i]--;
        for (int j = i; j >= 1; j--) {
          if (s[j] < s[j - 1]) {
            s[j] = '9';
            s[j - 1]--;
          }
        }
        break;
      }
    }
    int offset = (s[0] == '0');
    printf("Case #%d: %s\n", t + 1, s + offset);
  }
}
