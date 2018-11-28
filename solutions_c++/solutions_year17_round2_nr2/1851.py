#include <bits/stdc++.h>

int t, i, j, n, c[6], o[6], k;
char s[6004], tr[] = "ROYGBV";

void Do (int x)
{
  s[j++] = tr[x];
  c[x]--;
  int dual = x == 0 ? 3 : x == 2 ? 5 : 1;
  while (c[dual] > 0) {
    s[j++] = tr[dual];
    c[dual]--;
    s[j++] = tr[x];
    c[x]--;
  }
}

int main ()
{
  scanf ("%d\n", &t);
  for (i = 1; i <= t; i++) {
    scanf ("%d%d%d%d%d%d%d", &n, &c[0], &c[1], &c[2], &c[3], &c[4], &c[5]);
    j = 0;
    k = 0;
    while (c[0] > 0) {
      Do (0);
      if (c[2] - c[5] > c[4] - c[1]) k = 2;
      else k = 4;
      if (c[k] > 0) Do (k);
      else break;
    }
    if (k != 2 || c[4]) {
        if (k == 2) Do (4);
        while (c[2] > 0) {
          Do (2);
          if (c[4] > 0) Do (4);
          else break;
        }
    }
    //s[j] = 0;
    //printf ("%d %s\n", j, s);
    if (j == n + 1 && s[n] == s[0]) j--;
    s[j] = 0;
    printf ("Case #%d: %s\n", i, j == n && s[n-1] != s[0] ? s : "IMPOSSIBLE");
  }
  return 0;
}
