#include <cstdio>
#include <cstring>
void inv(char *c) {
  if (*c == '+') *c = '-';
  else *c = '+';
}
int k;
int opt(char *str) {
  int kk = k - 1;
  for (int i = kk; str[i] != '\0'; ++i)
    if (str[i - kk] == '+') continue;
    else {
      for (int j = 0; j < k; ++j)
        inv(str + i - j);
      return 1 + opt(str);
    }
  return 0;
}
int main() {
  int t;
  scanf("%d", &t);
  int caso = 0;
  while (t--) {
    char str[1001];
    scanf("%s %d", str, &k);
    int flip = opt(str);
    int imp = 0;
    for (int i = 0; str[i]; ++i)
      if (str[i] == '-') imp = 1;
    printf("CASE #%d: ", ++caso);
    if (imp) printf("IMPOSSIBLE\n");
    else printf("%d\n", flip);
  }
  return 0;
}
