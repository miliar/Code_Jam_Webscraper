#include <iostream>
#include <cstdio>
#include <string>
#include <set>
#define ll long long
using namespace std;
const ll maxn = 1000;
const ll maxx = 18;
ll n;
string s;
ll a,b;
bool flag;
void quay(ll x)
{
	for (ll i=9; i>=1; i--)
	if (i>=a%10)
	{
		a=(a*10)+i;
		b=(b*10)+(s[x]-'0');
		if (a<=b)
		{
			if (x+1<s.size()) quay(x+1);
			else flag=true;
		}
		if (flag) return;
		a/=10;
		b/=10;
	}
}
void solve()
{
	cin >> n;
	s=to_string(n);
	flag=false;
	a=0;
	b=0;
	quay(0);
	if (flag)
	cout << a;
	else
	{
		for (ll i=0; i+1<s.size(); i++)
			cout << 9;
	}
}
int main()
{
	ios_base::sync_with_stdio(0);
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	ll t;
	cin >> t;
	for (ll i=1; i<=t; i++)
	{
		cout << "Case #" << i << ": ";
		solve();
		cout << '\n';
	}
	return 0;
}