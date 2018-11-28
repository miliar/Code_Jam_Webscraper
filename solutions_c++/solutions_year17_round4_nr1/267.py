#include<cstdio>
#include<cstdlib>
#include<algorithm>
using namespace std;
int a[10];
int main()
{
  freopen("as.in","r",stdin);
  freopen("as.out","w",stdout);
  int t,n,x,p,ans=0;
  scanf("%d",&t);
  for (int o=1;o<=t;o++)
  {
    scanf("%d%d",&n,&p);
    memset(a,0,sizeof(a));
    for (int i=1;i<=n;i++)
    {
      scanf("%d",&x);
      a[x%p]++;
    }
    ans=a[0];
    ans++;
    if (p==3)
    {
      if (a[2]>a[1]) ans+=a[1],a[2]-=a[1],a[1]=0;
      if (a[1]>=a[2]) ans+=a[2],a[1]-=a[2],a[2]=0;
      ans+=a[1]/3+a[2]/3;a[1]%=3;a[2]%=3;
      if (a[1]==0&&a[2]==0) ans--;
    }
    else
    {ans+=a[1]/2;
      if (a[1]%2==0) ans--;
    }
    printf("Case #%d: %d\n",o,ans);
  }
}
