#include <bits/stdc++.h>

using namespace std;

typedef long long int ll;

int main()
{
	ll t;
	cin >> t;
	for(ll i=1;i<=t;i++)
	{
		cout << "Case #" << i << ": ";
		ll n;
		cin >> n;
		if(n>=1&&n<=9)
		{
			cout << n << endl;
			continue;
		}
		vector<ll> a;
		ll temp = n;
		while(temp)
		{
			a.push_back(temp%10);
			temp/=10;
		}
		reverse(a.begin(),a.end());
		ll j,k,l,m;
		ll flag=0;
		for(j=1;j<a.size();j++)
		{
			if(a[j]<a[j-1])
			{
				flag =1;
				break;
			}
		}
		if(flag)
		{
			k = j;
			for(j-=1;j>=1;j--)
			{
				if(a[j]!=a[j-1])
					break;
			}
			
			if(a[j]==0)
			{
				a[j] = 9;
				a[j-1]-=1;
			} 
			else
				a[j]-=1;
			for(l=j+1;l<a.size();l++)
				a[l]=9;
		}
		for(j = 0;j<a.size();j++)
		{
			if(a[j]!=0)
				break;
		}
		for(;j<a.size();j++)
			cout << a[j];
		cout << endl;
	}
}