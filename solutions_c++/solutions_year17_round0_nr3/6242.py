#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

int main()
{
	ios_base::sync_with_stdio(false),cin.tie(0);

	int tt;
	cin>>tt;
	for (int ti=1; ti<=tt; ti++)
	{
		ll n,k;
		ll a,b;
		
		cin>>n>>k;
		
		multiset<ll> s;
		s.insert(-n);
		
		while (k--)
		{
			ll m = -(*s.begin());
			s.erase(s.begin());
			
			a = (m-1)/2;
			b = m-a-1;
			s.insert(-a);
			s.insert(-b);
		}
	
		cerr<<"Case Done "<<ti<<'\n';
		cout<<"Case #"<<ti<<": ";
		cout<<max(a,b)<<' '<<min(a,b);
		cout<<'\n';
	}
	
    return 0;
}
