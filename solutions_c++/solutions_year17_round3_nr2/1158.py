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
  //freopen("B-small-attempt5.in", "r", stdin);
  //freopen("a.out", "w", stdout);
  //cout.precision(7);
  pi=acos(-1);
  int t,i,cnt=0,a,b,c,d;
  scanf("%d",&t);
  for(i=1;i<=t;i++)
  {
    scanf("%d%d",&a,&b);
    if(a==2 || b==2)
    {
      scanf("%d%d%d%d",&a,&b,&c,&d);
      if(a>c)
      {
        swap(a,c);
        swap(b,d);
      }
      if(d-a<=720 || (b+(1440-c))<=720)
       cnt=2;
      else
       cnt=4;
    }
    else
    {
      if(a==1 && b==1)
      {
        scanf("%d%d%d%d",&a,&b,&c,&d);
         cnt=2;
      }
      else
      {
        scanf("%d%d",&a,&b);
         cnt=2;
      }
    }
    printf("Case #%d: %d\n",i,cnt);
  }
  return 0;
}
