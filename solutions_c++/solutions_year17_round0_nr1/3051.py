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
int k;

int solve(string s) {
	int n = s.size(), ans = 0;
	for (int i = n-1; i>=k-1; --i) if (s[i]=='-') {
		++ans;
		FOR(j,i-k+1, i+1) s[j] = (s[j]== '+' ? '-' : '+');
	}
	FOR0(i,n) if (s[i]=='-') return INF;
	return ans;
}

int main() {
	NSYNC;
	int t;
	cin >> t;
	FOR0(i,t) {
		string s;
		cin >> s;
		cin >> k;
		int ans = solve(s);
		reverse(all(s));
		ans = min(ans, solve(s));
		cout << "Case #" << i+1 << ": ";
		if (ans==INF) cout << "IMPOSSIBLE" << endl;
		else cout << ans << endl;
	}
	return 0;
}
