#include <bits/stdc++.h>
typedef long long int ll;
using namespace std;

ll tidy(ll num)
{
	if((num/10)==0)
		return num;
		
	ll dig = num%10,temp = num;
	int f=1;
	while(temp)
	{
		ll k = temp%10;
		if(k>dig)
		{
			f=0;break;
		}
		
		dig = k;
		temp/=10;
	}

	if(f)
	{
		return tidy(num/10)*10 + num%10;
	}
	else
	return tidy( (num/10) -1 )*10 + 9;	
}


int main()
{
	ll t;cin>>t;
	for(ll tc=1;tc<=t;tc++)
	{
		cout<<"Case #"<<tc<<": ";
		ll n;cin>>n;

		cout<<tidy(n)<<"\n";

	}

	return 0;
}