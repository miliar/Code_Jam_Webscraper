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

ll hd, ad, hk, ak, b, d;

bool solve(ll turns)
{
	if(d==0)
	{
		if(ad>=hk)
		{
			return 1;
		}
		if(ak>=hd)
		{
			return 0;
		}
		if(2LL*ad>=hk||ad+b>=hk)
		{
			return (turns>=2);
		}	
		if(2LL*ak>=hd) //infinite cure loop
		{
			return 0;
		}
	}
	ll maxdturns = 0;
	if(d>0) maxdturns = (ak+d-1)/d;
	ll maxbturns = 0;
	if(b>0) maxbturns = (hk-ad+b-1)/b;
	for(ll i = 0; i <= maxdturns; i++)
	{
		for(ll j = 0; j <= maxbturns; j++)
		{
			if(i+j>=turns) break;
			//cerr<<i<<' '<<j<<'\n';	
			ll curhp = hd;
			ll curhpen = hk;
			int cnt=0;
			ll debuff = i;
			ll buff = j;
			ll curatk = ad;
			ll curatken = ak;
			bool pos=1;
			while(curhpen>0)
			{
				//if(hd==21) cerr<<cnt<<' '<<curhp<<' '<<curhpen<<'\n';
				cnt++;
				if(cnt>turns) break;
				if(curatk>=curhpen)
				{
					curhpen-=curatk;
					continue;
				}	
				if(curatken>=curhp)
				{
					if(debuff>0&&curatken-d<curhp)
					{
						curatken=max(0LL,curatken-d);
						curhp-=curatken;
						debuff--;
						if(curhpen<=0) break;
						if(curhp<=0)
						{
							pos=0; break;
						}
						continue;
					}
					curhp=hd;
					curhp-=curatken;
					if(curhpen<=0) break;
					if(curhp<=0)
					{
						pos=0; break;
					}
					continue;
				}
				if(debuff>0)
				{
					curatken=max(0LL,curatken-d);
					curhp-=curatken;
					debuff--;
					if(curhpen<=0) break;
					if(curhp<=0)
					{
						pos=0; break;
					}
					continue;
				}
				if(buff>0)
				{
					curatk+=b;
					curhp-=curatken;
					buff--;
					if(curhpen<=0) break;
					if(curhp<=0)
					{
						pos=0; break;
					}
					continue;
				}
				curhpen-=curatk;
				curhp-=curatken;
				if(curhpen<=0) break;
				if(curhp<=0)
				{
					pos=0; break;
				}
			}
			if(pos&&cnt<=turns) return 1;
		}
	}
	return 0;
}

int main()
{
	ios_base::sync_with_stdio(0); cin.tie(0);
	freopen("C-small3.in", "r", stdin);
	freopen("C-small3.out", "w", stdout);
	int t; cin>>t;
	for(int zz = 1; zz <= t; zz++)
	{
		cout<<"Case #"<<zz<<": ";
		cin>>hd>>ad>>hk>>ak>>b>>d;
		ll lo = 1; ll hi = 1000;
		ll ans = -1;
		while(lo<=hi)
		{
			ll mid = (lo+hi)>>1;
			if(solve(mid))
			{
				hi=mid-1;
				ans=mid;
			}
			else lo=mid+1;
		}
		if(ans==-1) cout<<"IMPOSSIBLE\n";
		else cout<<ans<<'\n';
		cerr<<"Case #"<<zz<<" solved.\n";
	}
}
