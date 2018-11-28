#include <cstdio>
#include <cstring>
int main()
{
  int T;scanf("%d",&T);
  for (int t=0;t<T;++t)
  {
    char stx[1005];
    int p;
    scanf("%s %d",stx,&p);
    int n = strlen(stx);
    int cnt = 0;
    for (int q=0;q+p<=n;++q)
    {
      if (stx[q]=='-')
      {
        cnt++;
        for (int w=q;w<q+p;++w)
          stx[w] = '+'+'-'-stx[w];
      }
    }
    bool good = true;
    for (int q=0;q<n;++q)
      if (stx[q]=='-')
        good = false;
    if (good)
      printf("Case #%d: %d\n", t+1, cnt);
    else 
      printf("Case #%d: IMPOSSIBLE\n", t+1);
  }
  return 0;
}