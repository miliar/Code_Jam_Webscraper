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

struct segment {
	int l, r, len;
	segment() {}
	segment(int _l, int _r) : l(_l), r(_r), len(_r - _l + 1) {}
	inline bool operator < (const segment &rhs) const {
		if (len != rhs.len) return len < rhs.len;
		return l > rhs.l;
	}
} ;
priority_queue<segment> q;

int main(int argc, char *argv[]) {
#ifdef KANARI
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
	
	int T, n, k, Case = 0;
	cin >> T;
	while (T--) {
		cin >> n >> k;
		while (!q.empty()) q.pop();
		q.push(segment(1, n));
		segment cur;
		int mid;
		while (k--) {
			cur = q.top();
			// cerr << cur.l << " " << cur.r << endl;
			q.pop();
			mid = (cur.l + cur.r) / 2;
			if (cur.l < mid) q.push(segment(cur.l, mid - 1));
			if (mid < cur.r) q.push(segment(mid + 1, cur.r));
		}
		int maxd = cur.r - mid, mind = mid - cur.l;
		cout << "Case #" << ++Case << ": " << maxd << " " << mind << endl;
		// break;
	}

	fclose(stdin);
	fclose(stdout);
	return 0;
}
