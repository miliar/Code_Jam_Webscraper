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
bool is = false;
const int MAXN = 100;
string str[MAXN];
int grid[MAXN][MAXN];
vector<int> ans;
char RM[MAXN];
map<int,int> mapp;
int n,m;
bool check2(int X, int XX, int Y, int YY, int z) {
	for(int i=X;i<=XX;i++) for(int j=Y;j<=YY;j++) if(grid[i][j]!=z) return false;
	return true;
}
bool check(vector<int> &A) {
	int r = 0;
	int c=0;
	int cnt=0;
	for(int i=0;i<sz(A);i++) {
		if(i!=0 and i%m==0) ++r,c=0;
		grid[r][c++] = A[i];
	}
	++r;
	for(auto it:mapp) {
		int IX,IY=-1;
		for(int i=0;i<r and IY==-1;i++) {
			for(int j=0;j<c and IY==-1;j++) {
				if(grid[i][j] == it.ss) {
					IX = i;
					IY = j;
					break;
				}
			}
		}
		int tillX = r-1;
		int tillY = c-1;
		for(int i=IX;i<r;i++) {
			if(grid[i][IY] == it.ss);
			else {
				tillX = i-1;
				break;
			}
		}
		for(int i=IY;i<c;i++) {
			if(grid[IX][i] == it.ss);
			else {
				tillY = i-1;
				break;
			}
		}
		if(!check2(IX,tillX,IY,tillY,it.ss)) {
			return false;
		}
		else cnt += (tillX-IX+1)*(tillY-IY+1);
	}
	if(cnt!=n*m) return false;
	return true;
}
void go(int idx, vector<int> v) {
	if(is) return;
	if(idx==sz(v)) {
		if(check(v)) {
			ans = v;
			is = true;
		}
		return;
	}
	if(v[idx]==-1) {
		for(auto it:mapp) {
			v[idx] = it.ss;
			go(idx+1,v);
		}
	}
	else go(idx+1,v);
}
int main() {
	// freopen("TASK.in","r",stdin);freopen("TASK.out","w",stdout);
	precompute();
	int t;
	cin>>t;
	int cc=0;
	while(t--) {
		is = false;
		mapp.clear();
		++cc;
		vector<int> v;
		v.clear();
		cin>>n>>m;
		for(int i=1;i<=n;i++) {
			cin>>str[i];
			for(int j=0;j<sz(str[i]);j++) if(str[i][j]!='?') mapp[str[i][j]]++;
		}
		int c=0;
		for(auto &it:mapp) {
			it.ss=c++;
			RM[c-1] = it.ff;
		}
		for(int i=1;i<=n;i++) {
			for(int j=0;j<sz(str[i]);j++) {
				if(str[i][j]=='?') v.pb(-1);
				else v.pb(mapp[str[i][j]]);
			}
		}
		go(0,v);
		cout<<"Case #"<<cc<<":\n";
		for(int i=0;i<sz(ans);i++) {
			if(i!=0 and i%m==0) cout<<"\n";
			cout<<RM[ans[i]];
		}
		cout<<"\n";
	}
	return 0;
}
