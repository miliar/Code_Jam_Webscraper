//Template
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <algorithm>
#include <climits>
#include <cmath>
#include <utility>
#include <set>
#include <map>
#include <queue>
#include <ios>
#include <iomanip>
#include <ctime>
#include <numeric>
#include <functional>
#include <fstream>
#include <string>
#include <vector>
#include <bitset>
#include <cstdarg>
#include <complex>
#include <cassert>
using namespace std;

typedef long long ll;
typedef unsigned int uint;
typedef unsigned long long ull;
typedef long double ld;
#define pair(x, y) make_pair(x, y)
#define runtime() ((double)clock() / CLOCKS_PER_SEC)

inline int read() {
	static int r, sign;
	static char c;
	r = 0, sign = 1;
	do c = getchar(); while (c != '-' && (c < '0' || c > '9'));
	if (c == '-') sign = -1, c = getchar();
	while (c >= '0' && c <= '9') r = r * 10 + (int)(c - '0'), c = getchar();
	return sign * r;
}

template <typename T>
inline void print(T *a, int n) {
	for (int i = 1; i < n; ++i) cout << a[i] << " ";
	cout << a[n] << endl;
}
#define PRINT(_l, _r, _s, _t) { cout << #_l #_s "~" #_t #_r ": "; for (int _i = _s; _i != _t; ++_i) cout << _l _i _r << " "; cout << endl; }

ll f[20][10][2];
bool valid[20][10][2];

int main(int argc, char *argv[]) {
#ifdef KANARI
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
	
	int T, Case = 0;
	ll n;
	cin >> T;
	while (T--) {
		cin >> n;
		int len = 0, num[19];
		while (n > 0) {
			num[++len] = n % 10;
			n /= 10;
		}
		int prefix = 1;
		for (int i = len - 1; i > 0; --i) {
			if (num[i] >= num[i + 1]) ++prefix;
			else break;
		}
		cout << "Case #" << ++Case << ": ";
		if (prefix < len) {
			int same = 0;
			for (int i = len - prefix + 1; i <= len; ++i) {
				if (num[len - prefix + 1] == num[i]) ++same;
				else break;
			}
			--num[len - prefix + same];
			for (int i = 1; i < same; ++i)
				num[len - prefix + i] = 9;
			for (int i = len - prefix; i > 0; --i)
				num[i] = 9;
		}
		while (num[len] == 0) --len;
		for (int i = len; i > 0; --i)
			cout << num[i];
		cout << endl;
	}

	fclose(stdin);
	fclose(stdout);
	return 0;
}
