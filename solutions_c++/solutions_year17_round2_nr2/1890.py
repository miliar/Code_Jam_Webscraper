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
int ans[MAXN];
int fin[MAXN];
pii ar[5];
int main() {
	freopen("TASK.in","r",stdin);freopen("TASK.out","w",stdout);
	fast_cin;
	precompute();
	int t;
	cin>>t;
	int cc = 0;
	while(t--) {
		++cc;
		int N, R, O, Y, G, B, V;
		cin>>N>>R>>O>>Y>>G>>B>>V;
		int n = N;
		int z = min(2*O,B);
		if(z&1) --z;
		B -= z;
		B += z/2;
		O -= z/2;
		
		z = min(2*G,R);
		if(z&1) --z;
		R -= z;
		R += z/2;
		G -= z/2;
		

		z = min(2*V,Y);
		if(z&1) --z;
		Y -= z;
		Y += z/2;
		V -= z/2;
		
		cout<<"Case #"<<cc<<": ";
		if(V or G or O) {
			cout<<"IMPOSSIBLE\n";
			continue;
		}
		ar[1] = mp(R,1);
		ar[2] = mp(Y,2);
		ar[3] = mp(B,3);
		sort(ar+1,ar+1+3);
		int gg = ar[1].ff;
		int cnt = 1;
		while(gg--) {
			fin[cnt++] = ar[3].ss;
			fin[cnt++] = ar[2].ss;
			fin[cnt++] = ar[1].ss;
		}
		ar[2].ff -= ar[1].ff;
		ar[3].ff -= ar[1].ff;
		gg = ar[2].ff;
		while(gg--) {
			fin[cnt++] = ar[3].ss;
			fin[cnt++] = ar[2].ss;
		}
		--cnt;
		ar[3].ff -= ar[2].ff;
		ans[1] = fin[1];
		int id = 1;
		for(int i=1;i<cnt;i++) {
			if(ar[3].ff and fin[i]!=ar[3].ss and fin[i+1]!=ar[3].ss) {
				ans[id++] = fin[i];
				ans[id++] = ar[3].ss;
				ar[3].ff--;
			}
			else ans[id++] = fin[i];
		}
		bool is = true;
		if(ar[3].ff) is = false;
		ans[id++] = fin[cnt];
		assert(is?(id-1 == n):true);
		for(int i=2;i<=n;i++) if(ans[i]==ans[i-1]) is = false;
		if(ans[1]==ans[n]) is = false;
		if(!is) {
			cout<<"IMPOSSIBLE\n";
			continue;
		}
		for(int i=1;i<=n;i++) {
			if(ans[i] == 1) cout<<"R";
			if(ans[i] == 2) cout<<"Y";
			if(ans[i] == 3) cout<<"B";
		}
		cout<<endl;
	}
	return 0;
}
