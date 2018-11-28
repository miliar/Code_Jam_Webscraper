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

ll a[101];
multiset<ii> segments[101];
multiset<pair<ii,int> > intervals;
int main()
{
	ios_base::sync_with_stdio(0); cin.tie(0);
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	int t; cin>>t;
	for(int zz = 1; zz <= t; zz++)
	{
		cout<<"Case #"<<zz<<": ";
		int n,p; cin>>n>>p;
		for(int i=0;i<n;i++) cin>>a[i];
		ll mini=1000000000; ll maxi=0;
		for(int i=0;i<n;i++)
		{
			vector<ll> vec;
			for(int j=0;j<p;j++)
			{
				ll x; cin>>x;
				vec.pb(x);
			}
			sort(vec.begin(),vec.end());
			for(int j=0;j<p;j++)
			{
				ll x = vec[j];
				ll l = (x*10+a[i]*11-1)/(a[i]*11);
				ll r = (x*10)/(a[i]*9);
				segments[i].insert(mp(l,r));
				mini=min(mini,l);
				maxi=max(maxi,r);
				//cerr<<l<<' '<<r<<'\n';
				intervals.insert(mp(mp(l,r),i));
			}
		}
		int cnt = 0;
		for(int i=mini;i<=maxi;i++)
		{
			if(intervals.empty()) break;
			pair<ii,int> tmp = *(intervals.begin());
			if(tmp.fi.fi>i) continue;
			bool possible=1;
			while(possible)
			{
				vector<pair<ii,int> > V;
				for(int j=0;j<n;j++)
				{
					for(multiset<ii>::iterator it = segments[j].begin(); it != segments[j].end(); it++)
					{
						if((*it).fi<=i&&i<=(*it).se)
						{
							//cerr<<(*it).fi<<' '<<(*it).se<<' '<<j<<'\n';
							V.pb(mp((*it),j));
							break;
						}
						else if((*it).fi>i) break;
					}
				}
				if(int(V.size())==n)
				{
					cnt++;
					for(int i=0;i<n;i++)
					{
						pair<ii,int> tmp = V[i];
						multiset<ii>::iterator it = segments[tmp.se].find(V[i].fi);
						assert(it!=segments[tmp.se].end());
						multiset<pair<ii,int> >::iterator it2 = intervals.find(V[i]);
						assert(it2!=intervals.end());
						intervals.erase(it2);
						segments[tmp.se].erase(it);
					}
				}	
				else possible=0;
			}
		}
		for(int i=0;i<n;i++) segments[i].clear();
		intervals.clear();
		cout<<cnt<<'\n';
		cerr<<"Case #"<<zz<<" solved.\n";
	}
}
