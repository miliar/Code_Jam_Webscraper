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


long double square(const pll& pancake) {
	return (long double)M_PI * sqr(pancake.first);
}

long double side_area(const pll& pancake) {
	return  (long double)2.0 * M_PI * pancake.first * pancake.second;
}

long double stupid(const vector<pll>& pancakes, int k) {
	const int n = pancakes.size();
	long double ans = 0;
	cerr << fixed << setprecision(16);
	for (int mask = 0; mask < (1 << n); ++mask) {
		if (popcount(mask) != k) {
			continue;
		}
		long double area = 0;
		for (int i = 0, cnt = 0; i < n; ++i) {
			if ((mask & (1 << i)) == 0) {
				continue;
			}
			area += side_area(pancakes[i]);
			++cnt;
			if (cnt == k) {
				area += square(pancakes[i]);
			}
		}
		umax(ans, area);
	}
	return ans;
}

struct Cmp {
	bool operator()(const pll& lhs, const pll& rhs) const {
		return side_area(rhs) - side_area(lhs) > EPS;
	}
};

void solve(std::istream& in, std::ostream& out) {
	in >> __;
	for (int _ = 0; _ < __; ++_) {
		out << "Case #" << _ + 1 << ": ";
		int n, k;
		in >> n >> k;
		vector<pll> pancakes(n);
		in >> pancakes;
		sort(pancakes);

		// long double jans = stupid(pancakes, k);

		long double area = 0;

		multiset<pll, Cmp> stack;
		long double total_side_area = 0;
		int xx = 0;
		for (const auto& it : pancakes) {
			const long double side = side_area(it);
			long double total_side = 0;
			for (auto iter = stack.begin(); iter != stack.end(); ++iter) {
				total_side += side_area(*iter);
			}
			long double cur = total_side + side;
			cur += square(it);
			umax(area, cur);
			/* if (xx < 2) {
			cerr << endl << total_side_area << endl;
			cerr << value(it) << endl;
			cerr << area << endl << endl;
			}
			++xx; */
			if (stack.size() < k - 1) {
				stack.emplace(it);
				total_side_area += side;
			}
			else if (!stack.empty() && side_area(*stack.begin()) < side) {
				total_side_area -= side_area(*stack.begin());
				stack.erase(stack.begin());
				stack.emplace(it);
				total_side_area += side;
			}
		}

		/* if (abs(area - jans) > EPS) {
			cerr << fixed << setprecision(16) << _ + 1 << " WTF " << jans << " " << area << endl;
		} */

		out << fixed << setprecision(16) << area << endl;
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

