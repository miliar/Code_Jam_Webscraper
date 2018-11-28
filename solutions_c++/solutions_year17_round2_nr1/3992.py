#include<bits/stdc++.h>
using namespace std;
#define ll long long
#define pf(z) printf("%lld\n",z)
#define sf(z) scanf("%lld",&z)
ll t,n;
double d;
int main()
{
	freopen("A-small-attempt1.in","r",stdin);
	freopen("outputf.in","w",stdout);
	cin>>t;
	cout<<fixed<<setprecision(6);
	for(ll test=1;test<=t;test++)
	{
		double ans;
		cin>>d>>n;
		if(n==1)
		{
			double a,b;
			cin>>a>>b;
			ans=(d*b)/(d-a);
		}
		else 
		{
			double a1,b1,a2,b2;
			cin>>a1>>b1>>a2>>b2;
			if(a1>a2)
			{
				swap(a1,a2);
				swap(b1,b2);
			}
			if(b2>=b1)
			{
				ans=(d*b1)/(d-a1);
			}
			else
			{
				double x=(b1*a2-b2*a1)/(b1-b2);
				if(x<d) ans=min(d*b2/(d-a2),b1*x/(x-a1));
				else ans=(d*b1)/(d-a1);
			}
		}
		printf("Case #%lld: ",test);
		cout<<ans<<endl;
	}
}
