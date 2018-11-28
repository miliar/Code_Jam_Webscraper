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
#define vpi vector< pair<ll,ll> >  >  
typedef pair<pair<int, int>,int> P;

 
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
int main()
{
	
	freopen("A-large.in","r",stdin);
	freopen("out12.txt","w",stdout);
	int l=0;
	int t;
	cin>>t;
	while(t--)
	{
				int d,n;
		cin>>d>>n;
		vector<pair<int,int> > v(n);
		int xd,xs;
		int pos=INT_MAX;
		int s=INT_MAX;
		double t=0;
		for(int i=0;i<n;i++)
		{
			cin>>v[i].ff>>v[i].ss;
			double lt=(double)(d-v[i].ff)/(double)v[i].ss;
			t=max(t,lt);
			
		}
		
		
		
		double ans=d/t;
		
		l++;
		std::cout.precision(6);
		cout.fixed;
		cout<<"Case #"<<l<<": "<<fixed<<ans<<endl;
	}
	
return 0;
}
