#include <iostream>
#include <algorithm>
#include <utility>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <cmath>
#include <string>
#include <cstring>
#include <cstdio>
#include <cassert>
using namespace std;

#define REP(i, n) for (int i = 0; i < (int)(n); i++)

void openFiles() {
#ifndef ONLINE_JUDGE
	freopen("C-small-2-attempt0.in", "rt", stdin);
	freopen("C-small-2-attempt0.out", "wt", stdout);
	//freopen("test.out", "wt", stdout);
#endif
}

typedef pair<int, int> pii;

template <class T, class U>
ostream& operator<<(ostream& os, const pair<T, U>& p) {
	os << "[" << p.first << ", " << p.second << "]";
	return os;
}

template <class T>
ostream& operator<<(ostream& os, const set<T>& s) {
	os << "[";
	for (typename set<T>::const_iterator ii = s.begin(); ii != s.end(); ++ii)
		os << " " << *ii;
	os << " ]";
    return os;
}
               
void solve() {
	int n, k; scanf("%d %d ", &n, &k);	

	set<pii> s;
	s.insert(pii(-n, 0));
	int mn, mx = 0;
	REP(i, k) {
		pii p = *s.begin();
		p.first = -p.first;
		s.erase(s.begin());
		int put = p.second + (p.first + 1) / 2;
		int d1 = (p.first - 1) / 2;
		int d2 = p.first / 2;
		mn = min(d1, d2), mx = max(d1, d2);
		if (p.first > 2) {
			s.insert(pii(-d1, p.second));
		}
		if (p.first > 1) {
			s.insert(pii(-d2, put));
		}
	}
	printf("%d %d\n", mx, mn);
}

int main() {
    openFiles();
    int n; scanf("%d ", &n);
    for (int i = 0; i < n; i++) {
    	cerr << i << endl;
        printf("Case #%d: ", i + 1);
        solve();
    }
    return 0;
}
