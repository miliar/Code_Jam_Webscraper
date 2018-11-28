#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>

using namespace std;

const int MaxN = 1234;

char s[MaxN];
              
int main (void)
{
  int test, tests;
  scanf ("%d", &tests);
  for (test = 0; test < tests; test++)
  {
    int i, j, k, res = 0;
    scanf ("%s %d", s, &k);
    for (i = 0; s[i] != 0; i++)
      if (s[i] == '-')
      {
        res++;
        for (j = 0; j < k && s[i+j] != 0; j++)
          s[i+j] = '+' + '-' - s[i+j]; 
        if (j < k)
        {
          res = -1;
          break;
        }
      }
    if (res == -1)
      printf ("Case #%d: IMPOSSIBLE\n", test + 1);
    else
      printf ("Case #%d: %d\n", test + 1, res);
  }
  return 0;
}
