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

int main()
{
	ios_base::sync_with_stdio(0); cin.tie(0);
	freopen("A-small.in", "r", stdin);
	freopen("A-small.out", "w", stdout);
	int t; cin>>t;
	for(int zz = 1; zz <= t; zz++)
	{
		cout<<"Case #"<<zz<<": ";
		int n,p; cin>>n>>p;
		int cnt[p];
		memset(cnt,0,sizeof(cnt));
		for(int i=0;i<n;i++)
		{
			int x; cin>>x;
			x%=p;
			cnt[x]++;
		}
		int ans = 0;
		ans+=cnt[0];
		if(p==2)
		{
			ans+=cnt[1]/2;
			cnt[1]%=2;
			if(cnt[1]) ans++;
		}
		else if(p==3)
		{
			int tmp = min(cnt[1],cnt[2]);
			ans+=tmp;
			cnt[1]-=tmp;
			cnt[2]-=tmp;
			while(cnt[1]>0)
			{
				cnt[1]-=3;
				ans++;
			}
			while(cnt[2]>0)
			{
				cnt[2]-=3;
				ans++;
			}
		}
		else if(p==4)
		{
			ans+=cnt[2]/2;
			cnt[2]%=2;
			int tmp = min(cnt[1],cnt[3]);
			ans+=tmp;
			cnt[1]-=tmp;
			cnt[3]-=tmp;
			if(cnt[1]>0)
			{
				assert(cnt[3]==0);
				while(cnt[2]>0&&cnt[1]>0)
				{
					cnt[1]-=2;
					cnt[2]--;
					ans++;
				}
				while(cnt[1]>0)
				{
					cnt[1]-=4;
					ans++;
				}
			}
			else if(cnt[3]>0)
			{
				assert(cnt[1]==0);
				while(cnt[2]>0&&cnt[3]>0)
				{
					cnt[3]-=2;
					cnt[2]--;
					ans++;
				}
				while(cnt[3]>0)
				{
					cnt[3]-=4;
					ans++;
				}
			}
		}
		cout<<ans<<'\n';
		cerr<<"Case #"<<zz<<" solved.\n";
	}
}

