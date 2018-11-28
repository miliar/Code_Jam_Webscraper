#include<cstdio>
#include<cstring>
#include<algorithm>
#include<cstdlib>
using namespace std;
int calc=0;
const int maxn=1010;
int n,c,m,ans,t;
int a[maxn],cap[maxn];
int ne[maxn];
int ts[maxn];
bool judge (int s)
{
  calc=0;int lastx=c;
  memset(cap,0,sizeof(cap));
  memset(ne,0,sizeof(ne));
  for (int i=m;i>=1;i--)
  {
    int x=min(a[i],lastx);
    if (cap[a[i]]<s) {cap[a[i]]++;continue;}
    while (x>0&&cap[x]>=s)
    {
      x--;
    }
    cap[x]++;ne[x]++;
    if (ne[a[i]]>0) ne[a[i]]--;else calc++;
    if(x==0) return false;
    lastx=x;
  }
  return true;
}
int main()
{
  freopen("bl.in","r",stdin);
    freopen("bs.out","w",stdout);
  scanf("%d",&t);
  for (int o=1;o<=t;o++)
  {
    memset(ts,0,sizeof(ts));
    ans=0;
    scanf("%d%d%d",&n,&c,&m);
    for (int i=1;i<=m;i++)
    {
      int y;
      scanf("%d%d",&a[i],&y);
      ts[y]++;
    }
    for (int i=1;i<=n;i++) ans=max(ans,ts[i]);
    sort(a+1,a+m+1);
    int left=ans,right=m;
    while (left<right)
    {
      int mid=(left+right)>>1;
      if (judge(mid)) right=mid;
      else left=mid+1;
    }
    judge(left);
    printf("Case #%d: %d %d\n",o,left,calc);
  }
}
