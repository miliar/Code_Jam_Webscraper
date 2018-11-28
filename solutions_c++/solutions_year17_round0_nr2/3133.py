#include <bits/stdtr1c++.h>

using namespace std;

typedef long long ll;

//(curr digit, below, last)
vector<ll> d, p10;
ll memo[20][3][15];
const ll inf = 1000000000000000000LL;
ll dp(int i, int below, int last) {
	if (last > d[i] && !below) return -inf;
	if (i == int(d.size())-1) {
		if (below) return 9;
		else return d[i];
	} else if (memo[i][below][last] != -1) {
		return memo[i][below][last];
	}
	
	ll& ans = memo[i][below][last] = -inf;
	for (int x = last; x <= (below ? 9 : d[i]); x++) {
		int nbelow = below;
		if (x < d[i]) nbelow = true;
		ans = max(ans, p10[i] * x + dp(i+1, nbelow, x));
	}
	return ans;
}

int main() {
    ios::sync_with_stdio(0);
    int t; cin >> t;
    for (int ca = 1; ca <= t; ca++) {
        cout << "Case #" << ca << ": ";
		memset(memo, -1, sizeof memo);
		
		d.clear();
		p10.clear();
		ll n; cin >> n;
		ll p = 1;
		while (n) {
			d.push_back(n%10);
			p10.push_back(p);
			p *= 10;
			n /= 10;
		}
		reverse(d.begin(), d.end());
		reverse(p10.begin(), p10.end());
		cout << dp(0, 0, 0) << endl;
    }
	return 0;
}