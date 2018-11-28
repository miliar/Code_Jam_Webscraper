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
#define vpi vector< pair<ll,ll> >  
typedef pair<pair<int, int>,int> P;
#define mod %1000000007
 
bool less_vectors(const vector<int>& a,const vector<int>& b) 
{
   return a.size() > b.size();
}

int gcd(int a,int b)
{
	if(a%b==0)
		return b;
		else
			return gcd(b,a%b);
}
vpi v;
ll n;
ll dp[15][15][15];
ll rec(int i,int k,int p)
{
	if(i==n)
		if(k==0)
		return v[p].ff*v[p].ff;
		else
			return -LONG_MAX;
	if(dp[i][k][p]==-1)
	{
		if(k==0)
			return v[p].ff*v[p].ff;
			else
			{
				if(p!=-1)
				return dp[i][k][p]=max(v[p].ff*v[p].ff-v[i].ff*v[i].ff+2*v[i].ss*v[i].ff+rec(i+1,k-1,i),rec(i+1,k,p));
				else
					return dp[i][k][p]=max(2*v[i].ss*v[i].ff+rec(i+1,k-1,i),rec(i+1,k,p));
			}
	}
	else
		return dp[i][k][p];
}
int main()
{
	
	freopen("A-small-attempt0.in","r",stdin);
	freopen("aout.txt","w",stdout);
	int l=0;
	int t;
	cin>>t;
	while(t--)
	{
		ll k;
		cin>>n>>k;
		v.clear();
		v.resize(n);
		for(int i=0;i<n;i++)
		{
			cin>>v[i].ff>>v[i].ss;
		}
		sort(v.rbegin(),v.rend());
		for(int i=0;i<15;i++)
		{
			for(int j=0;j<15;j++)
			{
				for(int k=0;k<15;k++)
					dp[i][j][k]=-1;
			}
		}
		ll as=rec(0,k,-1);
		//cout<<as<<endl;;
		std::cout.precision(7);
		cout.fixed;
		long double ans=(long double)as*(long double)3.141592653589;

		l++;
		cout<<"Case #"<<l<<": "<<fixed<<ans<<endl;
	}
	
return 0;
}