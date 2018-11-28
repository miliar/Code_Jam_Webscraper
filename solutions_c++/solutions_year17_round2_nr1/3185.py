#include <bits/stdc++.h>
using namespace std;
#define MOD 1000000007
#define ll long long
#define INF 1e18
#define pb push_back
int main()
{
	ll t;
	cin>>t;
	ll z=0;
	ll d,n;
	long double ans;
	long double tim;
	ll pos,sp;
	while(t--)
	{
		z++;
		ans=0.0;
		cout<<"Case #"<<z<<": ";
		cin>>d>>n;
		for(int i=0;i<n;i++)
		{
			cin>>pos>>sp;
			tim=(d-pos);
			tim=tim/sp;
			if(tim>ans)
			{
				ans=tim;
			}
		}	
		ans=(d*1.0)/ans;
		cout<<fixed<<setprecision(6)<<ans<<endl;


	}
}