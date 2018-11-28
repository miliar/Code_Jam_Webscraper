#include <iostream>
#include <cstdio>
#include <map>
#include <iterator>
#define X first
#define ll long long
using namespace std;

ll n,k;
map<ll,ll> M;
void solve()
{
	cin >> n >> k;
	M.clear();
	M[n]=1;
	while (k>0)
	{
		ll p=(*prev(M.end(),1)).X;
		if (k>M[p])
		{
			if (M.count((p-1)/2)) M[(p-1)/2]+=M[p];
			else M[(p-1)/2]=M[p];
			if (M.count((p-1)-(p-1)/2)) M[(p-1)-(p-1)/2]+=M[p];
			else M[(p-1)-(p-1)/2]=M[p];
			k-=M[p];
			M.erase(p);
		}
		else
		{
			cout << (p-1)-(p-1)/2 << ' ' << (p-1)/2;
			k=0;
		}
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