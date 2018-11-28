#include <bits/stdc++.h>
using namespace std;

#ifdef HELTHAZAR
	#define DEBUG true
#else
	#define DEBUG false
#endif

#define dout if (DEBUG) cout

struct interval {
	int l, r, index;
	interval() {}
	interval(int l, int r, int index) : l(l), r(r), index(index) {}
	bool operator < (interval &i) {
		return l < i.l;
	}
};

void solve() {
	vector<int> a(2);
	cin >> a[0] >> a[1];

	vector<interval> v;
	vector<int> rem = {720, 720};
	for (int i = 0; i < 2; i++) {
		for (int j = 0; j < a[i]; j++) {
			interval ival;
			cin >> ival.l >> ival.r;
			ival.index = i;
			rem[i] -= ival.r - ival.l;
			v.push_back(ival);
		}
	}

	sort(v.begin(), v.end());

	int cnt = 0;
	vector<int> between[2];
	for (int i = 0; i < v.size(); i++) {
		int j = i + 1;
		if (i == v.size() - 1) {
			j = 0;
			v[j].l += 1440;
		}
		if (v[i].index != v[j].index) {
			cnt++;
		}
		else {
			between[v[i].index].push_back(v[j].l - v[i].r);
			cnt += 2;
		}
	}

	for (int i = 0; i < 2; i++) {
		sort(between[i].begin(), between[i].end());
		for (int j = 0; j < between[i].size(); j++) {
			if (rem[i] - between[i][j] >= 0) {
				rem[i] -= between[i][j];
				cnt -= 2;
			}
		}
	}

	cout << cnt;
}

int main() {
	int test;
	cin >> test;

	for (int t = 1; t <= test; t++) {
		//printf("Case #%d: ", t);
		cout << "Case #" << t << ": ";

		solve();

		cout << endl;
		//printf("\n");
	}
}
