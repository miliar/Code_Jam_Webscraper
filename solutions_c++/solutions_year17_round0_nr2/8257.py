#include <iostream>
#include <map>
#include <vector>
#include <set>
#include <algorithm>
#include <functional>
#include <cstdio>
#include <string>
#include <cmath>
using namespace std;

#define FOR(i,a,b)	for(int i=(a);i<(b);++i)
#define mp make_pair
#define pb push_back

typedef long long ll, int64;

int num_digs(ll n) {
	int cnt = 0;
	while (n > 0) {
		n /= 10;
		cnt++;
	}
	return cnt;
}


vector<int> make_vec(ll n) {
	vector<int> v;
	while (n > 0) {
		v.insert(v.begin(), n % 10);
		n /= 10;
	}
	return v;
}


ll tidy_leq(ll num) {	//find # tidy numbers x, 1 <= x <= num
	if (num == 0) {
		return 0;
	}
	int n_digs = num_digs(num);
	vector<int> n_vec = make_vec(num);
	vector<ll> dp_hit(n_digs, 0);
	vector<vector<ll> > dp_less(n_digs, vector<ll>(10, 0));
	
	// dp_eq[0] = 1;
	FOR (dig, 1, n_vec[0]) dp_less[0][dig] = 1;
	dp_hit[0] = 1;

	bool reversal_seen = false;
	FOR (pos, 1, n_digs) {
		FOR (dig, 0, 10) {
			if (dig > 0) dp_less[pos][dig] += 1; //starting something here (had leading 0's before)
			FOR (prev, 0, dig+1) { //0 <= prev <= dig
				dp_less[pos][dig] += dp_less[pos-1][prev];

			}
			if (dig < n_vec[pos] && dig >= n_vec[pos-1]) {
				dp_less[pos][dig] += dp_hit[pos-1];
			}
		}
		if (n_vec[pos] >= n_vec[pos-1]) {
			dp_hit[pos] = dp_hit[pos-1];
		}

	}

	ll ans = dp_hit[n_digs-1];
	FOR (dig, 0, 10) {
		ans += dp_less[n_digs-1][dig];
	}

	return ans;
}


ll tidy_range(ll a, ll b) {
	return tidy_leq(b) - tidy_leq(a - 1);
}


ll b_search(ll hi) {
	ll lo = 1;
	while (lo < hi) {
		ll mid = lo + (hi - lo + 1) / 2;
		ll v = tidy_range(mid, hi);
		if (v > 0) {
			lo = mid;
		}
		else {
			hi = mid - 1;
		}
	}
	return lo;
}


int main(void) {
	int nc;
	ll n;
	cin >> nc;
	FOR (cs, 1, nc + 1) {
		cin >> n;
		cout << "Case #" << cs << ": " << b_search(n) << endl;
	}
}