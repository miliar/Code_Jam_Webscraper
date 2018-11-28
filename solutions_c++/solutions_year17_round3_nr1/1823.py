#include<bits/stdc++.h>
using namespace std;
#define N 1005
#define pii pair<int,int>
#define ff first
#define ss second
#define mp make_pair
#define pb push_back
#define ll long long 
#define mod 1000000007
#define barn cin.sync_with_stdio(0);cin.tie(0)
pair< double,double > re[N];
double r[N],h[N];
double ans[N][N];
vector< pii > v;
double max(double a,double b)
{
  return ((a>b)?a:b);
}
int main()
{
  //barn;
  //freopen("inputf.in","r",stdin);
  //freopen("outputf.in","w",stdout);
  int t,w;
  scanf("%d",&t);
  for(w=1;w<=t;w++)
  {
    int n,k,i,j,len,p,q;
    double val,maxi=0;
    scanf("%d%d",&n,&k);
    for(i=0;i<=n;i++)
      for(j=0;j<=n;j++)
        ans[i][j]=-1;
    for(i=1;i<=n;i++)
      scanf("%lf%lf",&re[i].ff,&re[i].ss);
    sort(re+1,re+n+1);
    for(i=1;i<=n;i++)
    {
      r[i]=re[i].ff;
      h[i]=re[i].ss;
    }
    val=2*r[1]*h[1]+r[1]*r[1];
    v.pb(mp(1,1));
    ans[1][1]=2*r[1]*h[1]+r[1]*r[1];
    for(i=2;i<=n;i++)
    { 
       len=v.size();
       for(j=0;j<len;j++)
       {
          p=v[j].ff;
          q=v[j].ss;
          val=ans[p][q]+(2*r[i]*h[i]+(r[i]*r[i]-r[p]*r[p]));
          if(ans[i][q+1]==-1 && q+1<=k )
            v.pb(mp(i,q+1));
          ans[i][q+1]=max(ans[i][q+1],val);
       }
       v.pb(mp(i,1));
       ans[i][1]=2*r[i]*h[i]+r[i]*r[i];
    }
    for(i=1;i<=n;i++)
    {
       maxi=max(maxi,ans[i][k]);
    }
    maxi=maxi*3.1415926;
    printf("Case #%d: %.6lf\n",w,maxi);
  }
  return 0;
}