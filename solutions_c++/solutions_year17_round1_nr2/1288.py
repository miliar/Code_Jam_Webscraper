#include <bits/stdc++.h>
using namespace std;

typedef pair<int,int> ii;
typedef pair<ii,int> pii;
typedef vector<int> vi;
typedef vector<ii> vii;
typedef vector<pii> vpii;
typedef long long int ll;
typedef unsigned long long int ull;

#define mi 1000000007
#define rep(i,a,b) for(i=a;i<b;i++)
#define repv(i,a,b) for(i=b-1;i>=a;i--)
#define pr(arr,n) rep(i,0,n) cout<<arr[i]<<" "; cout<<endl;
#define pr1(arr,n) rep(i,1,n+1) cout<<arr[i]<<" "; cout<<endl;
#define inf INT_MAX
#define gc getchar_unlocked
#define PB push_back
#define MP make_pair
#define fi first
#define se second
#define SET(a,b) memset(a,b,sizeof(a))
#define MAX 500005
#define gu getchar
#define pu putchar
#define si(n) scanf("%d",&n)
#define dout(n) printf("%d\n",n)
#define sll(n) scanf("%lld",&n)
#define lldout(n) printf("%lld\n",n)

#define TRACE

#ifdef TRACE
#define trace1(x)                cerr << #x << ": " << x << endl;
#define trace2(x, y)             cerr << #x << ": " << x << " | " << #y << ": " << y << endl;
#define trace3(x, y, z)          cerr << #x << ": " << x << " | " << #y << ": " << y << " | " << #z << ": " << z << endl;
#define trace4(a, b, c, d)       cerr << #a << ": " << a << " | " << #b << ": " << b << " | " << #c << ": " << c << " | " << #d << ": " << d << endl;
#define trace5(a, b, c, d, e)    cerr << #a << ": " << a << " | " << #b << ": " << b << " | " << #c << ": " << c << " | " << #d << ": " << d << " | " << #e << ": " << e << endl;
#define trace6(a, b, c, d, e, f) cerr << #a << ": " << a << " | " << #b << ": " << b << " | " << #c << ": " << c << " | " << #d << ": " << d << " | " << #e << ": " << e << " | " << #f << ": " << f << endl;

#else

#define trace1(x)
#define trace2(x, y)
#define trace3(x, y, z)
#define trace4(a, b, c, d)
#define trace5(a, b, c, d, e)
#define trace6(a, b, c, d, e, f)

#endif

int mult(int x,int y)
{
  ll ans,x1=(ll)x,y1=(ll)y;
  ans=(x1*y1)%mi;
  return (int)ans;
}
int gcd(int a,int b) { return b==0 ? a : gcd (b,a%b);}
int lcm(int a,int b) { return a*(b/gcd(a,b));}

ll pow1(ll a,ll b)
{
  ll ans=1;
  while(b>0)
    {
      if(b&1) ans=(ans*a)%mi;	
      a=(a*a)%mi; b>>=1;
    }	
  return ans;
}
vector<vi> v;
int a[15],m[15][15];
int main()
{
  int t,n,p,i,j,cnt=0;
  si(t);
  while(t--)
    {
      cnt++;
      v.resize(0);
      si(n); si(p); v.resize(n+2);
      rep(i,1,n+1)
	si(a[i]);
      rep(i,1,n+1)
	{
	  rep(j,1,p+1)
	    {
	      int x;
	      si(x); m[i][j]=x;
	    }
	}
      int ans=0;
      if(n==1)
	{
	  rep(i,1,p+1)
	    {
	      if(m[1][i]%a[1]==0)
		ans++;
	      else
		{
		  int x=m[1][i]/a[1];
		  rep(j,max(1,x-100),x+100)
		    {
		      double x1=(double)j*a[1];
		      if((double)m[1][i]+1e-10>=0.9*x1 && (double)m[1][i]-1e-10<=1.1*x1)
			{
			  ans++;
			  break;
			}
		    }
		}
	    }
	  printf("Case #%d: %d\n",cnt,ans);
	  continue;
	}
      sort(m[2]+1,m[2]+p+1);
      do {
	int tmp=0;
	rep(i,1,p+1)
	  {
	    int mn1,mn2;
	    mn1=m[1][i]/a[1];
	    mn2=m[2][i]/a[2];
	    rep(j,max(1,min(mn1,mn2)-100),max(mn1,mn2)+100)
	      {
		double x1=(double)j*a[2],x2=(double)j*a[1];
		if(x1>1e7 || x2>1e7) break;
		if((double)m[2][i]+1e-10>=0.9*x1 && (double)m[2][i]-1e-10<=1.1*x1)
		  {
		    if((double)m[1][i]+1e-10>=0.9*x2 && (double)m[1][i]-1e-10<=1.1*x2)
		      {
			tmp++;
			break;
		      }
		  }
	      }
	  }
	ans=max(ans,tmp);
      }while(next_permutation(m[2]+1,m[2]+p+1));
      printf("Case #%d: %d\n",cnt,ans);
    }
  return 0;
}
