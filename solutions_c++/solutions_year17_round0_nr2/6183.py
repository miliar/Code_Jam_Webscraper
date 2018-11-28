#include <bits/stdc++.h>
using namespace std;
#define ll long long
int check(ll n)
{
	int a=n%10;
	n/=10;
	while(n)
	{
		if(n%10>a)return 0;
		a=n%10;
		n/=10;
	}
	return 1;
}
int main()
{
	//freopen("1.in","r",stdin);
	//freopen("out","w",stdout);
	int t;cin>>t;
	for(int o=1;o<=t;o++)
	{
		ll n;cin>>n;
		if(check(n))
		{
			printf("Case #%d: ",o);
			cout<<n<<endl;
			continue;
		}
		ll m=n;
		int a=m%10;
		ll b=1LL*a,c=1;
		m/=10;
		while(m)
		{
			if(check(n-b-1))
			{
				break;
			}
			a=m%10;
			c*=10;
			b+=a*c;
			m/=10;
		}
		n-=b+1;
		printf("Case #%d: ",o);
		cout<<n<<endl;
	}
	return 0;
}
