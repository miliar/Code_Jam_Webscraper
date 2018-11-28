#include<stdio.h>
#include<bits/stdc++.h>
using namespace std;
#define ll long long
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
struct node
{
  ll p,s;
}a[10001];
bool cmp(node a,node b)
{
  if(a.p!=b.p)
   return a.p>b.p;
   return a.s<b.s;
};
struct pnt
{
  double d,t,s;
};
vector<pnt>adj[1011];
int main()
{
   //freopen("A-small-attempt1(1).in", "r", stdin);
   //freopen("a.out", "w", stdout);
  cout.precision(7);
  int t,c,n,i;
  ll d;
  scanf("%d",&t);
  for(c=1;c<=t;c++)
  {
    scanf("%lld%d",&d,&n);
    for(i=0;i<n;i++)
     scanf("%lld%lld",&a[i].p,&a[i].s);
    sort(a,a+n,cmp);
    for(i=0;i<n;i++)
     adj[i].clear();
    pnt tmp;
    tmp.d=(double)a[0].p;
    tmp.t=((double)d-a[0].p)/a[0].s;
    tmp.s=(double)a[0].s;
    adj[0].push_back(tmp);
    int j;
    double cur,cnt;
    for(i=1;i<n;i++)
    {
      cur=a[i].p;
      cnt=a[i].s;
      ///cout<<cur<<' '<<cnt<<endl;
      for(j=0;j<adj[i-1].size();j++)
      {
        double tm;
        if(adj[i-1][j].s>=cnt)
        {
          cur+=cnt*adj[i-1][j].t;
          continue;
        }
        tm=(cur-adj[i-1][j].d)/(adj[i-1][j].s-cnt);
        //cout<<tm<<endl;
        //cout<<adj[i-1][j].t<<endl;
        if(tm<adj[i-1][j].t)
        {
          tmp.d=cur;
          tmp.t=tm;
          tmp.s=cnt;
          adj[i].push_back(tmp);
          tmp.d=cur+tm*cnt;
          tmp.t=adj[i-1][j].t-tm;
          tmp.s=adj[i-1][j].s;
          adj[i].push_back(tmp);
          j++;
          for(;j<adj[i-1].size();j++)
          {
            adj[i].push_back(adj[i-1][j]);
          }
        }
        else
        {
          cur+=cnt*adj[i-1][j].t;
          continue;
        }
      }
      if(adj[i].empty())
      {
        cur=a[i].p;
        cnt=a[i].s;
        tmp.d=cur;
        tmp.t=((double)d-cur)/cnt;
        tmp.s=cnt;
        adj[i].push_back(tmp);
      }
      //for(j=0;j<adj[i].size();j++)
       //cout<<adj[i][j].d<<' '<<adj[i][j].t<<' '<<adj[i][j].s<<endl;
       //cout<<endl;
    }
    cur=0;
    cnt=0;
    double ans=0;
    for(j=0;j<adj[n-1].size();j++)
    {
      cnt+=adj[n-1][j].t;
    }
    //cout<<cnt<<endl;
    ans=(d/cnt);
    cout<<"Case #"<<c<<": "<<ans<<endl;
  }
  return 0;
}
