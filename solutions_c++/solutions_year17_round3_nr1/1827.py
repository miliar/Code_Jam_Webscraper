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
const lld M =1e3+7;
const lld mod=1e9+7;
const lld infi =-2e16;
lld i,j,k,n,x,y,m,mymax=LLONG_MIN,mymin=LLONG_MAX,b,c,z,sum;
pll r[M];
bool myf(pll A,pll B)
{
  if(A.F*A.S>B.F*B.S)
    return true;
 return false;
}
bool my2(pll A,pll B)
{
  if(A.F>B.F)
    return true;
 return false;
}
lld solve()
{ 
    cin>>n>>k;
    up(0,n,i)
    {
      ds(r[i].F,r[i].S);
      
    }
    ld ans=0;
    sort(r,r+n,my2);
    up(0,n,i)
    {
       ld temp=0;
      temp+=r[i].F*r[i].F+2*r[i].F*r[i].S;
      pll t2[n+1];
      up(i+1,n,j)
      {
        t2[j-i-1]=r[j];
      }
      sort(t2,t2+n-i-1,myf);
      up(0,k-1,j)
      temp+=2*t2[j].F*t2[j].S;
      //dg3(i,temp,r[i].F);
     ans=max(ans,temp);
     }
    // cout<<ans<<endl;
    cout<<fixed<<setprecision(9)<<ans*pi<<endl;;
}
int main()
{
  freopen("A.in","r",stdin);
  freopen("A.out","w",stdout);
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
