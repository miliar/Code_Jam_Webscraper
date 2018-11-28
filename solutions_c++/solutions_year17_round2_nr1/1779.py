#include <bits/stdc++.h>
#define ll long long int
#define ld long double 
#define MOD 1000000007 
#define mem(a) memset(a,0,sizeof(a))
#define pb push_back
#define ff first
#define ss second 
#define ios ios_base::sync_with_stdio(false);

using namespace std;

long double k[1010], s[1010];

int main()
{
	ll t;
	ll d,n;
	long double qq ,ww;
	cin>>t;
	for(ll i=1; i<=t; i++)
	{
		cout<<"Case #"<<i<<": ";
		mem(k);
		mem(s);
		cin>>d>>n;
		long double tm = 0;
		for(ll i=0; i<n; i++)
		{
			cin>>qq>>ww;
			tm=max(tm, (d-qq)/ww);
		}
		cout<<setprecision(10)<<d/tm<<endl;
	}
	return 0;
}