#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

ll get(ll n, ll la)
{
	ll r=0,t=0,p=1,pp=0;
	int lo = log10(n);
	for (int i=0; i<=lo; i++)
	{
		t=t*10ll+1;
		for (int j=1; j<10; j++)
			if (t*j<=n && p<la) r=max(r,p*j), pp=p;
		p*=10;
	}
	if (!r) return 0;
	return r + get(n-r,pp);
}

int main()
{
	ios_base::sync_with_stdio(false),cin.tie(0);

	int tt;
	cin>>tt;
	for (int ti=1; ti<=tt; ti++)
	{
		ll n,r;
		cin>>n;
		
		r = get(n, n+1);	
	
		cerr<<"Case Done "<<ti<<'\n';
		cout<<"Case #"<<ti<<": ";
		cout<<r;
		cout<<'\n';
	}
	
    return 0;
}
