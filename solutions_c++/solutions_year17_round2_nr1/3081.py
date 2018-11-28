#include <stdio.h>

int t, n;
int d;
int k;
float s;
float max;

int main()
{
  scanf("%d", &t);
  for (int i=0; i<t; i++)
  {
    max = -1;
    getchar();
    scanf("%d %d", &d, &n);
    for (int j=0; j<n; j++)
    {
      getchar();
      scanf("%d %f", &k, &s);
      float tm = (d - k) / s;
      if (max == -1 || max < tm)
        max = tm;
    }
    printf("Case #%d: %f\n", i+1, d/max);
  }
  return 0;
}