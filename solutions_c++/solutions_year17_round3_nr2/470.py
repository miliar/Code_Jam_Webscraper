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
const int MAXN = 1000;
int GG[MAXN];
bool cameron;
int INT[2][24*60+50];
int INF = 1e9;
int C[2][MAXN],D[2][MAXN];
int dp[2][24*60+3][722];
int go(int chance, int minute, int done) {
	if(INT[chance][minute]) return INF;
	// for(int i=1;i<=GG[chance];i++) {
	// 	if(minute>=C[chance][i] and minute<=D[chance][i]) return INF;
	// }
	if(done < 0) return INF;
	int cameronMovesLeft = done;
	int cameronMovesDone = 720 - done;
	int jamieMovesDone = minute-1-cameronMovesDone;
	int jamieMovesLeft = 720 - jamieMovesDone;
	if(chance and cameronMovesLeft <= 0) return INF;
	if(!chance and jamieMovesLeft <= 0) return INF;
	if(minute==24*60) {
		if(chance) {
			if(cameron) return 0;
			else return 1;
		}
		else {
			if(cameron) return 1;
			else return 0;
		}
	}
	if(dp[chance][minute][done]!=-1) return dp[chance][minute][done];
	int ret = INF;
	if(chance) {
		int Z;
		if(cameronMovesLeft > 1) {
			Z = go(chance, minute+1, cameronMovesLeft-1);
			if(Z<INF) ret = min(ret, Z);
		}
		Z = go(!chance, minute+1, cameronMovesLeft-1);

		if(Z<INF) ret = min(ret, 1 + Z);
	}
	else {
		int Z;
		if(jamieMovesLeft > 1) {
			Z = go(chance, minute+1, cameronMovesLeft);
			if(Z<INF) ret = min(ret, Z);
		}
		Z = go(!chance, minute+1, cameronMovesLeft);

		if(Z<INF) ret = min(ret, 1 + Z);
	}
	return dp[chance][minute][done] = ret;
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
		int AC,AJ;
		cin>>AC>>AJ;
		GG[1] = AC;
		GG[0] = AJ;
		memset(INT,0,sizeof(INT));
		for(int i=1;i<=AC;i++) {
			cin>>C[1][i]>>D[1][i];
			++C[1][i];
			INT[1][C[1][i]]++;
			INT[1][D[1][i]+1]--;
		}
		for(int i=1;i<=AJ;i++) {
			cin>>C[0][i]>>D[0][i];
			++C[0][i];
			INT[0][C[0][i]]++;
			INT[0][D[0][i]+1]--;
		}
		for(int i=0;i<2;i++) for(int j=1;j<24*60+15;j++) INT[i][j] += INT[i][j-1];
		int ret = 1e9;
		memset(dp,-1,sizeof(dp));
		cameron = false;
		ret = min(ret, go(false,1,720));
		memset(dp,-1,sizeof(dp));
		cameron = true;
		ret = min(ret, go(true,1,720));
		cout<<ret<<endl;
	}
	return 0;
}
