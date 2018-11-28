#include <iostream>
#include <sstream>
#include <vector>
#include <string>
#include <stack>
#include <queue>
#include <map>
#include <set>
#include <cfloat>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <climits>
#include <algorithm>
#include <unordered_map>
#include <unordered_set>

#define MOD 1000000007
#define PI 3.14159265359
#define REP(i,n) for(int i = 0; i < n; ++i)
#define FOR(i,n,m) for(int i = n; i < m; ++i)
#define LL long long

using namespace std;


void func(LL N, LL _k, LL &first, LL &second) {
	LL k = _k;
	while (k & (k-1)) { k &= (k-1); }
	int order = 0;
	while ((1L << order) != k) ++order;
	LL more, less, nm = 1, nl = 0;
	more = N;
	less = N-1;
	LL newnm = 1, newnl = 0;
	LL lastless = 0, lastmore = 0;
	while (order >= 0) {
		nm = newnm, nl = newnl;
		newnm = newnl = 0;
		if (more&1) newnm += nm << 1;
		else newnm += nm, newnl += nm;
		if (less&1) newnl += nl << 1;
		else newnm += nl, newnl += nl;

		//cout << more << " " << less << " " << nm << " " << nl << " " << newnm << " " << newnl << endl;
		lastmore = more;
		lastless = less;
		more = N >> 1;
		less = more - 1;
		N = more;
		--order;
	}
	//cout << _k << " " << k << " " << newnm << " " << lastmore << " " << lastless << endl;
	if (_k - k + 1 <= nm) first = lastmore>>1, second = lastmore-1-first;
	else first = lastless>>1, second = lastless-1-first;
}

int main() {
	int t;
	LL N, k;
	cin >> t;
	for (int i = 1; i <= t; ++i) {
		cin >> N;
		cin >> k;
		LL f, s;
		func(N, k, f, s);
		cout << "Case #" << i << ": " << f << " " << s << endl;
	}
	return 0;
}
