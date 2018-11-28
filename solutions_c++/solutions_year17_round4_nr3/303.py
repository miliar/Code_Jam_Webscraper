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
int HOR = 1, VER = -1;
char str[77][77];
int pos[77][77];
int NOT = 0;
bool GG[77][77];
int main() {
	// freopen("TASK.in","r",stdin);freopen("TASK.out","w",stdout);
	precompute();
	int t;
	cin>>t;
	int cc=0;
	while(t--) {
		int r,c;
		++cc;
		bool is = true;
		cout<<"Case #"<<cc<<": ";
		cin>>r>>c;
		for(int i=1;i<=r;i++) scanf("%s",str[i]+1);
		memset(pos,0,sizeof(pos));
		memset(GG,false,sizeof(GG));
		for(int i=1;i<=r;i++) {
			for(int j=1;j<=c;j++) {
				if(!(str[i][j]=='-' or str[i][j] == '|')) continue;
				for(int k = j-1;k>=1;k--) {
					if(str[i][k]=='#') break;
					if(!(str[i][k]=='-' or str[i][k] == '|')) continue;
					if(pos[i][j]!=NOT) {
						if(pos[i][j]!=VER) is = false;
					}
					if(pos[i][k] == NOT) {
						pos[i][k] = pos[i][j] = VER;
					}
					else {
						if(pos[i][k] != VER) is=false;
					}
					pos[i][j] = VER;
				}
				for(int k = j+1;k<=c;k++) {
					if(str[i][k]=='#') break;
					if(!(str[i][k]=='-' or str[i][k] == '|')) continue;
					if(pos[i][j]!=NOT) {
						if(pos[i][j]!=VER) is = false;
					}
					if(pos[i][k] == NOT) {
						pos[i][k] = pos[i][j] = VER;
					}
					else {
						if(pos[i][k] != VER) is=false;
					}
					pos[i][j] = VER;
				}
			}
		}
		for(int j=1;j<=c;j++) {
			for(int i=1;i<=r;i++) {
				if(!(str[i][j]=='-' or str[i][j] == '|')) continue;
				for(int k = i-1;k>=1;k--) {
					if(str[k][j]=='#') break;
					if(!(str[k][j]=='-' or str[k][j] == '|')) continue;
					if(pos[i][j]!=NOT) {
						if(pos[i][j]!=HOR) is = false;
					}
					if(pos[k][j] == NOT) {
						pos[k][j] = pos[i][j] = HOR;
					}
					else {
						if(pos[k][j] != HOR) is=false;
					}
					pos[i][j] = HOR;
				}
				for(int k = i+1;k<=r;k++) {
					if(str[k][j]=='#') break;
					if(!(str[k][j]=='-' or str[k][j] == '|')) continue;
					if(pos[i][j]!=NOT) {
						if(pos[i][j]!=HOR) is = false;
					}
					if(pos[k][j] == NOT) {
						pos[k][j] = pos[i][j] = HOR;
					}
					else {
						if(pos[k][j] != HOR) is=false;
					}
					pos[i][j] = HOR;
				}
			}
		}
		if(!is) {
			cout<<"IMPOSSIBLE\n";
			continue;
		}
		for(int i=1;i<=r;i++) {
			for(int j=1;j<=c;j++) {
				if(!(str[i][j]=='-' or str[i][j] == '|')) continue;
				if(pos[i][j]==NOT) continue;
				if(pos[i][j]==HOR) {
					for(int k = j+1;k<=c;k++) {
						if(str[i][k]=='#') break;
						GG[i][k] = true;
					}
					for(int k = j-1;k>=1;k--) {
						if(str[i][k]=='#') break;
						GG[i][k] = true;
					}
				}
				else {
					for(int k = i+1;k<=r;k++) {
						if(str[k][j]=='#') break;
						GG[k][j] = true;
					}
					for(int k = i-1;k>=1;k--) {
						if(str[k][j]=='#') break;
						GG[k][j] = true;
					}
				}
			}
		}
		for(int i=1;i<=r;i++) {
			for(int j=1;j<=c;j++) {
				if(!(str[i][j]=='-' or str[i][j] == '|')) continue;
				if(pos[i][j]!=NOT) continue;
				bool present = false;
				for(int k = j+1;k<=c;k++) {
					if(str[i][k]=='#') break;
					if(!GG[i][k]) present = true;
				}
				for(int k = j-1;k>=1;k--) {
					if(str[i][k]=='#') break;
					if(!GG[i][k]) present = true;
				}
				if(present) pos[i][j]=HOR;
				else pos[i][j]=VER;
				if(pos[i][j]==HOR) {
					for(int k = j+1;k<=c;k++) {
						if(str[i][k]=='#') break;
						GG[i][k] = true;
					}
					for(int k = j-1;k>=1;k--) {
						if(str[i][k]=='#') break;
						GG[i][k] = true;
					}
				}
				else {
					for(int k = i+1;k<=r;k++) {
						if(str[k][j]=='#') break;
						GG[k][j] = true;
					}
					for(int k = i-1;k>=1;k--) {
						if(str[k][j]=='#') break;
						GG[k][j] = true;
					}
				}
			}
		}
		for(int i=1;i<=r;i++) for(int j=1;j<=c;j++) {
			if(str[i][j]=='.' and GG[i][j]==false) is=false;
		}
		if(!is) {
			cout<<"IMPOSSIBLE\n";
			continue;
		}
		cout<<"POSSIBLE\n";
		for(int i=1;i<=r;i++) {
			for(int j=1;j<=c;j++) {
				if(str[i][j]=='-' or str[i][j]=='|') {
					if(pos[i][j]==HOR) cout<<"-";
					else cout<<"|";
				}
				else cout<<str[i][j];
			}
			cout<<endl;
		}
	}
	return 0;
}
