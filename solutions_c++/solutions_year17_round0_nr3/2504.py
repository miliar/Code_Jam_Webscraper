#include <algorithm>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <string>
#include <vector>
#include <cmath>
#include <queue>
#include <set>
#include <map>
using namespace std;
typedef long long ll;
typedef vector<ll> vl;
typedef vector<vl> vvl;

set<ll> gaps;
map<ll,ll> dp;

void add_gap(ll g) {
	if(g == 0) return;
	if(gaps.count(g)) return;
	gaps.insert(g);
	add_gap(g/2);
	add_gap((g-1)/2);
}

ll placed(ll gap, ll cap) {
	if(gap < cap) return 0;
	if(!dp.count(gap))
		dp[gap] = 1+placed(gap/2,cap)+placed((gap-1)/2,cap);
	return dp[gap];
}

vl cut,amt;

int main() {
	ios::sync_with_stdio(0); cin.tie();
	int T;
	cin >> T;
	for(int t = 1; t <= T; ++t) {
		ll n,k;
		cin >> n >> k;
		gaps.clear();
		add_gap(n);
		cut.clear();
		amt.clear();
		for(auto a : gaps) {
			dp.clear();
			cut.push_back(a);
			amt.push_back(placed(n,a));
		}
		for(int i = cut.size()-1; i >= 0; --i) {
			if(amt[i] >= k) {
				cout << "Case #" << t << ": " << (cut[i]/2) << " " << (cut[i]-1)/2 << "\n";
				break;
			}
		}
	}
	return 0;
}