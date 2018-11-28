#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
string task(ll n)
{
	string k = "";
	while(n)
	{
		int res = n%10;
		n/=10;
		k+= char(res+'0');
	}
	reverse(k.begin(),k.end());
	return k;
}
ll fun(int p)
{
	ll res = 1;
	for(int i = 0;i < p;i++)
		res*=10;
	return res;
}
int main()
{
	ios::sync_with_stdio(0);
	freopen("B-large.in","r",stdin);
	freopen("sxav.out","w",stdout);
	int test; cin >>test;
	int tases = 1;
	while(test--)
	{
		ll n; cin >> n;
		string g = task(n);
		int i = 0;
		for(;i+1 < g.size();i++)
		{
			if(g[i] > g[i+1])
				break;
		}
		if(i+1 == g.size())
		{
			cout <<"Case #" <<tases++ <<": "<< n<< endl;
			continue;
		}
		while(i != 0)
		{
			if(g[i-1] > g[i]-1)
				i--;
			else break;
		}
		int p = g.size()-i-1;
		ll pon = fun(p);
		cout <<"Case #" <<tases++ <<": "<< n-n%pon-1 << endl;
	}
	return 0;
}
