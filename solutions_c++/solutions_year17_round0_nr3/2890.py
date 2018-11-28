#include <iostream>
#include <fstream>
#include <vector>
#include <set>
#include <assert.h>
#include <map>
#include <algorithm>

using namespace std;

long long get_next_right(vector<bool> &viz, long long pos) {
	while (viz[pos] == false) pos++;
	return pos;
}

pair<long long, long long> solve(long long n, long long k) {
	if (n == 1) return make_pair(0LL, 0LL);

	vector<bool> viz = vector<bool>(n+2);
	viz[0] = true;
	viz[n + 1] = true;

	auto best = make_pair(0LL, 0LL);
	long long best_pos = -1;
	for (long long i = 0; i < k; i++) {
		best = make_pair(0LL, 0LL);
		long long last = 0, right = -1;
		for (int i = 1; i <= n; i++) {
			if (viz[i]) last = i;
			else {
				if (i >= right) {
					right = get_next_right(viz, i + 1);
				}
				auto result = make_pair(i - last - 1, right - i - 1);
				auto mmresult = make_pair(min(result.first, result.second), max(result.first, result.second));

				if (mmresult > best) {
					best = mmresult;
					best_pos = i;
				}
			}
		}

		if (best_pos == -1) {
			cerr << n << ' ' << k << '\n';
			assert(best_pos != -1);
		}
		viz[best_pos] = true;
	}

	return best;
}

pair<long long, long long> divide(long long nr) {
	if (nr & 1LL) return{ nr >> 1, nr >> 1 };
	else return{ (nr >> 1) - 1, nr >> 1 };
}

pair<long long, long long> solve_big(long long n, long long k) {
	map<long long, long long> mp;
	mp[n] = 1LL;
	long long level = 1, sum = 0;
	for (auto nr : mp) {
		if (nr.first > 0)
			sum += nr.second;
	}

	vector<pair<long long, long long> > v;
	while (k > sum) {
		k -= sum;
		for (auto nr : mp) {
			v.push_back({nr.first, nr.second});
		}
		mp.clear();
		for (auto elm : v) {
			auto mid = divide(elm.first);
			mp[mid.first] += elm.second;
			mp[mid.second] += elm.second;
		}
		v.clear();

		sum = 0;
		for (auto nr : mp) {
			if (nr.first > 0)
				sum += nr.second;
		}
		level++;
	}

	for (auto nr : mp) {
		if (nr.first > 0)
			v.push_back({ nr.first, nr.second });
	}



	if (k <= v.back ().second) {
		return divide(v.back().first);
	}
	else {
		return divide(v[0].first);
	}
}

#define TESTS 0

int main() {
	ios_base::sync_with_stdio(false);
	ifstream fin("C-large.in");
	ofstream fout("t33.out");
	int t;
	long long n, k;

	if (TESTS) {
		for (int i = 2; i <= 300; i++) {
			for (int k = 1; k <= i; k++) {
				assert(solve(i, k) == solve_big(i, k));
				cerr << "Test (" << i << ", " << k << ") passed\n";
			}
		}
	}

	fin >> t;
	for (int i = 0; i < t; i++) {
		fin >> n >> k;
		auto result = solve_big(n, k);
		fout << "Case #" << i + 1 << ": " << result.second << ' ' << result.first << '\n';
	}

	return 0;
}