#include <iostream>
#include <cstdio>
#include <queue>
#include <utility>
#include <map>

typedef long long ll;

using namespace std;

//priority_queue<ll> pq;
map<ll, ll, std::greater<ll>> m;
ll count, N, K;

//pair<int, int> solve() {
//	ll left, right;
//	while (count < K) {
//		ll tmp = pq.top();
//		pq.pop();
//		left = (tmp - 1) / 2;
//		right = tmp - 1 - left;
//		if (left) pq.push(left);
//		if (right) pq.push(right);
//		++count;
//	}
//	return make_pair(left, right);
//}
//
pair<ll, ll> solve() {
	ll left, right;
	ll tmp = K;
	while (tmp > 0) {
		//for (auto i : m) cout << i.first << ":" << i.second << "|";
		//cout << endl;
		ll c, dist;
		auto top = m.begin();
		c = top->second;
		dist = top->first;
		m.erase(top);
		left = (dist - 1) / 2;
		right = dist - 1 - left;
		if (m.find(left) == m.end()) m[left] = 0;
		if (m.find(right) == m.end()) m[right] = 0;
		m[left] += c;
		m[right] += c;
		tmp -= c;
	}
	return make_pair(left, right);
}

int main() {
	freopen("C-large.in", "r", stdin);
	int T;
	cin >> T;
	for (int i=0; i<T; ++i) {
		//pq = priority_queue<ll>();
		m.clear();
		count = 0;
		cin >> N >> K;
		//pq.push(N);
		m[N] = 1;
		pair<ll, ll> res = solve();
		printf("Case #%d: %lld %lld\n", i+1, res.second, res.first);
	}

	return 0;
}
