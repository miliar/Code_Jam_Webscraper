#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

ll tidy(ll n, ll s, ll curr)
{
	if((s*10)==curr) return n;
	else
	{
		int d1 = (n/(curr/10))%10;
		int d2 = (n/curr)%10;
		if(d1<d2) 
		{
			n = (n/curr)*curr - 1;
		}
		return tidy(n,s,curr*10);
	}
}

int main() {
	int t; cin>>t;
	ll n, s;
	for(int q=1; q<=t; q++)
	{
		cin>>n;
		s=(ll)pow(10,floor(log10(n)));
		cout<<"Case #"<<q<<": "<<tidy(n,s,10)<<endl;
	}
	return 0;
}