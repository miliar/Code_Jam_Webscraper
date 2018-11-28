#include <bits/stdc++.h>
#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/tree_policy.hpp>

using namespace std;
using namespace __gnu_pbds;

#define fi first
#define se second
#define mp make_pair
#define pb push_back
#define fbo find_by_order
#define ook order_of_key

typedef long long ll;
typedef pair<ll,ll> ii;
typedef vector<int> vi;
typedef long double ld; 
typedef tree<int, null_type, less<int>, rb_tree_tag, tree_order_statistics_node_update> pbds;
typedef set<int>::iterator sit;
typedef map<int,int>::iterator mit;
typedef vector<int>::iterator vit;

ii getres(ll x)
{
	return mp(x/2,(x-1)/2);
}

unordered_map<ll,ll> ma;

ll solve(ll n, ll k)
{
	if(k>n)
	{
		return 0;
	}	
	if(ma.find(n)!=ma.end()) return ma[n];
	ll ans = 1;
	if(n&1)
	{
		ans+=2LL*solve((n>>1),k);
	}
	else
	{
		ans+=solve((n>>1),k);
		ans+=solve((n>>1)-1,k);
	}
	return (ma[n]=ans);
}

int main()
{
	ios_base::sync_with_stdio(0); cin.tie(0);
	freopen("C-large.in", "r", stdin);
	freopen("C-large.out", "w", stdout);
	int t; cin>>t;
	for(int zz = 1; zz <= t; zz++)
	{
		cout<<"Case #"<<zz<<": ";
		ll n, k; cin>>n>>k;
		ll lo = 1; ll hi = n;
		ll ans = 0;
		while(lo<=hi)
		{
			ll mid = (lo+hi)>>1;
			ma.clear();
			if(solve(n,mid)>=k)
			{
				lo = mid + 1;
				ans = mid;
			}
			else
			{
				hi = mid - 1;
			}
		}
		ii tmp = getres(ans);
		cout<<tmp.fi<<' '<<tmp.se<<'\n';
		cerr<<"Case #"<<zz<<" solved.\n";
	}
}
