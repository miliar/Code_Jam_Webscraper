#include <bits/stdc++.h>

using namespace std;

#define INF 0x3f3f3f3f
#define NSYNC ios::sync_with_stdio(false)
#define FOR(i,a,b) for(int i=a; i<(b); ++i)
#define FOR0(i,b) for(int i=0; i<(b); ++i)
#define DBG(x) cout << #x << " == " << x << endl
#define DBGV(v) for(int x : v) cout << x << " "; cout << endl
#define DBGP(x,y) cout << "(" << x << ", " << y << ")" << endl
#define pb(x) push_back(x)
#define mp(x,y) make_pair(x,y)
#define sz(a) (int)((a).size())
#define all(c) (c).begin(),(c).end()
#define R(x) scanf(" %d",&(x))
#define RR(x,y) scanf(" %d %d",&(x), &(y))
#define CLR(v) memset(v, 0, sizeof(v))
#define SET(v) memset(v, -1, sizeof(v))

typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;

const int MAXN = 1010;
ll dp[20][11][3]; //pos, last, smaller
string s;
ll pwrs[20];
int n;

ll solve(int pos, int last, bool smaller) {
	if (pos==n) return 0;
	ll& ans = dp[pos][last][smaller];
	if (ans != -1) return ans;
	ans = -1e18;
	ll pwr = pwrs[n-1-pos];
	FOR(i,last,10) {
		if (!smaller && i+'0' > s[pos]) break;
		ans = max(ans, pwr*i + solve(pos+1, i, smaller || (i+'0' < s[pos])));
	}
	return ans;
}

int main() {
	NSYNC;
	pwrs[0] = 1;
	FOR(i,1,19) pwrs[i] = pwrs[i-1]*10;
	int t;
	cin >> t;
	FOR0(i,t) {
		cin >> s;
		SET(dp);
		n = s.size();
		cout << "Case #" << i+1 << ": " << solve(0,0,0) << endl;
	}
	return 0;
}
