#include<bits/stdc++.h>
#define endl '\n'
using namespace std;
typedef long long ll;
ll arr[20];
ll ans[20];
ll sz = 0;
ll n;
inline bool cmp(ll pos)
{
	ll temp = 0;
	for(ll i = 0; i<sz; ++i)
	{
		if(i<=pos)
			temp = temp*10 + ans[i];
		else
			temp *= 10;
	}
	if(temp>n)
		return 0;
	else
		return 1;
}

bool aux(ll pos)
{
	//cout<<"aux called with pos = "<<pos<<" ans pos -1 "<<ans[pos-1]<<endl;
	if(pos==sz)
		return 1;
	bool flag = 0;
	for(ll i = 9; i>=ans[pos-1]; --i)
	{
		ans[pos] = i;
		if(!cmp(pos)) continue;
		if(aux(pos+1))
			{flag = 1; break;}
	}
	if(flag)
		return 1;
	else
		return 0;
}

ll solve (ll n)
{
	ll temp = n;
	sz = 0;
	while(temp)
	{
		temp/=10;
		++sz;
	}
	temp = n;
	for(ll i=sz-1; i+1; --i)
	{
		arr[i] = temp%10;
		temp /= 10; 
	}
	/*
	for(ll i=0; i<sz; ++i)
	{
		cout<<arr[i];
	}
	cout<<endl;
	*/
	for(ll i = arr[0]; i>=0; --i)
	{
		ans[0] = i;
		if(aux(1))
			break;
	}
	ll ret=0;
	for(ll i=0; i<sz; ++i)
	{
		ret = ret*10 + ans[i];
	}
	return ret;
}


int main()
{
	ll t;
	cin>>t;
	ll i = 0;
	while(++i<=t)
	{
		cin>>n;
		cout << "Case #" << i <<": "<<solve(n)<<endl;
	}
	return 0;
}