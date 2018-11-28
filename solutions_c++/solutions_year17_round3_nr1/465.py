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
typedef pair<long double,long double> pii;
typedef pair<int,pair<int,int> > piii;
typedef pair<ll,ll> pll;

ll POWER[65];
ll power(ll a, ll b) {ll ret=1;while(b) {if(b&1) ret*=a;a*=a;if(ret>=MOD) ret%=MOD;if(a>=MOD) a%=MOD;b>>=1;}return ret;}
ll inv(ll x) {return power(x,MOD-2);}

void precompute() {
	POWER[0]=1;
	for(int i=1;i<63;i++) POWER[i]=POWER[i-1]<<1LL;
}
long double INF = 2e18;
long double check = -1e18;
const int MAXN = 1002;
long double dp[MAXN][MAXN];
bool f[MAXN][MAXN];
pii A[MAXN];
int n;
const long double PI = acos(-1.0);
long double go(int idx, int lft) {
	if(lft==1) {
		return PI*A[idx].ff*A[idx].ff + 2.0*PI*A[idx].ff*A[idx].ss;
	}
	if(idx==n+1) return -INF;
	int LFT = n-idx+1;
	if(LFT<lft) return -INF;
	if(f[idx][lft]) return dp[idx][lft];
	f[idx][lft] = true;
	long double ret = -INF;
	for(int i=idx+1;i<=n;i++) {
		long double Z = go(i, lft-1);
		long double add = 2.0*PI*A[idx].ff*A[idx].ss;
		add += PI*(A[idx].ff*A[idx].ff - A[i].ff*A[i].ff);
		if(Z>check) ret = max(ret, Z + add);
	}
	return dp[idx][lft] = ret;
}
bool cmp(const pii &A, const pii &B) {
	if(A.ff>B.ff) return true;
	return false;
}
int main() {
	// freopen("TASK.in","r",stdin);freopen("TASK.out","w",stdout);
	precompute();
	int t;
	cin>>t;
	int cc=0;
	while(t--) {
		++cc;
		int k;
		cin>>n>>k;
		memset(f,false,sizeof(f));
		for(int i=1;i<=n;i++) {
			cin>>A[i].ff>>A[i].ss;
		}
		sort(A+1,A+1+n,cmp);
		long double ret = -INF;
		for(int i=1;i<=n;i++) ret = max(ret, go(i,k));
		cout<<"Case #"<<cc<<": ";
		cout<<fixed<<setprecision(9)<<ret<<endl;
	}
	return 0;
}
