#include <bits/stdtr1c++.h>

using namespace std;

typedef long long ll;
typedef pair<ll, ll> pii;

map<pii, pii> memo;
pii solve2(ll n, ll k) {
	if (k == 0) return pii(n, n);
	if (k == 1) return pii(n/2, (n-1)/2);
	if (memo.count(pii(n,k))) return memo[pii(n,k)];
	
	//pii s0 = solve2(n/2, k/2), s1 = solve2((n-1)/2, (k-1)/2);
	//return pii(min(s0.first, s1.first), min(s0.second, s1.second));
	if (k % 2 == 0) return solve2(n/2, k/2);
	else return solve2((n-1)/2, (k-1)/2);
}

pii solve(ll n, ll k) {
	pii ans;
	vector<int> occ(n+2);
	occ[0] = occ[n+1] = 1;
	for (int l = 0; l < k; l++) {
		int best = -1, bestL = -1, bestR = -1;
		for (int i = 1; i <= n; i++) {
			int ls = 0, rs = 0;
			while (!occ[i+ls]) ls++;
			while (!occ[i-rs]) rs++;
			ls--, rs--;
			if (min(ls, rs) > min(bestL, bestR)) {
				best = i;
				bestL = ls;
				bestR = rs;
			} else if (min(ls, rs) == min(bestL, bestR)) {
				if (max(ls, rs) > max(bestL, bestR)) {
					best = i;
					bestL = ls;
					bestR = rs;
				}
			}
		}
		occ[best] = true;
		ans = pii(bestL, bestR);
	}
	return ans;
}

int main() {
    ios::sync_with_stdio(0);
    int t; cin >> t;
    for (int ca = 1; ca <= t; ca++) {
        cout << "Case #" << ca << ": ";
		
		ll n, k; cin >> n >> k;
		//cout << solve(n, k).first << " " << solve(n, k).second << endl;
		cout << solve2(n, k).first << " " << solve2(n, k).second << endl;
    }
	return 0;
}