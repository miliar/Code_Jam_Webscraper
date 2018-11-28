#include <iostream>
#include <string>
#include <fstream>
#include <algorithm>
#include <vector>
#include <set>

using namespace std;
typedef long long ll;
typedef pair<ll,ll> ii;
//...
//
static ii solve(ll n,ll m,ll cb,ll cs)
{
	if(m<=cb)
	{
		ll v1=(n-1)/2;
		ll v2=n-1-v1;
		return ii(max(v1,v2),min(v1,v2));
	}
	m-=cb;
	if(m<=cs)
	{
		ll v1=(n-2)/2;
		ll v2=n-2-v1;
		return ii(max(v1,v2),min(v1,v2));
	}
	m-=cs;
	ll maxi=(n-1)/2;
	maxi=n-1-maxi;
	ll cs2=0;
	ll cb2=cb;
	if((n-1)/2==maxi)
		cb2+=cb;
	else
		cs2+=cb;
	if(n-2-((n-2)/2)==maxi)
		cb2+=cs;
	cs2+=(cb+cb+cs+cs-cs2-cb2);
	return solve(maxi,m,cb2,cs2);
}
static ii solve2(ll n,ll m)
{
	if(n==m)
		return ii(0,0);
	vector<bool> vec(n);
	for(ll i=0;i<m;i++)
	{
		vector<ll> L(n);
		vector<ll> R(n);
		for(ll j=1;j<n;j++)
			if(!vec[j]&&!vec[j-1])
				L[j]=L[j-1]+1;
		for(ll j=n-2;j>-1;j--)
			if(!vec[j]&&!vec[j+1])
				R[j]=R[j+1]+1;
		ii best=ii(-1,-1);
		ll b=-1;
		for(ll k=0;k<n;k++)
		{
			if(vec[k])
				continue;
			if(min(L[k],R[k])>best.first||(min(L[k],R[k])==best.first&&max(L[k],R[k])>best.second))
			{
				best=ii(min(L[k],R[k]),max(L[k],R[k]));
				b=k;
			}
		}
		if(i==m-1)
			return ii(best.second,best.first);
		vec[b]=true;
	}
}
int main()
{
	ofstream fout;
	ifstream fin;
	fout.open("output.txt");
	fin.open("C-large.in");
	ll t;
	fin >> t;
	for(ll i=0;i<t;i++)
	{
		cout << i << endl;
		ll n,m;
		fin >> n >> m;
		if(i==5)
		{
			cout << n << m << endl;
		}
		ii res=solve(n,m,1,0);
		res.first = max(res.first,ll(0));
		res.second = max(res.second,ll(0));
		fout <<"Case #" << i+1 << ": " << res.first << " " << res.second << endl;

	}
}