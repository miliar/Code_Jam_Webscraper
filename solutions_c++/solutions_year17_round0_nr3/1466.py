#include <iostream>
#include <chrono>
#include <vector>
#include <algorithm>
#include <cassert>
#include <cstdint>
#include <queue>
#include <functional>
#include <map>
#include <set>

using namespace std;

// #define DBG

int main(int argc, char** argv) {

	unsigned test_count; cin >> test_count;

	map<int64_t, int64_t> m;
	set<int64_t, greater<int64_t>> s;
	for (unsigned ti = 1; ti <= test_count; ++ti) {
		s.clear(), m.clear();
		int64_t N, K; cin >> N >> K;
#ifdef DBG
		cout << "Test " << ti << ": " << N << ' ' << K << endl;
#endif
		m[N] = 1; s.insert(N);
		int64_t l = 0, r = 0, processed = 0;
		while (processed < K) {
			int64_t v = *s.begin();
			int64_t cnt = m[v];
			s.erase(s.begin());
			m.erase(v);
			l = (v - 1) / 2;
			r = (v - 1) - l;
			s.insert(l), s.insert(r);
			m[l] += cnt, m[r] += cnt;
			processed += cnt;
#ifdef DBG
			cout << v << ' ' << cnt << ' ' << processed << endl;
#endif
		}

		cout << "Case #" << ti << ": " << r << ' ' << l << endl;
	}

	return 0;
}
