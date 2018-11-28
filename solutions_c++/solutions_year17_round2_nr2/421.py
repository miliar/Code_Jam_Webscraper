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
	int r;
	int o;
	int y;
	int g;
	int b;
	int v;
	string ans;

	void read(istream& cin) {
		cin >> n >> r >> o >> y >> g >> b >> v;
	}

	void solve() {
		int R = r - g;
		int Y = y - v;
		int B = b - o;
		string imp = "IMPOSSIBLE";
		ans = "";
		if (R < 0 || Y < 0 || B < 0)
			ans = imp;
		if (R == 0 && r != 0) {
			if (y || v || b || o)
				ans = imp;
			else
				for (int i = 0; i < r; ++i)
					ans += "RG";
			return;
		}
		if (Y == 0 && y != 0) {
			if (r || g || b || o)
				ans = imp;
			else
				for (int i = 0; i < y; ++i)
					ans += "YV";
			return;
		}
		if (B == 0 && b != 0) {
			if (r || g || y || v)
				ans = imp;
			else
				for (int i = 0; i < b; ++i)
					ans += "BO";
			return;
		}

		vector<pair<int, char>> w(3);
		w[0] = make_pair(R, 'R');
		w[1] = make_pair(Y, 'Y');
		w[2] = make_pair(B, 'B');
		sort(w.begin(), w.end());
		ans = string(w[2].first, w[2].second);
		int i, j;
		for (i = 0, j = 0; i < ans.size() && j < w[1].first; i++)
			if (ans[i] == w[2].second) {
				ans.insert(ans.begin() + i + 1, w[1].second);
				j++;
			}
		for (j = 0; i < ans.size() && j < w[0].first; i++)
			if (ans[i] == w[2].second) {
				ans.insert(ans.begin() + i + 1, w[0].second);
				j++;
			}
		if (*ans.begin() == *ans.rbegin()) {
			ans = imp;
			return;
		}
		for (i = 0; i < ans.size() && j < w[0].first; i++)
			if (ans[i] == w[2].second) {
				ans.insert(ans.begin() + i + 1, w[0].second);
				j++;
			}

		for (i = 0; i < ans.size(); ++i)
			if (ans[i] == 'R') {
				string is = "";
				for (j = 0; j < g; ++j)
					is += "GR";
				ans.insert(i + 1, is);
				break;
			}

		for (i = 0; i < ans.size(); ++i)
			if (ans[i] == 'Y') {
				string is = "";
				for (j = 0; j < v; ++j)
					is += "VY";
				ans.insert(i + 1, is);
				break;
			}

		for (i = 0; i < ans.size(); ++i)
			if (ans[i] == 'B') {
				string is = "";
				for (j = 0; j < o; ++j)
					is += "OB";
				ans.insert(i + 1, is);
				break;
			}

	}

	void write(ostream& cout) const {
		cout << ans;
	}
};

void open_files() {
	freopen("B-small-attempt0.in", "r", stdin);
	freopen("B-small-attempt0.out", "w", stdout);
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
