#include<bits/stdc++.h>

using namespace std;

#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/tree_policy.hpp>

using namespace __gnu_pbds;
 
#define ordered_set tree<int, null_type, less<int>, rb_tree_tag, tree_order_statistics_node_update>

#define ff first
#define ss second
#define pb push_back
#define mp make_pair
#define all(x) x.begin(),x.end()
#define sz(x) ((int)x.size())
#define eps 1e-9
#define fast_cin ios_base::sync_with_stdio(false)

const int MOD = 1e9+7;

typedef long long ll;
typedef pair<int,int> pii;
typedef pair<int,pair<int,int> > piii;
typedef pair<ll,ll> pll;

ll POWER[65];
ll power(ll a, ll b) {ll ret=1;while(b) {if(b&1) ret*=a;a*=a;if(ret>=MOD) ret%=MOD;if(a>=MOD) a%=MOD;b>>=1;}return ret;}
ll inv(ll x) {return power(x,MOD-2);}

void precompute() {
	POWER[0]=1;
	for(int i=1;i<63;i++) POWER[i]=POWER[i-1]<<1LL;
}
int mapp[3][1005];
int main() {
	// freopen("TASK.in","r",stdin);freopen("TASK.out","w",stdout);
	precompute();
	int t;
	cin>>t;
	int cc=0;
	while(t--) {
		++cc;
		cout<<"Case #"<<cc<<": ";
		int n,c,m;
		cin>>n>>c>>m;
		memset(mapp,0,sizeof(mapp));
		for(int i=1;i<=m;i++) {
			int p,b;
			cin>>p>>b;
			mapp[b][p]++;
		}
		int ans=0,ans2=0;
		for(int i=n;i>=1;i--) {
			int x = mapp[2][i];
			for(int j=1;j<=n;j++) {
				if(i==j) continue;
				int v = min(x,mapp[1][j]);
				x-=v;
				mapp[1][j]-=v;
				ans+=v;
			}
			mapp[2][i] = x;
		}
		int cnt=0;
		for(int i=1;i<=n;i++) {
			if(mapp[1][i] and mapp[2][i]) {
				cnt++;
				if(i==1) {
					ans+=mapp[1][i]+mapp[2][i];
				}
				else {
					ans+=max(mapp[1][i],mapp[2][i]);
					ans2+=min(mapp[1][i],mapp[2][i]);
				}
			}
			else if(mapp[1][i]) ans+=mapp[1][i];
			else if(mapp[2][i]) ans+=mapp[2][i];
		}
		assert(cnt<=1);
		cout<<ans<<" "<<ans2<<endl;
	}
	return 0;
}