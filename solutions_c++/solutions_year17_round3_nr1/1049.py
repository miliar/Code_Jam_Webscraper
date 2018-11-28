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
#define PI 3.14159265358979323846 
using namespace std;
typedef vector<lli> vli;
typedef pair<lli,lli> pi;
typedef pair<pair<lli,lli>,lli> ppi;
typedef vector<vector<lli> > vv;
int main()
{
	ios::sync_with_stdio(false);cin.tie(0);cout.tie(0);
	int t,n,k;
	cin>>t;
	for(int test=1;test<=t;test++)
	{
		cin>>n>>k;
		double a,b;
		vector<pair<double,double> > v(n);
		FOR(i,0,n)
		{
			cin>>v[i].F>>v[i].S;
		}
		sort(all(v),greater<pair<double,double> >());
		double ans=0;
		FOR(i,0,n-k+1)
		{
			priority_queue<double> q;
			FOR(j,i+1,n)
			{
				q.push(v[j].F*v[j].S);
			}
			double sum=0;
			FOR(j,0,k-1)
			{	
				sum+=q.top();
				q.pop();

			}
			sum+=v[i].F*v[i].S;
			sum*=2;
			sum+=v[i].F*v[i].F;
			sum*=PI;
			ans=max(ans,sum);
		}
		cout<<"Case #"<<test<<": "<<fixed<<setprecision(10)<<ans<<endl;
	}
}