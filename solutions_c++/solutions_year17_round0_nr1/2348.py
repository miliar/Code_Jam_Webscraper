#include <bits/stdc++.h>
using namespace std;

int main ()
{
  int t, i, k, j;
  char s[1004];
  scanf ("%d", &t);
  for (i = 1; i <= t; i++) {
    scanf ("%s%d", s, &k);
    int r = 0, l;
    for (j = 0; s[j] != 0; j++) {
      if (s[j] == '-') {
        for (l = 0; l < k && s[j + l] != '\0'; l++) s[j + l] ^= '+' ^ '-';
        if (l < k) break;
        r++;
      }
    }
    fprintf (stderr, "%s\n", s);
    printf (s[j] != '\0' ? "Case #%d: IMPOSSIBLE\n" : "Case #%d: %d\n", i, r);
  }
  return 0;
}
