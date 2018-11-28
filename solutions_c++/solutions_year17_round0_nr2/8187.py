#pragma comment(linker, "/STACK:66777216")
#pragma warning(disable : 4996)

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

#include <cstdint>

#ifdef _MSC_VER
#include <intrin.h>

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

// namespace std

#include <iterator>

using namespace std;

int __;

bool is_tidy(const std::string& s) {
	for (int i = 1; i < s.length(); ++i) {
		if (s[i] < s[i - 1]) {
			return false;
		}
	}
	return true;
}

std::string change(const ll x, const int shift) {
	std::string tmp = std::to_string(x);
	if (shift == 0) {
		return tmp;
	}
	for (int i = 0; i < shift; ++i) {
		tmp[tmp.length() - 1 - i] = '0';
	}
	ll y = std::stoll(tmp) - 1;
	return std::to_string(y);
}

void solve(std::istream& in, std::ostream& out) {
	in >> __;
	for (int _ = 0; _ < __; ++_) {
		out << "Case #" << _ + 1 << ": ";
		ll x;
		in >> x;
		int len = std::to_string(x).length();
		ll mx = -1;
		for (int i = 0; i < len; ++i) {
			string y = change(x, i);
			if (is_tidy(y)) {
				umax(mx, std::stoll(y));
				break;
			}
		}
		if (mx == -1) {
			out << "WTF" << endl;
		}
		else {
			out << mx << endl;
		}
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

