#include <iostream>
#include <vector>
#include <random>
#include <array>
#include <cstdlib>
#include <cstring>
#include <map>

using namespace std;

#define forn(i, n) for(int i = 0; i < (n); ++i)
#define all(x) x.begin(), x.end()

template<typename T> int sz(const T& x) { return static_cast<int>(x.size()); }
template<typename T> void mx(T& x, const T& y) { x = std::max(x, y); }
template<typename T> void mn(T& x, const T& y) { x = std::min(x, y); }


struct State {
	std::array<uint8_t, 4> cnt;

	State() {
		cnt.fill(0);
	}

	bool is_zero() const {
		return std::max(all(cnt)) == 0;
	}
};

bool operator<(const State& a, const State& b) {
	return memcmp(&a, &b, sizeof(State)) < 0;
}

int n, p;

map<State, uint8_t> dp;

uint8_t DP(State state, int leftover) {
	auto res = dp.emplace(state, 0);
	if (!res.second) {
		return res.first->second;
	}

	forn (i, p) {
		if (state.cnt[i] > 0) {
			state.cnt[i]--;
			mx(res.first->second, DP(state, (leftover + p - i) % p));
			state.cnt[i]++;
		}
	}
	if (leftover == 0) {
		res.first->second++;
	}
	return res.first->second;
}

void solve() {
	cin >> n >> p;
	vector<int> g(n);
	State initial;
	forn (i, n) {
		cin >> g[i];
		initial.cnt[g[i] % p]++;
	}

	dp.clear();
	dp.emplace(State{}, 0);
	cout << (int) DP(initial, 0) << endl;
}

int main() {
  int t;
  cin >> t;
  forn (i, t) {
    cout << "Case #" << i + 1 << ": ";
    solve();
  }
  return 0;
}
