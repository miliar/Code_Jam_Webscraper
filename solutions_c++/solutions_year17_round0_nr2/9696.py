#include<bits/stdc++.h>
#define ll long long
using namespace std;
bool check(ll n)
{
ll k=n%10;
	n/=10;
	while(n)
	{
		ll w=n%10;
	if(w>k)
		return false;
		k=w;
		n/=10;
	}
	return true;
}

int main()
{
ll n,t;
cin>>t;
for(int j=1;j<=t;j++)
{
	cin>>n;
for(ll i=n;i>0;i--)
{
	if(check(i))
	{
		cout<<"Case #"<<j<<": "<<i<<endl;
		break;
	}
}
}
}
