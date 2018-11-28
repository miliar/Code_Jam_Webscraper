#include<bits/stdc++.h>
using namespace std;
typedef long long ll;

pair<ll,ll> value(ll num)
{	if(num%2==0)return make_pair(num/2-1,num/2);
	else return make_pair(num/2,num/2);
}

pair<ll,ll> height(ll k,ll n)
{
	ll child=0;
	ll add=0;
	ll h=0;
	while(1)
	{	add = (1LL)<<h;
		if(child+add>=k)break;
		child += add;
		h++;
	}
	ll left_people = n-child;
	ll rem = left_people%add;
	ll divisor = left_people/add;
	ll left_k = k-child;
	pair<ll,ll> obt;
	if(rem>=left_k)obt = value(divisor+1);
	else obt = value(divisor);
	
	return make_pair(max(obt.first,obt.second),min(obt.first,obt.second));
	
}

int main()
{
	int t;
	scanf("%d",&t);
	int iterator=1;
	while(t--)
	{	ll n,k;
		cin>>n>>k;
		pair<ll,ll> ans = height(k,n);
		cout<<"Case #"<<iterator<<": "<<ans.first<<" "<<ans.second<<endl;
		iterator++;
	}
	
	
}
