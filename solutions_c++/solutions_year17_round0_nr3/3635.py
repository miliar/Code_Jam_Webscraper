#include <iostream>
#include <string.h>
#include <cstdio>
#include <set>
using namespace std;


void solve(int tst) {
	int N, K;
	cin >> N >> K;
	
	set<pair<int, int> > s;
	s.insert(make_pair(-N, 1));

	for (int i = 1; i <= K; ++i) {
		pair<int, int> p = *(s.begin());
		s.erase(s.begin());
		int n = -p.first;
		int lo = p.second;
		int hi = lo + n - 1;
		int mid = (lo + hi) / 2;
		if (lo < mid) {
			s.insert(make_pair(-(mid - lo), lo));
		}
		if (mid < hi) {
			s.insert(make_pair(-(hi - mid), mid + 1));	
		}
		if (i == K) {
			printf("Case #%d: %d %d\n", tst, hi - mid, mid - lo);		
		}
	}


	
}

int main() {
	freopen("input.txt", "r", stdin);
	int tst;
	cin >> tst;
	for (int i = 1; i <= tst; ++i) {
		solve(i);
	}
	return 0;
}