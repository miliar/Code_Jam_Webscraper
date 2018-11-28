#include <bits/stdc++.h>
#define mp make_pair
#define pb push_back
#define ll long long 
#define pi pair<ll,ll>
#define pii pair<pi,ll>
#define graph std::vector<std::vector<ll> > 
#define sc(x) scanf("%lld",&x)
#define sp " "
using namespace std;

ll ison(ll x,ll i)
{
	return x&(1ll<<i);
}

const ll MOD=1e9+7;
const double PI =acos(-1.0);
const ll MAX=1e13;
const ll N=1e3+10;

ll n,k;
ll ls[N],rs[N],Mn[N],Mm[N];
bool occ[N];

int main()
{
	std::ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	ll t;
	cin>>t;
	for (int tc = 0; tc < t; ++tc)
	{
		cin>>n>>k;
		memset(occ,false,sizeof(occ));
		for(int i=1;i<=n;i++) ls[i]=i-1;
		for(int i=n;i>=1;i--) rs[i]=n-i;
		for(int i=1;i<=n;i++) Mn[i]=min(ls[i],rs[i]);
		for(int i=1;i<=n;i++) Mm[i]=max(ls[i],rs[i]);

		ll ans1,ans2,idx;
		while(k--)
		{
			ans2=Mn[1];
			for(int i=1;i<=n;i++)
			{
				if(occ[i]) continue;
				ans2=max(Mn[i],ans2);
			}


			ans1=-1;
			for (int i = 1; i < n+1; ++i)
			{
				if(occ[i]) continue;
				if(ans2==Mn[i])
				{
					ans1=max(Mm[i],ans1);
				}
			}

			for (int i = 1; i <=n; ++i)
			{
				if(occ[i]) continue;
				if(ans1==Mm[i] && ans2==Mn[i])
				{
					idx=i;
					break;
				}
			}

			occ[idx]=true;
			//cout<<idx<<endl;
			ll cnt=0;
			for(int i=idx-1;i>=1;i--)
			{
				if(occ[i]) break;
				rs[i]=min(cnt,rs[i]);
				cnt++;
			}
			cnt=0;
			for(int i=idx+1;i<=n;i++)
			{
				if(occ[i]) break;
				ls[i]=min(cnt,ls[i]);
				cnt++;
			}

			for(int i=1;i<=n;i++) Mn[i]=min(ls[i],rs[i]);
			for(int i=1;i<=n;i++) Mm[i]=max(ls[i],rs[i]);
		}

		cout<<"Case #"<<tc+1<<": ";
		cout<<max(ls[idx],rs[idx])<<" "<<min(ls[idx],rs[idx])<<"\n";
	}
	return 0;
}