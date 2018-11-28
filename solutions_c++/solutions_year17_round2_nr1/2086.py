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
const int MAXN = 1e3+55;
ll S[MAXN],K[MAXN];
int main() {
	// freopen("TASK.in","r",stdin);freopen("TASK.out","w",stdout);
	fast_cin;
	precompute();
	int t;
	cin>>t;
	int cc = 0;
	while(t--) {
		++cc;
		long double Time;
		int d,n;
		cin>>d>>n;
		for(int i=1;i<=n;i++) cin>>K[i]>>S[i];
		for(int i=n;i>=1;i--) {
			if(i==n) {
				long double speed = S[i];
				long double dist = d - K[i];
				Time = 1.0*dist/speed;
				continue;
			}
			long double speed = S[i];
			long double dist = d - K[i];
			long double gg = 1.0*dist/speed;
			Time = max(Time, gg);
		}
		long double lo=0.0, hi=1e18, ret=0.0;
		int iter = 200;
		while(iter--) {
			long double mid = (lo+hi)/2.0;
			long double dist = mid*Time;
			long double gg = 1.0*d/Time;
			if(mid>=gg or dist>d) hi = mid;
			else lo=mid,ret=mid;
		}
		cout<<"Case #"<<cc<<": ";
		cout<<fixed<<setprecision(6)<<ret<<endl;
	}
	return 0;
}
