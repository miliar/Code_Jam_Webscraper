#include <bits/stdc++.h>
using namespace std;

#define ff first
#define ss second
#define pp pair< pair<ll, ll>, pair<ll, ll> >

typedef long long ll;

pp fn(pp a, ll n)
{
	if(n==1) return a;
	else
	{
		pp b;
		if(a.ff.ff == a.ff.ss)
		{
			b.ff.ff = a.ff.ff/2;
			b.ff.ss = (a.ff.ff-1)/2;
			b.ss.ff = b.ss.ss = (a.ss.ff+a.ss.ss);
		}
		else if(a.ff.ff%2 == 0)
		{
			b.ff.ff = a.ff.ff/2;
			b.ff.ss = (a.ff.ff-1)/2;
			b.ss.ff = a.ss.ff;
			b.ss.ss = a.ss.ff + 2*a.ss.ss;
		}
		else if(a.ff.ff%2 == 1)
		{
			b.ff.ff = a.ff.ss/2;
			b.ff.ss = (a.ff.ss-1)/2;
			b.ss.ss = a.ss.ss;
			b.ss.ff = 2*a.ss.ff + a.ss.ss;
		}
		return fn(b,n-1);
	}
}

int main() {
	int t; cin>>t;
	ll n, k, temp;
	pp b;
	for(int q=1; q<=t; q++)
	{
		cin>>n>>k;
		ll cntr = ((ll)ceil(log2(k+1)))-1;
		if(cntr==0)temp = n;
		else
		{
			b.ff.ff = n/2;
			b.ff.ss = (n-1)/2;
			b.ss.ss = 1;
			b.ss.ff = 1;
			b = fn(b,cntr);
			if((k-(2<<(cntr-1)))<b.ss.ff)temp = b.ff.ff;
			else temp = b.ff.ss;
		}
		cout<<"Case #"<<q<<": "<<temp/2<<" "<<(temp-1)/2<<"\n";
	}
	return 0;
}