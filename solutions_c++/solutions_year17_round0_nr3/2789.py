#include<bits/stdc++.h>
using namespace std;
typedef unsigned long long ull;
#define fastScan ios_base::sync_with_stdio(0); cin.tie(NULL);
#define Fill(a,x) memset(a,x,sizeof(a))
#define ll long long int
#define MAX 4010
#define M 1000000007
//#define MOD 1000000007
#define pii pair<int,int>
#define pll pair<ll,ll>
#define mb make_pair
#define pb push_back
#define sc(x) scanf("%d",&x)
#define scc(x1,x2) scanf("%d%d",&x1,&x2)
#define sccc(x1,x2,x3) scanf("%d%d%d",&x1,&x2,&x3)
#define pr(x) printf("%d ",x)
#define prd(x) printf("%lf",x)
#define rep(i,n) for(int i=0;i<n;i++)
#define repp(i,a,b) for(int i=a;i<b;i++)
#define reff(i,a,b) for(int i=a;i>=b;i--)
#define IT(x) for(__typeof (x.begin()) it = x.begin(); it != x.end (); it++)
#define X first
#define Y second
#define co cout<<"vai"<<endl;
#define coo cout<<"yt"<<endl;
#define dbg(a)         std::cerr<<#a<<"="<<(a)<<"\n"
#define dbg1(a,b)       std::cerr<<#a<<"="<<(a)<<", "<<#b<<"="<<(b)<<"\n"
#define dbg2(a,b,c)     std::cerr<<#a<<"="<<(a)<<", "<<#b<<"="<<(b)<<", "<<#c<<"="<<(c)<<"\n"
#define dbg3(a,b,c,d)   std::cerr<<#a<<"="<<(a)<<", "<<#b<<"="<<(b)<<", "<<#c<<"="<<(c)<<", "<<#d<<"="<<(d)<<"\n"
#define dbg4(a,b,c,d,e) std::cerr<<#a<<"="<<(a)<<", "<<#b<<"="<<(b)<<", "<<#c<<"="<<(c)<<", "<<#d<<"="<<(d)<<", "<<#e<<"="<<(e)<<"\n"
ll gcd(ll a, ll b) { return (b == 0 ? a : gcd(b, a % b)); }
ll lcm(ll a, ll b) { return (a * (b / gcd(a, b))); }
ll power(ll x,ll y)
{
    ll ans=1;
    while(y>0){
        if(y&1)
            ans=(ans*x)%M;
        x=(x*x)%M;
        y/=2;
    }
    return ans%M;
}
const int INF = 2034567891;
const ll INF64 = 1234567890123456789ll;
const long double pi = 3.1415926535897932384626434;
const double eps = 1e-15;
int dx[] = {1,1,0,-1,-1,-1,0,1}, dy[] = {0,1,1,1,0,-1,-1,-1};

ifstream ifs("Subtask1.txt");
ofstream ofs("Solution1.txt");

int main()
{
    fastScan;
    //freopen("a.in","r",stdin);
    //freopen("b.out","w",stdout);
    ll t,k,ct=1,n;
    ifs>>t;
    while(t--)
    {
       ifs>>n>>k;
       map<ll,ll>mp;
       mp[n]++;
       ofs<<"Case"<<" "<<"#"<<ct<<": ";
       if(k==1)
       ofs<<max((n-1)/2,(n-1)-((n-1)/2))<<" "<<min((n-1)/2,(n-1)-((n-1)/2))<<endl;
       else
       {
       	 ll fl=0,f=0,an,cnti=0;
	     while(k>0)
	     {
	     	if(mp.size()==0)
	     	{
	     		//co;
	     		fl=1;
	     		break;
			 }
	   	  ll c=mp.rbegin()->X;
	   	  //dbg(c);
	   	  if(c==0)
	   	  {
	   	  //	cout<<"aa"<<endl;
	   	     fl=1;
			 break;	
		  }
		//  dbg1(mp[c],k);
		  if(mp[c]>=k)
		  {
		
		  	  f=1;
		  	  an=c;
		  	  break;
		  }
	   	 // dbg1(*it,s.size());
//	   	  for(auto j : mp)
//	   	  cout<<j.X<<" ";
//	   	  cout<<endl;

	      mp[max(0ll,(c-1)/2)]+=mp[c];
		  mp[max(0ll,(c-1)-((c-1)/2))]+=mp[c];
		//  dbg1(k,mp[c]);
		  k-=mp[c];	
		  mp.erase(c);
		  
//		  for(auto j : s)
//	   	  cout<<j<<" ";
//	   	  cout<<endl;
	      }
	      if(fl)
	      ofs<<"0"<<" "<<"0"<<endl;
	      else if(f)
	      ofs<<max((an-1)/2,(an-1)-((an-1)/2))<<" "<<min((an-1)/2,(an-1)-((an-1)/2))<<endl;
	      else
	      {
	       ll c=mp.rbegin()->X;
	      ofs<<max((c-1)/2,(c-1)-((c-1)/2))<<" "<<min((c-1)/2,(c-1)-((c-1)/2))<<endl;
	      }
	   }
	   //dbg(ct);
		ct++;
	}
}
