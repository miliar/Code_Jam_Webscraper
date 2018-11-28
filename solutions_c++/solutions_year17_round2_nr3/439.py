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

const ll inf = 1000000000LL * 1000000000LL;

struct test {
	int n;
	int q;
	vector<int> e;
	vector<int> s;
	vector<vector<ll>> d;
	vector<vector<long double>> t;
	vector<int> u;
	vector<int> v;
	vector<long double> ans;

	void read(istream& cin) {
		cin >> n >> q;
		e.resize(n);
		s.resize(n);
		d.resize(n);
		for (auto& v : d)
			v.resize(n);
		t.resize(n);
		for (auto& v : t)
			v.resize(n);
		u.resize(q);
		v.resize(q);

		for (int i = 0; i < n; ++i)
			cin >> e[i] >> s[i];
		for (int i = 0; i < n; ++i) {
			for (int j = 0; j < n; ++j) {
				cin >> d[i][j];
				if (d[i][j] == -1)
					d[i][j] = inf;
			}
			d[i][i] = 0;
		}
		for (int i = 0; i < q; ++i)
			cin >> u[i] >> v[i];
	}

	void solve() {
		for (int k = 0; k < n; ++k)
			for (int i = 0; i < n; ++i)
				for (int j = 0; j < n; ++j)
					d[i][j] = min(d[i][j], d[i][k] + d[k][j]);

		for (int i = 0; i < n; ++i)
			for (int j = 0; j < n; ++j)
				if (e[i] >= d[i][j])
					t[i][j] = (double)d[i][j] / s[i];
				else
					t[i][j] = inf;

		for (int k = 0; k < n; ++k)
			for (int i = 0; i < n; ++i)
				for (int j = 0; j < n; ++j)
					t[i][j] = min(t[i][j], t[i][k] + t[k][j]);

		for (int i = 0; i < q; ++i)
			ans.push_back(t[u[i] - 1][v[i] - 1]);
	}

	void write(ostream& cout) const {
		cout << setprecision(6) << fixed;
		for (auto d : ans)
			cout << d << ' ';
	}
};

void open_files() {
	freopen("C-large.in", "r", stdin);
	freopen("C-large.out", "w", stdout);
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
