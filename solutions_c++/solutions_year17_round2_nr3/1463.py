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
const lld M =1e2+7;
const lld mod=1e9+7;
const lld infi =LLONG_MAX;
lld i,j,ans,k,n,x,y,m,mymax=LLONG_MIN,mymin=LLONG_MAX,b,c,z,sum;
ld dp[M][M],d[M][M],E[M],S[M],temp[M][M];
lld solve()
{ 
    lld n,Q;
    cin>>n>>Q;
    up(1,n+1,i)
    {
      cin>>E[i]>>S[i];
    }
    up(1,n+1,i)
    {
      up(1,n+1,j)
      {
        cin>>temp[i][j];
        if(temp[i][j]==-1)temp[i][j]=0;
      }
    }
    down(n,0,i)
    {
      d[i][i]=0;
      up(i+1,n+1,j)
      {
        
        d[i][j]=d[i+1][j]+temp[i][i+1];
       // dg3(i,j,d[i][j]);
      } 
    }
    lld v,u;
    ds(v,u);
    down(n,0,i)
    {
      up(i+1,n+1,j)
      {
        if(d[i][j]<=E[i])
          dp[i][j]=d[i][j]/S[i];
        else
          dp[i][j]=1e16;
       // dg3(i,j,dp[i][j]);  
        up(i+1,j,k)
        {
          if(d[i][k]>E[i])break;
          if(dp[i][j]>((d[i][k]/S[i])+dp[k][j]))
          {
            dp[i][j]=(d[i][k]/S[i])+dp[k][j];
           
          }
        }
        
      }
    }
   cout<<fixed<<setprecision(6)<<dp[1][n]<<endl;
}
int main()
{
  freopen("c.in","r",stdin);
  freopen("c.out","w",stdout);
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
