#include <bits/stdc++.h>
using namespace std;

vector< pair<int, int> > a, b;

int gao(vector< pair<int, int> > &x) {
	if (x.size() == 1) return 2;
	sort(x.begin(), x.end());
	int t = x[1].second - x[0].first;
	int p = x[1].first - x[0].second;

	assert(t >= 0);
	assert(p >= 0);
	if (t <= 720 || p>= 720) return 2;
	else return 4;
}

int solve() {
	int c, j; 
	cin >> c >> j;
	a.resize(c);
	b.resize(j);
	for (int i = 0; i < c; i++)
		cin >> a[i].first >> a[i].second;
	for (int i = 0; i < j; i++)
		cin >> b[i].first >> b[i].second;

	if (c == 1 && j == 1) return 2;
	if (a.size() == 0) return gao(b);
	else return gao(a);
}

int main() {
	int T;
	cin >> T;
	for (int i = 1; i <= T; i++) {
		cout << "Case #" << i << ": ";
		cout << solve() << endl;
	}
	return 0;
}

