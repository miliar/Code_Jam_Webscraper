#include <bits/stdc++.h>
using namespace std;
 
#define N 100005
#define fi first
#define se second
#define MOD 1000000007
 
#define pb push_back
 
#define ll long long
 
#define eps 1.0e-7
#define inf 1e9 + 5
#define double long double

#define pp pair<int,int>

int main()
{
	ios::sync_with_stdio();
	freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
	ll i,j,k,t,n,d,s,c=1;

	cin>>t;	
	while(t--)
	{
		double ans,tm=0;
		cin>>d>>n;
		for(i=0;i<n;i++)
		{
			cin>>k>>s;
			double tmp,dis;
			dis = d-k;
			tmp = dis/s;
			if(tmp>tm)
			{
				ans = d/tmp;
				tm = tmp;
			}
		}
		cout<<"Case #"<<c++<<": "<<setprecision(7)<<std::fixed<<ans<<"\n";
	}
}