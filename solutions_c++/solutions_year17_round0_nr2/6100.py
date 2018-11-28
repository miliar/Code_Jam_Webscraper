#include <cstdio>

typedef long long ll;

int main(void) {
  int TT;
  scanf("%d", &TT);
  for (int T = 1; T <= TT; ++T) {
    char str[24];
    scanf("%s", str);

    for (;;) {
      char *p = str;
      for (++p; *p; ++p)
        if (*p < *(p - 1))
          break;
      if (!*p) break;

      --*(p - 1);
      for (; *p; ++p)
        *p = '9';
    }

    ll x;
    sscanf(str, "%lld", &x);
    printf("Case #%d: %lld\n", T, x);
  }
  return 0;
}
