#include<bits/stdc++.h>
#define nl ('\n')
#define pb push_back
#define MOD 1000000007
#define MAX 100000
typedef long long ll;
using namespace std;
//ll expo(ll x,ll y,ll M){ if(y==0) return 1; ll z = expo(x,y/2,M); if(y&1) return (1ll * ((1ll * x * z)%M) * z)%M; else return (1ll * z * z)%M;}
//ll gcd(ll x,ll y){ if(x==0) return y; return gcd(y%x,x); }
int main()
{
	//ios::sync_with_stdio(0);cin.tie(0);
	ll t,d,n,k,s;
	cin>>t;
	for(int i=1;i<=t;i++)
	{
		double ans = 0;
		cin>>d>>n;
		vector<pair<int,int>> pos;
		for(int j=1;j<=n;j++)
		{
			cin>>k>>s;
			pos.pb({k,s});
		}
		sort(pos.begin(),pos.end());
		reverse(pos.begin(),pos.end());double tim = 0.0;
		for(int j=0;j<pos.size();j++)
		{
			int dist = pos[j].first;
			double ti = (double)(d - dist) / pos[j].second;
			tim = max(ti,tim);
		}
		ans = (double) d / tim ; 
		cout<<"Case #"<<i<<": ";
		printf("%0.8lf\n",ans);
	}
	return 0;
}
