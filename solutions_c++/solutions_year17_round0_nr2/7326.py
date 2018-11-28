#include <bits/stdc++.h>
using namespace std;

#define IOS ios::sync_with_stdio(0); cin.tie(0); cout.tie(0);
#define endl "\n"
#define Max(x,y,z) max(x,max(y,z))
#define Min(x,y,z) min(x,min(y,z))
#define fr(i,s,e) for(i=s;i<e;i++)
#define rf(i,s,e) for(i=s-1;i>=e;i--)
#define pb push_back
#define eb emblace_back
#define mp make_pair
#define ff first
#define ss second
#define ll long long
#define trace1(x)                cerr<<#x<<": "<<x<<endl
#define trace2(x, y)             cerr<<#x<<": "<<x<<" | "<<#y<<": "<<y<<endl
#define trace3(x, y, z)          cerr<<#x<<":" <<x<<" | "<<#y<<": "<<y<<" | "<<#z<<": "<<z<<endl
#define trace4(a, b, c, d)       cerr<<#a<<": "<<a<<" | "<<#b<<": "<<b<<" | "<<#c<<": "<<c<<" | "<<#d<<": "<<d<<endl
#define trace5(a, b, c, d, e)    cerr<<#a<<": "<<a<<" | "<<#b<<": "<<b<<" | "<<#c<<": "<<c<<" | "<<#d<<": "<<d<<" | "<<#e<< ": "<<e<<endl
#define trace6(a, b, c, d, e, f) cerr<<#a<<": "<<a<<" | "<<#b<<": "<<b<<" | "<<#c<<": "<<c<<" | "<<#d<<": "<<d<<" | "<<#e<< ": "<<e<<" | "<<#f<<": "<<f<<endl
#define vl vector<long long>

#define vi vector<int> 
#define vii vector< vector<int> >
#define vll vector< vector<long long> >
#define vpi vector< vector<pair<ll,ll> > >  


bool less_vectors(const vector<int>& a,const vector<int>& b) 
{   return a.size() > b.size();
}
class CompareDist
{
public:
    bool operator()(pair<ll,ll> p1,pair<ll,ll> p2)
	{
        	
		return p1.ff>p2.ff;
		
    }
};
 
int main()
{
	IOS;
	freopen("B-small-attempt1.in","r",stdin);
	freopen("tpop.txt","w",stdout);
	int t;
	cin>>t;
	int l=0;
	while(t--)
	{
		ll n;
		cin>>n;
		ll n1=n;
		ll c=0;
		ll p=1;
		while(n1>0)
		{
			p*=10;
			c++;
			n1/=10;
			
		}
		p/=10;
		ll ans=0;
		if(c==1)
			ans=n;
		for(ll i=1;i<c;i++)
		{
			ll b=n/p;
			ll x=0;
			for(int j=1;j<=c-i;j++)
			{
				x=x*10+b;
			}
			//trace1(x);
			if(n%p>=x)
			{
				ans=ans+b*p;
				n=n%p;
				if(i==c-1)
				{
					ans+=n%p;
				}
			//	trace2(ans,n);
			}
			else
			{
				ans=ans+(b-1)*p;
				ll tmp=0;
				for(int j=1;j<=c-i;j++)
				{
					tmp=tmp*10+9;
				}
			//	trace2(ans,tmp);
				ans=ans+tmp;
				break;
			}
			p/=10;
			
		}
		l++;
		cout<<"Case #"<<l<<": "<<ans<<endl;
	}
	return 0;
}
