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
	int m;
	int er;
	vector<string> a;

	string ans;
	vector<string> b;

	vector<vector<int>> rght;
	vector<vector<int>> lft;
	vector<vector<int>> up;
	vector<vector<int>> dwn;

	void read(istream& cin) {
		cin >> n >> m;
		a.resize(n);
		for (auto& s : a)
			cin >> s;
		b = a;
	}

	int place_forced() {
		int i, j, ii, jj;
		bool can_v, can_h;
		for (i = 0; i < n; ++i)
			for (j = 0; j < m; ++j)
				if (b[i][j] == '.') {
					can_v = 0;
					can_h = 0;
					if (up[i][j] != -1 && b[up[i][j]][j] == '?')
						ii = up[i][j];
					else
						ii = dwn[i][j];
					if (ii >= 0 && b[ii][j] == '?')
						can_v = true;
					if (lft[i][j] != -1 && b[i][lft[i][j]] == '?')
						jj = lft[i][j];
					else
						jj = rght[i][j];
					
					if (jj >= 0 && b[i][jj] == '?')
						can_h = true;

					if (!can_h && !can_v)
						return 2;

					if (!can_h) {
						place(ii, j, '|');
					}
					else {
						place(i, jj, '-');
					}
					return 0;
				}
		return 1;
	}


	void place(int i, int j, char c) {
		b[i][j] = c;
		if (c == '|') {
			for (int ii = i - 1; ii >= 0 && b[ii][j] != '#'; --ii) {
				b[ii][j] = 'x';
				--er;
			}
			for (int ii = i + 1; ii < n && b[ii][j] != '#'; ++ii) {
				b[ii][j] = 'x';
				--er;
			}
		}
		else {
			for (int jj = j - 1; jj >= 0 && b[i][jj] != '#'; --jj) {
				b[i][jj] = 'x';
				--er;
			}
			for (int jj = j + 1; jj < m & b[i][jj] != '#'; ++jj) {
				b[i][jj] = 'x';
				--er;
			}
		}
	}

	void place_any() {
		for (int i = 0; i < n; ++i)
			for (int j = 0; j < m; ++j)
				if (b[i][j] == '?') {
					place(i, j, '-');
					return;
				}
	}

	void solve() {
		int i, j, ii, jj;
		bool p;
		string pos = "POSSIBLE";
		string impos = "IMPOSSIBLE";

		rght = vector<vector<int>>(n, vector<int>(m));
		lft = vector<vector<int>>(n, vector<int>(m));
		up = vector<vector<int>>(n, vector<int>(m));
		dwn = vector<vector<int>>(n, vector<int>(m));

		er = 0;
		for(i = 0; i < n; ++i)
			for (j = 0; j < m; ++j) {

				if (a[i][j] == '.') {
					er++;
					b[i][j] = '.';
				}
				else if (a[i][j] == '#')
					b[i][j] = '#';
				else
					b[i][j] = '?';
				for (ii = i - 1; ii >= 0; --ii)
					if (a[ii][j] != '.')
						break;
				up[i][j] = ii;
				for (ii = i + 1; ii < n; ++ii)
					if (a[ii][j] != '.')
						break;
				if (ii == n)
					ii = -1;
				dwn[i][j] = ii;
				for (jj = j - 1; jj >= 0; --jj)
					if (a[i][jj] != '.')
						break;
				lft[i][j] = jj;
				for (jj = j + 1; jj < m; ++jj)
					if (a[i][jj] != '.')
						break;
				if (jj == m)
					jj = -1;
				rght[i][j] = jj;
			}

		for (i = 0; i < n; ++i)
			for (j = 0; j < m; ++j) {
				if (b[i][j] == '?') {
					ii = up[i][j];
					if (ii >= 0 && b[ii][j] != '#')
						place(i, j, '-');
					ii = dwn[i][j];
					if (ii >= 0 && b[ii][j] != '#')
						place(i, j, '-');
					jj = lft[i][j];
					if (jj >= 0 && b[i][jj] != '#') {
						if (b[i][j] == '-') {
							ans = impos;
							return;
						}
						place(i, j, '|');
					}
					jj = rght[i][j];
					if (jj >= 0 && b[i][jj] != '#') {
						if (b[i][j] == '-') {
							ans = impos;
							return;
						}
						place(i, j, '|');
					}
				}
			}

		while (er) {
			int x = place_forced();
			if (x == 2) {
				ans = impos;
				return;
			}
			if (x == 1) {
				place_any();
			}
		}

		for (int i = 0; i < n; ++i)
			for (int j = 0; j < m; ++j)
				if (b[i][j] == '?')
					b[i][j] = '|';

		ans = pos;
		for (int i = 0; i < n; ++i)
			for (int j = 0; j < m; ++j)
			if (b[i][j] == 'x')
				b[i][j] = '.';
	}

	void write(ostream& cout) const {
		cout << ans << endl;
		if (ans == "POSSIBLE") {
			for (int i = 0; i < n; ++i)
				cout << b[i] << endl;
		}
	}
};

void open_files() {
	freopen("C-small-attempt1.in", "r", stdin);
	freopen("C-small-attempt1.out", "w", stdout);
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
		cout << "Case #" << i + 1 << ": " << tests[i];

	return 0;
}
