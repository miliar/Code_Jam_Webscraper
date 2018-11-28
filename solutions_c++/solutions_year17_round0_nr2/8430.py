#include <bits/stdc++.h>

using namespace std;

typedef unsigned long long ull;

ull n;
int T;
vector < ull > v;

void rec(int last, ull cur, int num) {
	v.push_back(cur);
	if (num == 19)
		return;
	for (int i = last; i <= 9; i++)
		if (cur * 10 + i <= (ull)1e18)
			rec(i, cur * 10 + i, num + 1);
}

int main() {
	freopen("b.in", "r", stdin);
	freopen("b.out", "w", stdout);

	for (int i = 1; i <= 9; i++)
		rec(i, i, 1);

	sort(v.begin(), v.end());

	cin >> T;

	int sz = (int)v.size();

	for (int t = 1; t <= T; t++) {
		cin >> n;
		int l = 0, r = sz - 1, cur;
		while (l <= r) {
			int mid = (l + r) >> 1;
			if (v[mid] <= n) {
				cur = mid;
				l = mid + 1;
			}
			else
				r = mid - 1;
		}
		cout << "Case #" << t << ": " << v[cur] << endl;
	}

	return 0;
}
