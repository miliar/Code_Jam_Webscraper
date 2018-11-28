#include "bits/stdc++.h"
using namespace std;
template<typename T, typename S> void amax(T &a, S b){ if(a < b) a = b; }
template<typename T, typename S> void amin(T &a, S b){ if(a > b) a = b; }
#define rep(a,b,c) for(int a = b; a < c; a++)
#define per(a,b,c) for(int a = b; a > c; a--)
#define rit(it,v) for(auto &it:v)
#define mset(a, b) memset(a, b, sizeof(a))
#define mp make_pair
#define mt make_tuple
#define pb push_back
using ii = pair<int,int>;
using ll = long long;
using vi = vector<int>;
using ld = long double;
using vll = vector<ll>;
const ll mod = 1000000007;
ll powm(ll a, ll b){ll ans=1;a %= mod;for(;b;b>>=1){if(b&1)ans=ans*a%mod;a = a*a%mod;}return ans;}
const int maxn = 100;
int dp[4][maxn][maxn][maxn], p;
int solve(int last, int a, int b, int c){
	if(a+b+c == 0) return 0;
	if(dp[last][a][b][c] != -1) return dp[last][a][b][c];
	int ans = 0;
	if(a) ans = max(ans, (last == 0) + solve((last + 1)%p, a-1, b, c));  
	if(b) ans = max(ans, (last == 0) + solve((last + 2)%p, a, b-1, c));  
	if(c) ans = max(ans, (last == 0) + solve((last + 3)%p, a, b, c-1));
	return dp[last][a][b][c] = ans;
}		
int main(){
	int cs; scanf("%d", &cs);
	for(int cc = 1; cc <= cs; cc++){
		printf("Case #%d: ", cc);
		int n; cin >> n >> p;
		vi arr(n); rit(it, arr) cin >> it;
		rit(it, arr) it %= p;
		vi cnt(5, 0);
		rit(it, arr) cnt[it]++;
		int ans = cnt[0];
		mset(dp, -1);
		ans += solve(0, cnt[1], cnt[2], cnt[3]);
		cout << ans << endl;
		fprintf(stderr, "(%d) solved\n", cc);
	}
	return 0;
}
