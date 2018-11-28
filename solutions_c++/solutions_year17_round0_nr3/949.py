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

void solve() {
	ll N, K;
	cin >> N >> K;
	priority_queue<ll> que;
	map<ll, ll> mp;
	que.push(N);
	mp[N] = 1;
	ll cnt = 0;
	while (!que.empty()) {
		ll n = que.top(); que.pop();
		ll t = mp[n];
		cnt += t;
		if (cnt >= K) {
			cout << n/2 << " " << (n-1)/2 << endl;
			break;
		}
		if (mp.find(n/2) == mp.end()) que.push(n/2);
		mp[n/2] += t;
		if (mp.find((n-1)/2) == mp.end()) que.push((n-1)/2);
		mp[(n-1)/2] += t;
	}
}

int main() {
	int T;
	cin >> T;
	for (int t = 1; t <= T; t++) {
		cout << "Case #" << t << ": ";
		solve();
	}
	return 0;
}