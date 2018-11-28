#include <bits/stdc++.h>

using namespace std;

#define FOR(i,a,b) for(int i = (a); i <= (b); ++i)
#define FORD(i,a,b) for(int i = (a); i >= (b); --i)
#define RI(i,n) FOR(i,1,(n))
#define REP(i,n) FOR(i,0,(n)-1)
#define mini(a,b) a=min(a,b)
#define maxi(a,b) a=max(a,b)
#define mp make_pair
#define pb push_back
#define st first
#define nd second
#define sz(w) (int) w.size()
typedef vector<int> vi;
typedef long long ll;
typedef long double ld;
typedef pair<int,int> pii;
typedef pair<pii, int> para;
const int inf = 1e9 + 7;
const int maxN = 1e2 + 9;

int n, p, arr[maxN], cnt[maxN], t;
int dp[maxN][maxN][maxN];

int solve(int a, int b, int c) {
	int ans = 0;

	if (dp[a][b][c] != -1)
		return dp[a][b][c];

	if (a >= 1 && c >= 1) ans = max(ans, 1 + solve(a - 1, b, c - 1));

	if (b >= 2) ans = max(ans, 1 + solve(a, b - 2, c));

	if (a >= 2 && b >= 1) ans = max(ans, 1 + solve(a - 2, b - 1, c));

	if (a >= 4) ans = max(ans, 1 + solve(a - 4, b - 1, c));

	if (b >= 1 && c >= 2) ans = max(ans, 1 + solve(a, b - 1, c - 2));

	if (c >= 4) ans = max(ans, 1 + solve(a, b, c - 4));

	if (ans == 0 && a + b + c != 0) ans++;
	dp[a][b][c] = ans;
	return ans;
}

int main() {
	ios_base::sync_with_stdio(0);
	cin>>t;
	RI(x, t) {
		cin>>n>>p;
		REP(i, n) cin>>arr[i];

		REP(i, 6) cnt[i] = 0;
		int ans = 0;
		if (p == 2) {
			int odd = 0;
			REP(i, n) {
				if (arr[i] % 2 == 0) ans++;
				else odd++;
			}
			ans += ((odd + 1)/ 2);
		}

		if (p == 3) {
			REP(i, n) {
				if (arr[i] % 3 == 0) ans++;
				else cnt[arr[i] % 3]++;
			}

			while (cnt[1] != 0 && cnt[2] != 0) {
				cnt[1]--; cnt[2]--;
				ans++;
			}

			while (cnt[1] > 0) {
				cnt[1] -= 3;
				ans++;
			}

			while (cnt[2] > 0) {
				cnt[2] -= 3;
				ans++;
			}

		}

		if (p == 4) {
			REP(i, n)
				if (arr[i] % 4 == 0) ans++;
				else cnt[arr[i] % 4]++;

			REP(i, 101) {
				REP(j, 101) {
					REP(k, 101) {
						dp[i][j][k] = -1;
					}
				}
			}
			ans += solve(cnt[1], cnt[2], cnt[3]);
		}
		cout<<"Case #"<<x<<": ";
		cout<<ans<<endl;
	}
	return 0;
}
