#include <cassert>

#include <stdio.h>

int main() {
  int T;
  scanf ("%d", &T);

  for (int t = 1; t <= T; t++)
  {
    static char S[1001];
    int K;

    scanf ("%s %d", S, &K);

    int d = 0;

    for (int i = 0; d != -1 && S[i] != '\0'; i++)
    {
      if (S[i] == '-')
      {
        d++;

        for (int j = i; j < i + K; j++)
        {
          if (S[j] == '\0')
          {
            d = -1;
            break;
          }
          else if (S[j] == '-')
          {
            S[j] = '+';
          }
          else
          {
            S[j] = '-';
          }
        }
      }
    }

    if (d >= 0)
    {
      printf ("Case #%d: %d\n", t, d);
    }
    else
    {
      printf ("Case #%d: IMPOSSIBLE\n", t);
    }
  }

  return 0;
}
