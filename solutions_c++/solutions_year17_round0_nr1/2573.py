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
int main()
{
  int t,n,i,j,k,x,cnt=0;
  ios::sync_with_stdio(false);
  cin>>t;
  while(t--)
    {
      string s,s1;
      cin>>s; cin>>x; s1=s;
      //from left
      int ans1=0,ans2=0,ans3=0,ans4=0;
      rep(i,0,s1.size())
	{
	  if(i+x-1==s.size()) break;
	  if(s1[i]=='-')
	    {
	      rep(j,i,i+x)
		{
		  if(s1[j]=='-') s1[j]='+';
		  else s1[j]='-';
		}
	      ans1++;
	    }
	}
      rep(i,0,s1.size())
	{
	  if(s1[i]=='-')
	    ans1=inf;
	}
      //from right
      s1=s;
      repv(i,0,s1.size())
	{
	  if(i-x+1<0) break;
	  if(s1[i]=='-')
	    {
	      repv(j,i-x+1,i+1)
		{
		  if(s1[j]=='-') s1[j]='+';
		  else s1[j]='-';
		}
	      ans2++;
	    }
	}
      rep(i,0,s1.size())
	{
	  if(s1[i]=='-')
	    ans2=inf;
	}
      //from left and right
      s1=s;
      i=0; j=s.size()-1;
      while(i<j)
	{
	  if(i+x-1==s.size()) break;
	  if(s1[i]=='-')
	    {
	      rep(k,i,i+x)
		{
		  if(s1[k]=='+') s1[k]='-';
		  else s1[k]='+';
		}
	      ans3++;
	    }
	  i++;
	  if(j-x+1<0) break;
	  if(s1[j]=='-')
	    {
	      repv(k,j-x+1,j+1)
		{
		  if(s1[k]=='+') s1[k]='-';
		  else s1[k]='+';
		}
	      ans3++;
	    }
	  j--;
	}
      rep(i,0,s1.size())
	if(s1[i]=='-') ans3=inf;
      //from right and left
      s1=s;
      i=0; j=s.size()-1;
      while(i<j)
	{
	  if(j-x+1<0) break;
	  if(s1[j]=='-')
	    {
	      repv(k,j-x+1,j+1)
		{
		  if(s1[k]=='+') s1[k]='-';
		  else s1[k]='+';
		}
	      ans4++;
	    }
	  j--;
	  if(i+x-1==s.size()) break;
	  if(s1[i]=='-')
	    {
	      rep(k,i,i+x)
		{
		  if(s1[k]=='+') s1[k]='-';
		  else s1[k]='+';
		}
	      ans4++;
	    }
	  i++;
	}
      cnt++;
      rep(i,0,s1.size())
	if(s1[i]=='-') ans4=inf;
      cout<<"Case #"<<cnt<<":"<<" ";
      if(ans1==inf && ans2==inf && ans3==inf && ans4==inf)
	cout<<"IMPOSSIBLE"<<endl;
      else
	cout<<min(min(ans1,ans2),min(ans3,ans4))<<endl;
    }
  return 0;
}
