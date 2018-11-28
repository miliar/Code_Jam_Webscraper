#include <bits/stdc++.h>

using namespace std;


pair<int64_t, int64_t> solve1(int64_t N, int64_t K) {
	multiset<pair<int64_t, int>> S = {make_pair(N, 0)};
	vector<int> locs;
	int64_t l, r;
	for (int k = 0; k < K; ++k) {

		auto it = S.end();
		--it;
		auto best = *it;
		S.erase(it);

		int64_t mid = best.first/2;
		// cout << mid << endl;
		locs.push_back(best.second+mid);
		l = best.first/2 - !(best.first%2);
		r = best.first/2;
		S.emplace(l, best.second);
		S.emplace(r, best.second+mid+1);
	}
	locs.push_back(-1);
	locs.push_back(N);
	sort(locs.begin(), locs.end());
	// for (int64_t loc : locs) {
	// 	cout << loc << " ";
	// }
	// cout << endl;
	return make_pair(max(l, r), min(l, r));
}

map<pair<int64_t, int>, map<pair<int64_t, int64_t>, int64_t>> DP;

map<pair<int64_t, int64_t>, int64_t> f(int64_t depth, int64_t sz) {
	if (depth == 1) {
		if (sz/2 - !(sz%2) < 0) {
			return {};
		}
		return {{{sz/2, sz/2 - !(sz%2)}, 1}};
	}
	auto key = make_pair(depth, sz);
	if (DP.count(key))
		return DP[key];
	auto a = f(depth-1, sz/2);
	auto b = f(depth-1, sz/2 - !(sz%2));
	for (auto &kv : b) {
		a[kv.first] += kv.second;
	}
	return DP[key] = a;
}

pair<int64_t, int64_t> solve2(int64_t N, int64_t K) {
	int64_t depth = 1, tmp = K, p = 1;
	while (tmp > 1) {
		++depth;
		tmp /= 2;
		p *= 2;
	}
	int64_t rem = K - p + 1;
	int64_t l, r;
	auto m = f(depth, N);
	while (rem > 0) {
		auto it  = m.end();
		--it;
		rem -= it->second;
		l = it->first.first;
		r = it->first.second;
		m.erase(it);
	}
	return {l, r};
}

void test() {
	default_random_engine re;
	for (int tc = 0; tc < 100000; ++tc) {
		int64_t N = (long long)re()%100000ll + (long long)1;
		int64_t K = (long long)re()%N + (long long)1;
		auto a = solve1(N, K);
		auto b = solve2(N, K);
		assert(a == b);
		cout << tc << " " << a.first << " " << a.second << endl;
	}
}

void solve() {
	int64_t N, K;
	cin >> N >> K;
	auto p = solve2(N, K);
	cout << p.first << " " << p.second << endl;
}

int main() {
	// test();
	// return 0;
	ios::sync_with_stdio(0);
	cin.tie(0);
	int T;
	cin >> T;
	for (int t = 0; t < T; ++t) {
		cout << "Case #" << (t+1) << ": ";
		solve();
	}
}