#include<stdio.h>
#include<bits/stdc++.h>
using namespace std;
#define ll long long
ll mod=1000000007;
ll pw(ll a,ll b)
{
  ll x=1;
  while(b)
  {
    if(b&1)
     x*=a;
    a*=a;
    b>>=1;
  }
  return x;
};
vector<int>v;
double pi;
double dp[1001][1001];
double x[1001];
int r[1001],h[1001];
int main()
{
  //freopen("A-small-attempt2.in", "r", stdin);
  //freopen("a.out", "w", stdout);
  //cout.precision(7);
  pi=acos(-1);
  //cout<<3*pi;
  int t,i,j,k,q,p,n;
  scanf("%d",&t);
  for(i=1;i<=t;i++)
  {
    scanf("%d%d",&n,&k);
    for(j=1;j<=n;j++)
    {
      scanf("%d%d",&r[j],&h[j]);
      x[j]=2*pi*(double)r[j]*(double)h[j];
      //cout<<x[j]<<endl;
    }
    double tmp;
    for(j=1;j<=k;j++)
    {
      for(p=1;p<=n;p++)
       dp[j][p]=0;
    }
    for(j=1;j<=n;j++)
     dp[1][j]=x[j];
    for(j=2;j<=k;j++)
    {
      for(p=1;p<=n;p++)
      {
        for(q=1;q<=n;q++)
        {
          if(r[q]>=r[p] && p!=q)
          {
            //cout<<q<<' '<<p<<' '<<j<<endl;
            tmp=dp[j-1][q]+x[p];
            //cout<<tmp<<' '<<dp[j-1][q]<<endl;
            tmp+=pi*((double)r[q]*r[q]-(double)r[p]*r[p]);
            //cout<<dp[j][p]<<' '<<tmp<<endl;
            if(tmp>dp[j][p])
            {
              dp[j][p]=tmp;
            }
            //cout<<dp[j][p]<<' '<<j<<endl;
          }
        }
      }
    }
    double mx=0;
    for(j=1;j<=n;j++)
    {
      //cout<<dp[k][j]<<endl;
      dp[k][j]+=pi*((double)r[j]*(double)r[j]);
     // cout<<dp[k][j]<<endl;
      mx=max(mx,dp[k][j]);
    }
    //cout<<mx;
    //cout<<"Case #"<<i<<": "<<mx<<endl;
    printf("Case #%d: %0.7lf\n",i,mx);
  }
  return 0;
}
