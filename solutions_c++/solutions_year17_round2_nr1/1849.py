#include<bits/stdc++.h>
using namespace std;
#define N 10005
#define pii pair<int,int>
#define ff first
#define ss second
#define mp make_pair
#define pb push_back
#define ll long long 
#define mod 1000000007
#define barn cin.sync_with_stdio(0);cin.tie(0)
pair<double,double> p[N];
int main()
{
  barn;
  //freopen("inputf.in","r",stdin);
  //freopen("outputf.in","w",stdout);
  int t,k,i;
  scanf("%d",&t);
  for(k=1;k<=t;k++)
  {
    double d,t,t1,ans;
    int n;
    scanf("%lf %d",&d,&n);
    for(i=0;i<n;i++)
      scanf("%lf %lf",&p[i].ff,&p[i].ss);
    sort(p,p+n);
    for(i=n-1;i>=0;i--)
    {
       if(i==n-1)
        t=(d-p[i].ff)/p[i].ss;
       else
       {
          t1=(d-p[i].ff)/p[i].ss;
          if(t1>t)
            t=t1;
       }
    }
    ans=d/t;
    printf("Case #%d: %.6lf\n",k,ans);
  }
  return 0;
}