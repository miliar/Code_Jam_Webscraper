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
int ar[500];
int p;
int get(int x) {
	if(x < 0) x+=p;
	return x;
}
int dp[4][102][102][102];
int go(int mod, int one, int two, int three) {
	if(one == 0 and two == 0 and three == 0) return 0;
	if(dp[mod][one][two][three]!=-1) return dp[mod][one][two][three];
	int add = 0;
	if(mod==0) add = 1;
	int ret = 0;
	if(one) ret = max(ret, add + go(get(mod - 1), one - 1, two, three));
	if(two) ret = max(ret, add + go(get(mod - 2), one, two - 1, three));
	if(three) ret = max(ret, add + go(get(mod - 3), one, two, three - 1));
	return dp[mod][one][two][three]=ret;
}
int main() {
	// freopen("TASK.in","r",stdin);freopen("TASK.out","w",stdout);
	precompute();
	int t;
	cin>>t;
	int cc=0;
	while(t--) {
		++cc;
		cout<<"Case #"<<cc<<": ";
		int ans = 0;
		int n;
		cin>>n>>p;
		for(int i=1;i<=n;i++) cin>>ar[i];
		memset(dp,-1,sizeof(dp));
		// if(p==2) {
		// 	int zero=0,one=0;
		// 	for(int i=1;i<=n;i++) if(ar[i]%p==0) zero++;else one++;
		// 	ans = zero + (one + 1) / 2;

		// }
		// else if(p==3){
		// 	int zero=0,one=0,two=0;
		// 	for(int i=1;i<=n;i++) if(ar[i]%p==0) zero++;else if(ar[i]%p==1) one++;else two++;
		// 	ans = zero;
		// 	ans+=min(one,two);
		// 	int v=min(one,two);
		// 	one-=v;
		// 	two-=v;
		// 	if(one) ans+=(one+2)/3;
		// 	if(two) ans+=(two+2)/3;
		// }
		// else {
		// 	// memset(dp,-1,sizeof(dp));
		// 	// int gg[10];
		// 	// gg[0]=gg[1]=gg[2]=gg[3]=0;
		// 	// for(int i=1;i<=n;i++) gg[ar[i]%p]++;
		// 	// int lft = n - gg[0];
		// 	// ans = gg[0];
		// 	// if(lft) ans += go(0, gg[1], gg[2], gg[3]);
		// }
		// cout<<ans<<endl;
		int gg[10];;
		for(int i=0;i<10;i++) gg[i]=0;
		for(int i=1;i<=n;i++) gg[ar[i]%p]++;
		ans=gg[0];
		ans+=go(0,gg[1],gg[2],gg[3]);
		cout<<ans<<endl;
	}
	return 0;
}
