#include<bits/stdc++.h>
#define up(j,k,i) for(i=j;i<k;i++)
#define down(j,k,i) for(i=j;i>k;i--)
#define pp(n) printf("%lld\n",n)
#define ps(s) printf("%s",s)
#define is(n) scanf("%lld",&n)
#define ips(n) scanf("%lld",n)
#define ss(s) scanf("%s",s)
#define cool 0
#define pb push_back
#define mp make_pair
#define F first
#define S second
#define f(i) cout<<i<<endl;
#define pll pair<lld,lld> 
#define pi acos(-1)
#define dg(x) cout<<#x<<' '<<x<<endl;
#define dg2(x,y) cout<<#x<<' '<<x<<' '<<#y<<' '<<y<<endl;
#define dg3(x,y,z) cout<<#x<<' '<<x<<' '<<#y<<' '<<y<<' '<<#z<<' '<<z<<endl;
#define ds(n,m) scanf("%lld %lld",&n,&m)
#define ts(n,m,k) scanf("%lld %lld %lld",&n,&m,&k)
typedef long double ld;
typedef long long int lld;
using namespace std;
const lld M =1e18+7;
const lld mod=1e9+7;
const lld infi =LLONG_MAX;
struct levels
{
  lld size;
  map <lld,lld> cnt;
};
void solve()
{
  lld n,k;
  ds(n,k);
  levels tree[68];
  tree[0].cnt[n]++;
  tree[0].size=1;
  lld level=1,tsize=1,cnt;
  while(tsize!=0)
  {
    tsize=0;
//    dg(level);
    for(auto kk:tree[level-1].cnt)
    {
      n=kk.F;
      cnt=kk.S;
      if(n<=1)continue;
      tsize+=cnt;
//      dg2(n,cnt);
      //cin>>k;
      if(n%2==0)
      {
        tree[level].cnt[n/2]+=cnt;
        if(n>2)
        {
          tree[level].cnt[n/2-1]+=cnt;
          tsize+=cnt;
        
        }
      
      }
      else
      {
        n--;
        tree[level].cnt[n/2]+=2*cnt;
        tsize+=cnt;
      }
    }
    if(tsize==0)break;
    tree[level].size=tsize;
    level++;
  }
  lld max_level=level;
  tsize=0;
  level=0;
  while(tsize+tree[level].size<k&&level<max_level)
  {
    tsize+=tree[level].size;
    level++;
  }
  priority_queue <pll> pq;
  for(auto kk:tree[level].cnt)
  {
    pq.push({kk.F,kk.S});
  }
  k-=tsize;
  k-=pq.top().S;
  
  while(k>0)
  {
    pq.pop();
    k-=pq.top().S;
  }
  n=pq.top().F;
  lld ls,rs;
  if(n%2==0)
    {
      ls=n/2;
      rs=ls-1;
    }
    else
    {
      ls=rs=n/2;
    }
    if(ls<rs)swap(ls,rs);
    printf("%lld %lld\n",ls,rs);
}
int main()
{
  freopen("C.in","r",stdin);
  freopen("out.out","w",stdout);
  lld t;
  is(t);
        lld tt=1;
        while(tt<=t)
        {   
             printf("Case #%lld: ",tt);solve();  
         //    dg(tt); 
               tt++;
        }
        
        return 0;
}
