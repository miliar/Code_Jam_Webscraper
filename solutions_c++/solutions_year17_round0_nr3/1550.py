#include <bits/stdc++.h>
using namespace std;

int T;
long long N, K;
int cas = 0;
typedef long long ll;
map<ll, ll> Move(const map<ll, ll>& m) {
	map<ll, ll> res;
	for(auto it = m.begin(); it != m.end(); it++) {
		long long val = it->first, cnt = it->second;
		if((val - 1) & 1) {
			res[(val - 1) / 2] += cnt;
			res[(val - 1) / 2 + 1] += cnt;
		} else {
			res[(val - 1) / 2] += cnt * 2;
		}
	}
	return res;
}
long long Count(const map<ll, ll>& m) {
	long long res = 0;
	for(auto it = m.begin(); it != m.end(); it++) {
		res += it->second;
	}
	return res;
}
long long CountLarge(const map<ll, ll>& m) {
	auto it = m.end();
	it--;
	return it->second;
}
int main() {
	freopen("./in.txt", "r", stdin);
	freopen("./out.txt", "w", stdout);
	cin >> T;
	while(T--) {
		printf("Case #%d: ", ++cas);
		cin >> N >> K;
		map<ll, ll> m;
		m[N] = 1;
		long long ansmax, ansmin;
		while(true) {
			long long c = Count(m);
			long long cl = CountLarge(m);
			if(K > c) {
				K -= c;
				m = Move(m);
			} else if(K > cl) {
				auto it = m.begin();
				long long val = it->first;
				long long cnt = it->second;
				ansmax = (val - 1) / 2 + ((val - 1) % 2);
				ansmin = (val - 1) / 2;
				break;
			} else {
				auto it = m.end();
				it--;
				long long val = it->first;
				long long cnt = it->second;
				ansmax = (val - 1) / 2 + ((val - 1) % 2);
				ansmin = (val - 1) / 2;
				break;
			}
		}
		cout << ansmax << " " << ansmin << endl;
	}
	return 0;
}
