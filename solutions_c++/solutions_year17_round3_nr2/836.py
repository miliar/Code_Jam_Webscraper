#pragma comment(linker, "/STACK:66777216")
#pragma warning(disable : 4996)
#define _USE_MATH_DEFINES

#include <algorithm>
#include <array>
#include <bitset>
#include <cassert>
#include <chrono>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <functional>
#include <iomanip>
#include <iostream>
#include <limits>
#include <map>
#include <numeric>
#include <queue>
#include <random>
#include <set>
#include <sstream>
#include <string>
#include <type_traits>
#include <unordered_map>
#include <unordered_set>
#include <utility>
#include <vector>
#pragma hdrstop


static constexpr long double EPS = 1e-9;

#include <cstdint>

#ifdef _MSC_VER
#include <intrin.h>
#define popcount(a) __popcnt(a)

#else
#define popcount(a) __builtin_popcount(a)
#define clz(a) __builtin_clz(a)
#define ctz(a) __builtin_ctz(a)
#endif

template<typename T>
inline bool umax(T& a, const T& b) {
	return (a < b ? a = b, true : false);
}

#ifdef _MSC_VER

#endif

template<typename T, size_t N>
struct MakeVector {

};

template<typename T>
struct MakeVector<T, 1> {
	/// caide keep
	template<typename R = std::vector<T>>
	static R make_vector(std::size_t size, const T& value) {
		return R(size, value);
	}
};

#ifdef _MSC_VER

#else
#define LLD "%lld"
#define LLU "%llu"
#endif

#define ll long long

#define pii std::pair<int, int>
#define pll std::pair<ll, ll>

namespace std {

	template<typename T>
	std::istream& operator >> (std::istream& in, std::vector<T>& vec) {
		for (auto& it : vec) {
			in >> it;
		}
		return in;
	}

	template<typename T, typename U>
	std::istream& operator >> (std::istream& in, std::pair<T, U>& rhs) {
		in >> rhs.first >> rhs.second;
		return in;
	}

}  // namespace std

#include <iterator>

template<typename R>
void sort(R& range) {
	std::sort(range.begin(), range.end());
}

template<typename T>
constexpr inline T sqr(const T& x) {
	return x * x;
}

using namespace std;

int __;

bool check(const vector<pii>& a) {
	if (a.back().second - a.front().first <= 720 || a.back().first - a.front().second >= 720) {
		return false;
	}
	return true;
}

void solve(std::istream& in, std::ostream& out) {
	in >> __;
	for (int _ = 0; _ < __; ++_) {
		out << "Case #" << _ + 1 << ": ";
		int ac, aj;
		in >> ac >> aj;
		vector<pii> a(ac), j(aj);
		in >> a >> j;
		sort(a);
		sort(j);
		bool bad = false;
		if (ac == 2) {
			bad = check(a);
		}
		else if (aj == 2) {
			bad = check(j);
		}
		out << (bad ? 4 : 2) << endl;
	}
}

#include <fstream>

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	srand(time(NULL));

	ios_base::sync_with_stdio(0);
	cin.tie(0);

	istream& in = cin;

	ostream& out = cout;

	out << fixed << setprecision(16);
	solve(in, out);
	return 0;
}

