#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

int getint() {
	char c = ' ';
	for(; c < '0' || c > '9'; c = getchar());
	int ret = 0;
	for(; c >= '0' && c <= '9'; c = getchar()) ret = ret * 10 + c - '0';
	return ret;
}

ll n, k;
map<ll, ll> segs;

void solve() {
	segs.clear();
	--k, segs[n] = 1;
	while(k) {
		auto pseg = segs.rbegin();
		ll len = pseg->first, number = pseg->second;
		ll t = min(number, k);
		k -= t, number -= t;
		ll l = (len - 1) >> 1, r = len >> 1;
		if(l) segs[l] += t;
		if(r) segs[r] += t;
		if(!number) segs.erase(len);
	}

	while(true) {
		auto pseg = segs.rbegin();
		ll len = pseg->first, number = pseg->second;
		segs.erase(len);
		if(!number) continue;
		ll l = (len - 1) >> 1, r = len >> 1;
		cout << r << ' ' << l << endl;
		break;
	}
}

int main() {
	for(int cases = getint(), idx = 1; idx <= cases; ++idx) {
		printf("Case #%d: ", idx);
		cin >> n >> k;
		solve();
	}
	return 0;
}

