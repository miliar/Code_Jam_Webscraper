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

// namespace std

#include <iterator>

using namespace std;

int __;

void solve(std::istream& in, std::ostream& out) {
	in >> __;
	for (int _ = 0; _ < __; ++_) {
		out << "Case #" << _ + 1 << ": ";
		string s;
		int k;
		in >> s >> k;
		int ans = 0;
		bool bad = false;
		for (int i = 0; i <= s.length() - k; ++i) {
			if (s[i] == '-') {
				++ans;
				for (int j = 0; j < k; ++j) {
					s[i + j] = (s[i + j] == '-' ? '+' : '-');
				}
			}
		}
		for (int i = s.length() - k + 1; i < s.length(); ++i) {
			if (s[i] == '-') {
				bad = true;
			}
		}
		if (bad) {
			out << "IMPOSSIBLE" << endl;
			continue;
		}
		out << ans << endl;
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

