#include <iostream>
#include <string>
#include <vector>
#include <set>
#include <algorithm>
#include <tuple>
#include <cassert>

using namespace std;
typedef long long ll_t;
struct Interval {
	ll_t left, right;
	Interval(ll_t l_ = 0, ll_t r_ = 0) : left(l_), right(r_) {}
	ll_t length() const {
		return right - left;
	}
	ll_t mid() const {
		return left + ((right - left) >> 1);
	}
	tuple<ll_t, ll_t> get_metric() const {
		ll_t m = mid();
		ll_t Ls = m - left - 1;
		ll_t Rs = right - m - 1;
		return make_tuple(Ls, Rs);
	}
};

ll_t log2_floor(ll_t N) {
	int res = 0;
	N >>= 1;
	while (N != 0) {
		++res;
		N >>= 1;
	}
	return res;
}

int main()
{
	int T;
	string str;
	cin >> T;
	getline(cin, str);
	ll_t N, K;
	for (int t = 1; t <= T; ++t) {
		cin >> N >> K;
		ll_t len = N;
		if (K > 1) {
			ll_t K1_level = log2_floor(K);
			ll_t prev_nodes = (1LL << K1_level) - 1;
			ll_t rest_K = K - prev_nodes;
			len = (N - prev_nodes) / (prev_nodes + 1);
			if ((K - prev_nodes) <= (N - prev_nodes) % (prev_nodes + 1))
				++len;
		}
		Interval i3(1, 2 + len);
		auto res2 = i3.get_metric();
		ll_t max2 = max(get<0>(res2), get<1>(res2));
		ll_t min2 = min(get<0>(res2), get<1>(res2));
		cout << "Case #" << t << ": " << max2 << ' ' << min2 << endl;
	}
	return 0;
}