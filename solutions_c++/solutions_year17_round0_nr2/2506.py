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
lld i,j,ans,k,n,x,y,m,mymax=LLONG_MIN,mymin=LLONG_MAX,b,c,z,sum;
lld p[20];
void solve()
{
  is(n);
  x=0;
  i=n;
  p[x]=1;
  while(n>0)
  {
    p[x+1]=10*p[x];
    x++;
    n/=10;
  }
  n=i;
  i=0;
  b=n;
  while(i<x)
  {
    b=n/p[i];
    y=b/10;
    if((y%10)>(b%10))
    {
      n-=p[i+1];
      n/=p[i+1];
      n=n*p[i+1]+(p[i+1]-1);
    }
    i++;
  }
  pp(n);
}
int main()
{
  freopen("in.in","r",stdin);
  freopen("out.out","w",stdout);
  lld t;
  is(t);
        lld tt=1;
        while(tt<=t)
        {   
             printf("Case #%lld: ",tt);solve();   
               tt++;
        }
        
        return 0;
}
