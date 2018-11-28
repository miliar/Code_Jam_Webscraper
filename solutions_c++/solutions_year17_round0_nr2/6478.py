#include<iostream>
#include<vector>
using namespace std;
#define ll long long int

int main()
{
	ll t;
	cin>>t;
	ll j=1;
	while(t--)
	{
		ll n;
		cin>>n;
		
		vector<ll> v;
		while(n)
		{
			v.push_back(n%10);
			n=n/10;
		}
		
		ll m = v.size();
		ll l=m-1,i;
		for(i=m-2;i>=0;i--)
		{
			if(v[i]>v[i+1])
			l=i;
			else if(v[i]<v[i+1])
			break;
		}
		
		
		if(m>1 && l>0 && i>=0)
		{
			v[l] = v[l]-1;
			for(ll k=0;k<l;k++)
			v[k]=9;
		}
		i=m-1;
		while(v[i]==0)
		i--;

		cout << "Case #" << j << ": ";
		for(;i>=0;i--)
		cout<<v[i];
		cout<<endl;
		j++;
	}
return 0;
}
