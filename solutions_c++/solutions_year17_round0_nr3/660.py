#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <queue>
#include <bitset>
#include <complex>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <limits>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <gmpxx.h>

using namespace std;

#define forn(i, n) for (int i = 0; i < (n); ++i)
#define foreach(it, a) for (__typeof((a).begin()) it = (a).begin(); it != (a).end(); ++it)

template<typename T> inline void ignore(T) {
}

typedef pair<int, int> score_t;

score_t compute_score(int m) {
	return make_pair(m / 2, (m-1)/2);
}

pair<int, int> solve(int n, int k) {
	priority_queue<int> q;
	q.push(n);
	while (k--) {
		n = q.top();
		q.pop();
		q.push(n/2);
		q.push((n-1)/2);
	}
	return compute_score(n);
}

int main(void) {
	int t; cin >> t;
	forn(i, t) {
		int n, k; cin >> n >> k;
		pair<int, int> ab = solve(n, k);
		cout << "Case #" << (i+1) << ": " << ab.first << ' ' << ab.second << endl;
	}
	return 0;
}
