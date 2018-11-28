#include <bits/stdc++.h>
typedef long long ll;
using namespace std;

bool checkND (ll n, ll digits)
{
	int prev=11;
	int curr=0;
	for (int i = 0; i < digits; ++i)
	{
		curr=n%10;
		n=n/10;
		if(curr > prev)
			return false;
		prev = curr;
	}
	return true;
}

ll ndigits(ll n)
{
	ll c=0;
	while(n>0)
	{
		c++;
		n=n/10;
	}
	return c;
}


int main()
{
	int t,T;
	cin>>t;
	T=t;
	while(t--)
	{
		ll n;
		ll rem;
		cin>>n;
		rem = n;
		ll mult = 1;
		ll digits = ndigits(n);
		// cout<<"digits"<<digits;
		while(!checkND(n,digits))
		{
			// cout<<"entered\n";
			int last = rem%10;
			if( last != 9)
			{
				n-=mult*(last+1);
			}
			// cout<<"n is "<<n<<endl;
			mult*=10;
			rem = n;
			rem/=mult;
			digits = ndigits(n);
		}
		cout<<"Case #"<<T-t<<": "<<n<<endl;
	}
}