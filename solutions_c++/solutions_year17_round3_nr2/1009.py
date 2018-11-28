#include<bits/stdc++.h>
using namespace std;
#define ll long long
#define pf(z) printf("%lld\n",z)
#define sf(z) scanf("%lld",&z)
int main()
{
    freopen("B-small-attempt3.in","r",stdin);
	freopen("outputf.in","w",stdout);
	ll t;
	cin>>t;
	for(ll test=1;test<=t;test++)
	{
		cout<<"Case #"<<test<<": ";
		ll ac,aj;
		cin>>ac>>aj;
		if(ac+aj==1)
		{
			ll temp1,temp2;
			cin>>temp1>>temp2;
			cout<<"2\n";
		}
		else
		{
			if(ac==1&&aj==1)
			{
				ll temp1,temp2;
				cin>>temp1>>temp2>>temp1>>temp2;
				cout<<"2\n";
			}
			else
			{
				ll a[4];
				cin>>a[0]>>a[1]>>a[2]>>a[3];
				sort(a,a+4);
				if(a[3]-a[0]<=720||1440-a[2]+a[1]<=720) cout<<"2\n";
				else cout<<"4\n";
			}
		}
	}
}
