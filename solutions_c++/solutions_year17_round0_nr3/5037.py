#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <limits.h>
#include <vector>
#include <stdlib.h>
#include <algorithm>
#include <memory.h>
#include <string.h>
#include <math.h>
#include <string>
#include <algorithm>
#include <functional>
#include <cassert>
#include <map>
#include <set>
#include <list>

using namespace std;
typedef long long lli;
typedef vector<int> vi;
typedef vector<lli> vli;
typedef pair<int, int> pii;
typedef vector<pii> vpii;
typedef long double ld;

const int INF = 0x3f3f3f3f;
const lli LINF = 0x3f3f3f3f3f3f3f3f;

//#define _LOCAL_DEBUG_
#ifdef _LOCAL_DEBUG_
#define eprintf(...) fprintf(stderr,__VA_ARGS__)
#else
#define eprintf(...) 
#endif

int n, k;
struct Segment {
	int l, len;
	const bool operator < (const Segment &s) const {
		return len == s.len ? l < s.l : len > s.len;
	}
};

void clear() {
}

void read(int t) {
	scanf("%d%d", &n, &k);
	set<Segment> s;
	s.insert({ 0, n });
	for (int i = 0; i < k; i++) {
		Segment seg = *s.begin();
		s.erase(s.begin());
		int pos = (seg.len - 1) / 2;
		if (pos > 0) s.insert({ seg.l, pos });
		if (pos < seg.len - 1) s.insert({ seg.l + pos + 1, seg.len - pos - 1 });
		int L = min(pos, seg.len - pos - 1), R = max(pos, seg.len - pos - 1);
		if(i == k - 1) printf("Case #%d: %d %d\n", t, R, L);
	}
}

int main() {
#ifdef _LOCAL_VAN
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
#endif
	int t;
	scanf("%d", &t);
	for (int it = 0; it < t; it++) {
		clear();
		read(it + 1);
	}
	return 0;
}