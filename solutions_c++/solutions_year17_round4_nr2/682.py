#include <cstdio>
#include <cstring>
#include <string>
#include <cmath>
#include <cstdlib>
#include <map>
#include <set>
#include <queue>
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
  int tt;
  scanf("%d", &tt);
  for (int tc=1; tc<=tt; tc++)
  {
    int n,m,c;
    scanf("%d %d %d",&n,&m,&c);
    int cnt[1001]={0}, cntgrid[1001] = {0};
    for (int i=0; i<c; i++)
    {
      int x,y;
      scanf("%d %d",&x,&y);
      cnt[y]++;
      cntgrid[x]++;
    }
    int ans=0;
    for (int i=1; i<=1000;i++)
    {
      if (cnt[i] > ans)
        ans = cnt[i];
    }
    int cursum =0 ;
    for (int i=1;i<=1000;i++)
    {
      cursum += cntgrid[i];
      if ((cursum + (i-1)) / i > ans)
        ans = (cursum + (i-1)) / i ;
    }
    int ans2=0;
    for (int i=1; i<=1000;i++)
      if (cntgrid[i] > ans)
        ans2 += cntgrid[i] - ans;
    printf("Case #%d: %d %d\n", tc, ans, ans2);

  }
  return 0;
}