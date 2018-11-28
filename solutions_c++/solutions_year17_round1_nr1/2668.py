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
vector<string> s;
int arr[26][4];
int main()
{
  int mnr,mxr,mnc,mxc,i,j,t,n,m,k;
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  cin>>t;
  int cnt=0;
  while(t--)
    {
      cnt++;
      s.clear();
      cin>>n>>m;
      string s1;
      rep(i,1,n+1)
	{
	  cin>>s1;
	  s.PB(s1);
	}
      rep(i,0,26)
	arr[i][0]=arr[i][2]=inf,arr[i][1]=arr[i][3]=-inf;
      rep(i,0,n)
	{
	  rep(j,0,m)
	    {
	      if(s[i][j]!='?')
		{
		  arr[s[i][j]-'A'][0]=min(arr[s[i][j]-'A'][0],i);
		  arr[s[i][j]-'A'][1]=max(arr[s[i][j]-'A'][1],i);
		  arr[s[i][j]-'A'][2]=min(arr[s[i][j]-'A'][2],j);
		  arr[s[i][j]-'A'][3]=max(arr[s[i][j]-'A'][3],j);
		}
	    }
	}
      rep(i,0,26)
	{
	  if(arr[i][0]!=inf)
	    {
	      rep(j,arr[i][0],arr[i][1]+1)
		rep(k,arr[i][2],arr[i][3]+1)
		s[j][k]=(char)(i+'A');
	    }
	}
      int cnt1=0;
      while(true)
	{
	  cnt1++;
	  if(cnt1>20)
	    break;
	  rep(i,0,26)
	    {
	      if(arr[i][0]!=inf)
		{
		  int l2=arr[i][2],r2=arr[i][3],l1=arr[i][0],r1=arr[i][1];
		  int flag=0;
		  while(l1>0 && flag==0)
		    {
		      flag=0;
		      rep(j,l2,r2+1)
			if(s[l1-1][j]!='?')
			  flag=1;
		      if(flag==0)
			{
			  rep(j,l2,r2+1)
			    s[l1-1][j]=(char)(i+'A');
			  l1--;
			  arr[i][0]--;
			}
		    }
		  flag=0;
		  while(r1<n-1 && flag==0)
		    {
		      flag=0;
		      rep(j,l2,r2+1)
			if(s[r1+1][j]!='?')
			  flag=1;
		      if(flag==0)
			{
			  rep(j,l2,r2+1)
			    s[r1+1][j]=(char)(i+'A');
			  r1++;
			  arr[i][1]++;
			}
		    }
		}
	    }
	  rep(i,0,26)
	    {
	      if(arr[i][0]!=inf)
		{
		  int l2=arr[i][2],r2=arr[i][3],l1=arr[i][0],r1=arr[i][1];
		  int flag=0;
		  while(l2>0 && flag==0)
		    {
		      flag=0;
		      rep(j,l1,r1+1)
			if(s[j][l2-1]!='?')
			  flag=1;
		      if(flag==0)
			{
			  rep(j,l1,r1+1)
			    s[j][l2-1]=(char)(i+'A');
			  l2--;
			  arr[i][2]--;
			}
		    }
		  flag=0;
		  while(r2<m-1 && flag==0)
		    {
		      flag=0;
		      rep(j,l1,r1+1)
			if(s[j][r2+1]!='?')
			  flag=1;
		      if(flag==0)
			{
			  rep(j,l1,r1+1)
			    s[j][r2+1]=(char)(i+'A');
			  r2++;
			  arr[i][3]++;
			}
		    }
		}
	    }
	}
      cout<<"Case #"<<cnt<<":"<<endl;
      rep(i,0,n) cout<<s[i]<<endl;
    }
  return 0;
}
