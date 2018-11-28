#include <stdio.h>
#include <string.h>

int main() {
  char s[1111];
  int cn, tn, k, n;
  int flipped[1111];
  int tot_flipped;
  for (scanf("%d", &tn), cn = 1; cn <= tn; cn++) {
    tot_flipped = 0;
    scanf("%s%d", s, &k);
    n = strlen(s);
    memset(flipped, 0, sizeof(flipped));
    for (int i = 0; i < n - k + 1; i++) {
      if ((s[i] == '-' && flipped[i] % 2 == 0)
          || (s[i] == '+' && flipped[i] % 2 == 1)) {
          tot_flipped++;
          for (int j = i; j < i + k; j++) {
            flipped[j]++;
          }
      }
    }
    bool ok = true;
    for (int i = n - k + 1; i < n; i++) {
      if ((s[i] == '-' && flipped[i] % 2 == 0)
          || (s[i] == '+' && flipped[i] % 2 == 1)) {
        ok = false;
        break;
      }
    }
    printf("Case #%d: ", cn);
    ok ? printf("%d\n", tot_flipped) : printf("IMPOSSIBLE\n");
  }
  return 0;
}
