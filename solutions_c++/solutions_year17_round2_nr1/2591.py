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
typedef pair<double,double> pi;
typedef pair<pair<double,double>,lli> ppi;
typedef vector<vector<lli> > vv;
int main()
{
	ios::sync_with_stdio(false);cin.tie(0);cout.tie(0);
	int t;
	cin>>t;
	for(int test=1;test<=t;test++)
	{
		double d,n;
		cin>>d>>n;
		vector<pi> v(n);
		FOR(i,0,n)
		{
			cin>>v[i].F>>v[i].S;
		}
		sort(all(v),greater<pi >());
		vector<double> time(n);
		time[0]=(d-v[0].F)/v[0].S;
		FOR(i,1,n)
		{
			v[i].S=min(v[i].S,(d-v[i].F)/time[i-1]);
			time[i]=(d-v[i].F)/v[i].S;
		}
		double ans = d/time[n-1];
		cout<<"Case #"<<test<<": "<<fixed<<setprecision(6)<<ans<<endl;

		
	}
}