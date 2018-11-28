// Dont hack this or I hack ur mama
#include <iostream>
#include <cstdio>
#include <vector>
#include <queue>
#include <map>
#include <string>
#include <algorithm>
#include <set>
#include <cmath>
#define ll long long 
#define ull unsigned long long
#define pb push_back
#define mp make_pair
#define EPS (1e-9)
using namespace std;

////////////// END OF TEMPLATE
ll N;
ll solve(ll n, ll g);
ll solve_dumb(ll n);
void read()
{
	freopen("1.in","r",stdin);
	freopen("1.out","w",stdout);
	int T;

	cin >> T;
	for(int i = 0 ;i< T; i++)
	{
		cin >> N;
		
		printf("Case #%d: %lld\n",i+1,solve(N,0));
	}	
}
pair<ll,ll> getFirst(ll d)
{
	ll digs = 1;
	while(d >=10)
		d/=10,digs*=10;
	return mp(d,digs);
}
bool good(ll d)
{
	if(d < 10)
		return true;
	ll g = 9;
	while(d > 0)
	{
		if(d%10 > g) return false;
		g = d%10;
		d/=10;
	}
	return true;
}
ll solve_dumb(ll n)
{
	for(ll i = n; i>=1;i--)
	{
		if(good(i))
			return i; 
	}
}
ll solve(ll n, ll g)
{
//out << n << ' '<< g<< endl;
	if(n < 10)
	{
		if(g > n)
			return -1;
		else
			return n;
	}else{
		pair< ll , ll > f = getFirst(n);
		ll dig = f.first;
		if(g > dig )
			return -1;
		ll nextDig = n - dig * f.second;
		ll ret = nextDig < f.second/10 ? -1 : solve( nextDig, f.first);
	       	if(ret == -1)
		{
			dig--;
			if(g > dig) 
				return -1;
			else
				return dig * f.second + f.second-1;
		}else{
			return dig*f.second + ret;
		}
	}	
}
int main()
{
	std::ios::sync_with_stdio(false);
	read();
	
	return 0;
}


