#include <bits/stdc++.h>
using namespace std;

#define ll long long
#define rep(n) for(int i=0;i<(n);i++)

bool is_tidy(ll n)
{
	if(n%10==0) return false;
	std::vector<ll> v;
	while(n!=0)
	{
		v.push_back(n%10);
		n/=10;
	}

	rep(v.size()-1) if(v[i]<v[i+1]) return false;
	return true;
}

int main()
{
	ll t; cin>>t;
	rep(t)
	{
		ll n; cin>>n;
		while(!is_tidy(n)) n--;
		cout<<"Case #"<<i+1<<": "<<n<<endl;
		//cout<<is_tidy(n)<<endl;
	}
}