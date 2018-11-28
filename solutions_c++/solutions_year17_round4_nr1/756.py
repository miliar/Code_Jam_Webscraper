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
    int n,p;
    scanf("%d %d",&n,&p);
    int arr[100];
    int cnt[4] = {0};
    for (int i=0; i<n; i++)
    {
      scanf("%d",&arr[i]);
      arr[i] %= p;
      cnt[arr[i] ] ++;
    }
    int ans=0;
    ans += cnt[0];
    if (p==2)
    {
      ans += (cnt[1]+1)/2;
    }
    else if (p==3)
    {
      int tmp = min(cnt[1], cnt[2]);
      ans += tmp;
      cnt[1] -= tmp;
      cnt[2] -= tmp;
      ans += (max(cnt[1],cnt[2]) + 2 )/ 3;
    }
    else if (p==4)
    {
      int tmp = min(cnt[1], cnt[3]);
      ans += tmp;
      cnt[1] -= tmp;
      cnt[3] -= tmp;
      int a=cnt[2], b=max(cnt[1],cnt[3]);
      if (a==0)
        ans += (b+3) / 4;
      else if (b==0)
        ans += (a+1) / 2;
      else
      {
        ans += b / 4;
        b -= b/4*4;
        ans += a / 2;
        a -= a/2*2;
        if (a>=1 && b>=2)
          {ans++; a--; b--; b--;}
        if (b>0)
          ans++;
      }
    }
    printf("Case #%d: %d\n", tc, ans);

  }
  return 0;
}