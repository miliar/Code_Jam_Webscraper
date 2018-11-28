#include<bits/stdc++.h>
#define pb push_back
#define F first
#define S second
#define mp make_pair
#define lli long long int
#define INF 1000000000000
#define MOD 1000000007
#define FOR(name,initial,final) for(lli name=initial;name<final;name++)
#define rz resize
#define all(x) (x).begin(),(x).end()
#define T int t; cin>>t; while(t--)
using namespace std;
typedef vector<lli> vli;
typedef pair<lli,lli> pi;
typedef pair<pair<lli,lli>,lli> ppi;
typedef vector<vector<lli> > vv;
int main()
{
	ios::sync_with_stdio(false);cin.tie(0);cout.tie(0);
	int t;
	cin>>t;
	for(int test=1;test<=t;test++)
	{
		int n,k;
		double u;
		cin>>n>>k;
		cin>>u;
		vector<double> v(n+1);
		FOR(i,0,n)
		{
			cin>>v[i];
		}
		v[n]=1.0;
		sort(all(v));
		FOR(i,1,n+1)
		{
			double req = v[i]-v[i-1];
			if(req*i<=u)
			{
				FOR(j,0,i)
				{
					v[j]+=req;
				}
				u-=req*i;
			}
			else
			{
				FOR(j,0,i)
				{
					v[j]+=u/i;
				}
				break;
			}
		}
		double ans=1;
		FOR(i,0,n)
		{
			ans*=v[i];
		}
		cout<<"Case #"<<test<<": "<<fixed<<setprecision(10)<<ans<<endl;

	}
}