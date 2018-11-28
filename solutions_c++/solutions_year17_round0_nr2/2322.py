#include <bits/stdc++.h>
using namespace std;

int main ()
{
  int t, i, j, k, cnt;
  char s[30], last[30];
#if 1
  scanf ("%d", &t);
  for (i = 1; i <= t; i++) {
    scanf ("%s", s);
#else
  int64_t v = 123456789012345678LL;
  for (v = 1; ; v++) {
    sprintf (s, "%lld", v);
    for (j = 0; s[j+1] && s[j] <= s[j+1]; j++) {}
    if (!s[j+1]) memcpy (last, s, 30);
#endif
    for (cnt = 0;;cnt++) {
      for (j = 0; s[j+1] != '\0' && s[j] <= s[j+1]; j++) {}
      if (s[j+1] == '\0') break;
      for (k = j + 1; s[k] != '\0'; k++) s[k] = '9';
      while (--s[j] == '0' && j > 0) {
        s[j] = '9';
        j--;
      }
    }
    printf ("Case #%d: %s\n", i, s[0] == '0' ? s + 1 : s);
    /*
    if (cnt > 19) printf ("X %lld %s\n", v, s);
    if (!((v-1) & v)) printf ("%lld\n", v);
    if (strcmp (s[0] == '0' ? s + 1 : s, last) != 0) printf ("%lld %s\n", v, s);
    */
  }
  return 0;
}
