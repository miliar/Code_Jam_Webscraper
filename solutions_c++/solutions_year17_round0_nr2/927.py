#include<iostream>
#include<vector>
#include<string>
#include<cstring>
#include<algorithm>
#include<map>
#include<set>
#include<cmath>
#include<cassert>
#include<queue>

using namespace std;
typedef long long ll;
typedef unsigned long long ull;
typedef pair<int, int> pii;
typedef vector<int> vi;
struct cww{cww(){ios::sync_with_stdio(false);cin.tie(0);}}star;

string S;
ll dp[20][2][10]; // keta, smaller flag, prev
ll p10[20], p11[20];

ll dfs(int keta, int flag, int prev) {
	ll& ret = dp[keta][flag][prev];
	if (ret >= 0) return ret;
	int N = S.size();
	if (keta == N) return ret = 0;
	ret = 0;
	int digit = S[keta] - '0';
	for (int d = prev; d < 10; ++d) {
		if (!flag && d > digit) continue;
		int nflag = flag | (d < digit);
		ret = max(ret, p10[N-1-keta]*d + dfs(keta+1, nflag, d));
	}
	return ret;
}

void solve() {
	ll N;
	cin >> N;
	S = to_string(N);
	//memset(dp, -1, sizeof(dp));
	//cout << dfs(0, 0, 0) << endl;
	int len = S.size();
	ll ans = 0;
	for (int i = 0; i < len; i++) {
		int d = 0;
		for (d = 0; d < 10; ++d) {
			//cout << i << " " << d << ": " << ans*p10[len-i] + d*p11[len-i-1] << endl;
			if (ans*p10[len-i] + d*p11[len-i-1] <= N) continue;
			else break;
		}
		if (d == 10) --d;
		if (ans*p10[len-i] + d*p11[len-i-1] > N) --d;
		ans = ans*10 + d;
	}
	cout << ans << endl;
}

int main() {
	p10[0] = 1;
	for (int i = 1; i <= 18; i++) {
		p10[i] = p10[i-1]*10;
	}
	p11[0] = 1;
	for (int i = 1; i <= 18; i++) {
		p11[i] = p11[i-1]*10 + 1;
	}
	int T;
	cin >> T;
	for (int t = 1; t <= T; ++t) {
		cout << "Case #" << t << ": ";
		solve();
	}
	return 0;
}
