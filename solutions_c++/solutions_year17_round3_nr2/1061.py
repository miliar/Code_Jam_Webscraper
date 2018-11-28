#include<bits/stdc++.h>
#define vi vector<int>
#define vll vector<LL>
#define pii pair<int,int>
#define pli pair<LL,int>
#define pll pair<LL,LL>
#define fr first
#define sc second
#define MAX 50010
#define LL   long long int
#define ll   long long int
//#define LLL long long int
#define inf 1000000
#define INF 10000000
#define mod 1000000007
#define PI acos(-1)
//#define N 65
#define mMax 30010
#define nMax 2010
#define SZ(a) a.size()
#define pb push_back
#define eb emplace_back
#define mp make_pair
#define rep1(i,b) for(int i=1;i<=b;i++)
#define rep2(i,b) for(int i=0;i<b;i++)
#define rep(i,a,b) for(int i=a;i<=b;i++)
#define all(A) A.begin(),A.end()
#define isf(a) scanf("%d",&a);
#define Lsf(a) scanf("%I64d",&a);
#define lsf(a) scanf("%lld",&a);
#define csf(a) scanf("%c",&a);
#define vedge vector<Edge>
using namespace std;
LL bigmod(LL a,LL b,LL Mod)
{
    if(b==0) return 1ll;
    if(b%2) return (a*bigmod(a,b-1,Mod))%Mod;
    LL c=bigmod(a,b/2,Mod);
    return (c*c)%Mod;
}
int dp[2][1450][1450];
int C[1450];
int A[1450];
int st;
int call(int i,int rem,int t)
{
  if(rem<0 || rem>1440) return inf;
  if(i==1439)
  {
    if(rem==720)
    {
      if(t==st) {return 0;}
      return 1;
    }
    return inf;
  }
  int &ret=dp[t][i][rem];
  if(ret!=-1) return ret;
  ret=inf;
  if(t==0)
  {
    if(A[i]<0) return inf;
    if(A[i]>1)
    {
      ret=min(ret,call(C[i]-1,rem+A[i]-1,0));
    }
    else
    {
      ret=min(ret,call(i+1,rem+1,0));
      ret=min(ret,1+call(i+1,rem-1,1));
    }
  }
  else
  {
    if(A[i]>0) return inf;
    if(A[i]<-1)
    {
      ret=min(ret,call(C[i]-1,rem+A[i]+1,1));
    }
    else
    {
      ret=min(ret,call(i+1,rem-1,1));
      ret=min(ret,1+call(i+1,rem+1,0));

    }
  }
  return ret;
}
int main()
{
   freopen("input.in","r",stdin);
   freopen("output.txt","w",stdout);

  int T,I=1;
  cin>>T;
  while(T--)
  {
    printf("Case #%d: ",I++);
    int n,m;
    scanf("%d %d",&n,&m);
    memset(C,0,sizeof(C));
    memset(A,0,sizeof(A));
    rep2(k,n)
    {
      int a,b;
      scanf("%d %d",&a,&b);
      C[a]=b;
      A[a]=b-a;
    }
    rep2(k,m)
    {
      int a,b;
      scanf("%d %d",&a,&b);
      C[a]=b;
      A[a]=a-b;
    }
    memset(dp,-1,sizeof(dp));
    st=0;
    int ans=call(0,721,0);
    memset(dp,-1,sizeof(dp));
    st=1;
    ans=min(ans,call(0,719,1));
    printf("%d\n",ans);
  }
  return 0;
}
