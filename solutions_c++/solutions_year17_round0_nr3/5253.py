#include <bits/stdc++.h>
using namespace std;

set<pair<int,int> > s;

void solve(int n, int k, int t_id) {
	s.clear();
	int L,R;
	s.insert(make_pair(-n, 1));
	for (int i = 0; i < k; i++) {
		pair<int,int> x = *s.begin();
		s.erase(s.begin());
		L = x.second;
		R = x.second + (-x.first) - 1;
		int m = (L+R)/2;
		s.insert(make_pair(-(m-L), L));
		s.insert(make_pair(-(R-m), m+1));
	}
	int ans1, ans2;
	int m = (L+R)/2;
	int d1 = m - L;
	int d2 = R - m;
	ans1 = min(d1, d2);
	ans2 = max(d1, d2);
	printf("Case #%d: %d %d\n", t_id, ans2, ans1);
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int t, n, k;
	cin>>t;
	for (int t_id = 1; t_id <= t; t_id++) {
		cin>>n>>k;
		solve(n, k, t_id);
	}

	return 0;
}
