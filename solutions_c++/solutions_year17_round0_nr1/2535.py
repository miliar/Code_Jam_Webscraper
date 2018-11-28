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
lld solve()
{
  string s;
  cin>>s;
  lld k;
  is(k);
  i=s.size()-1;
  ans=0;
  while(i>=k-1)
  {
    if(s[i]=='-')
    {
      ans++;
      j=0;
      while(j<k)
      {
        if(s[i-j]=='-')
        {
          s[i-j]='+';
        }
        else
        {
          s[i-j]='-';
        }
        j++;
      }
    }
    i--;
  }
  lld flag=0;
  while(i>=0)
  {
    if(s[i]=='-')
    {
      flag=1;
    }
    i--;

  }
  if(flag==1)
  {
    ps("IMPOSSIBLE\n");
    
  }
  else
  {
    pp(ans);
  }
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
