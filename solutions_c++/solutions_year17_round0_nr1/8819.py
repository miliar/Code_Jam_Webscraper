// * template
#include <bits/stdc++.h>

#ifdef LOCAL
#include "dump.hpp"
#else
#define dump(...)
#endif

using namespace std;

template<class T> inline void chmax(T &a, const T &b) { if(a < b) a = b; }
template<class T> inline void chmin(T &a, const T &b) { if(a > b) a = b; }

template<class T, class U> inline void fill_array(T &e, const U &v) { e = v; }
template<class T, class U, size_t s> inline void fill_array(T (&a)[s], const U &v) {for(auto&e:a)fill_array(e,v);}
template<class T, class U, size_t s> inline void fill_array(array<T, s> &a, const U &v) {for(auto&e:a)fill_array(e,v);}
template<class T, class U> inline void fill_array(vector<T> &a, const U &v) {for(auto&e:a)fill_array(e,v);}

// * solve

class solver {
private:
	using Bit = bitset<1000>;
	int n;
	int k;
	Bit start;
	Bit goal;
	Bit mask;

	void init() {
		start.reset();
		goal.reset();
		mask.reset();
	}

public:
	void input() {
		init();
		string s;
		cin >> s >> k;
		n = s.size();
		for(int i = 0; i < n; ++i) {
			if(s[i] == '+') start.set(i);
			goal.set(i);
		}
		for(int i = 0; i < k; ++i) {
			mask.set(i);
		}
	}

	string solve() const {
		int ans = 0;
		Bit current = start;
		for(int i = 0; i <= n - k; ++i) {
			if(!current[i]) {
				current ^= mask << i;
				++ans;
			}
		}
		return (current & goal) == goal ? to_string(ans) : "IMPOSSIBLE";
	}
};

// * main

int main() {
	cin.tie(nullptr);
	ios::sync_with_stdio(false);

	int T;
	cin >> T;

#ifdef _OPENMP
	int next_index = 0;
	vector<decltype(solver().solve())> ans(T);

	#pragma omp parallel for
	for(int t = 0; t < T; ++t) {
		int index;
		solver s;

		#pragma omp critical
		{
			index = next_index++;
			s.input();
		}

		ans[index] = s.solve();
	}

	for(int t = 1; t <= T; ++t) {
		cout << "Case #" << t << ": " << ans[t - 1] << '\n';
	}

#else
	solver s;
	for(int t = 1; t <= T; ++t) {
		s.input();
		const auto ans = s.solve();
		cout << "Case #" << t << ": " << ans << '\n';
	}
#endif

	return EXIT_SUCCESS;
}
