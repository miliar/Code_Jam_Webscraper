#include <functional>
#include <algorithm>
#include <iostream>
#include <iomanip>
#include <numeric>
#include <sstream>
#include <cstdlib>
#include <cstring>
#include <vector>
#include <cstdio>
#include <string>
#include <thread>
#include <mutex>
#include <stack>
#include <queue>
#include <deque>
#include <cmath>
#include <map>
#include <set>
#include <unordered_map>
#include <unordered_set>

using namespace std;

typedef long long ll;
typedef unsigned long long ull;

#define USE_THREADS

// start coding here

struct test {

	int n;
	int p;
	vector<int> g;
	int ans;
	void read(istream& cin) {
		cin >> n >> p;
		g.resize(n);
		for (int& x : g)
			cin >> x;
	}

	void solve() {
		map<int, int> mp;
		for (int& x : g)
			mp[(p - x % p) % p]++;
		ans = mp[0];

		if (p == 2)
			ans += (mp[1] + 1) / 2;
		if (p == 3) {
			int mn = min(mp[1], mp[2]);
			ans += mn;
			mp[1] -= mn;
			mp[2] -= mn;
			if (mp[2])
				mp[1] = mp[2];
			if (mp[1])
				ans += (mp[1] + 2) / 3;
		}
		if (p == 4) {
			int mn = min(mp[1], mp[3]);
			ans += mn;
			mp[1] -= mn;
			mp[3] -= mn;
			ans += mp[2] / 2;
			mp[2] %= 2;

			if (mp[3])
				mp[1] = mp[3];
			if (mp[1]) {
				ans += mp[1] / 4;
				mp[1] %= 4;
				if (mp[2] && mp[1] >= 2) {
					++ans;
					mp[2] = 0;
					mp[1] -= 2;
				}
				if (mp[2] || mp[1])
					++ans;
			}
			else
				if (mp[2])
					++ans;
		}
	}

	void write(ostream& cout) const {
		cout << ans;
	}
};

void open_files() {
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
}

void precalc() {
}

// end coding here

istream& operator >> (istream& in, test& t) {
	t.read(in);
	return in;
}

ostream& operator << (ostream& out, const test& t) {
	t.write(out);
	return out;
}

mutex test_pick_lock;
size_t tests_count;
size_t next_test;

vector<test> tests;

void solver_thread_func() {
	while (1) {
		test* current_test_ptr = nullptr;

		test_pick_lock.lock();

		if (next_test < tests_count)
			current_test_ptr = &tests[next_test++];

		test_pick_lock.unlock();

		if (!current_test_ptr)
			break;

		current_test_ptr->solve();
	}
}

int main() {
	open_files();
	precalc();

	ios_base::sync_with_stdio(false);
	cin >> tests_count;
	tests.resize(tests_count);
	for (auto& t : tests)
		cin >> t;

#ifdef USE_THREADS
	vector<thread> thread_pool(thread::hardware_concurrency());

	for (auto& t : thread_pool)
		t = thread(solver_thread_func);

	for (auto& t : thread_pool)
		t.join();
#else
	for (auto& t : tests)
		t.solve();
#endif

	for (size_t i = 0; i < tests_count; ++i)
		cout << "Case #" << i + 1 << ": " << tests[i] << endl;

	return 0;
}
