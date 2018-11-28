#include <cstdio>
void tidy(char *str) {
  if (str[1] == '\0') return;
  for (int i = 1; str[i] != '\0'; ++i)
    if (str[i] < str[i - 1]) {
      str[i - 1]--;
      while (str[i])
        str[i++] = '9';
      tidy(str);
    }
}
int main() {
  int t;
  scanf("%d", &t);
  for (int c = 1; c <= t; ++c) {
    char str[25];
    scanf("%s", str);
    tidy(str);
    char *s = str;
    while (*s == '0') ++s;
    printf("Case #%d: %s\n", c, s);
  }
  return 0;
}
