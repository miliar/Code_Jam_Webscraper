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
const int MAXN = 1e3;
multiset<int>::iterator init[MAXN];
multiset<int> s[MAXN];
int req[MAXN];

int main() {
	// freopen("TASK.in","r",stdin);freopen("TASK.out","w",stdout);
	precompute();
	int t;
	cin>>t;
	int cc=0;
	while(t--) {
		++cc;
		int n,p;
		cin>>n>>p;
		for(int i=1;i<=n;i++) cin>>req[i],s[i].clear();
		int maxi = -1;
		for(int i=1;i<=n;i++) {
			for(int j=1;j<=p;j++) {
				int x;
				cin>>x;
				s[i].insert(x);
				maxi = max(maxi,x);
			}
		}
		int ans = 0;
		for(int i=1;i<=2*maxi;i++) {
			bool is = true;
			int mini = 1e9;
			for(int j=1;j<=n;j++) {
				ll R = 1LL*req[j]*i;
				if(R>=2*maxi) {
					is = false;
					break;
				}
				double RX = 0.9*R;
				double RY = 1.1*R;
				auto it = s[j].lower_bound((int)ceil(RX));
				if(it==s[j].end()) {
					is = false;
					break;
				}
				auto it2 = s[j].upper_bound((int)floor(RY));
				if(it2==s[j].begin()) {
					is = false;
					break;
				}
				--it2;
				if(*it>*it2) {
					is = false;
					break;
				}
				if(*it<RX or *it>RY) {
					is = false;
					break;
				}
				int gg=1;
				auto temp = it;
				while(temp!=it2) {
					++gg;
					++temp;
				}
				mini = min(mini,gg);
				init[j] = it;
			}
			if(!is) continue;
			for(int j=1;j<=n;j++) {
				int x = mini;
				while(x--) {
					auto er = init[j];
					++init[j];
					s[j].erase(er);
				}
			}
			ans += mini;
		}
		cout<<"Case #"<<cc<<": "<<ans<<endl;
	}
	return 0;
}
