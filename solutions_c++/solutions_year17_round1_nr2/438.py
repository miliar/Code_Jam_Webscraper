#include <bits/stdc++.h>
using namespace std;

struct Bound {
	int low, high, id;

	Bound(int _low, int _high, int _id) {
		low = max(1, _low);
		high = _high;
		id = _id;
	}
};

int ceil(int x, int y) {
	return (x + y - 1) / y;
}

int floor(int x, int y) {
	return x / y;
}

int run() {
	int n, p; cin >> n >> p;
	vector<int> base (n);
	for (int i = 0; i < n; ++i) cin >> base[i];
	vector<Bound> bounds;
	for (int i = 0; i < n; ++i) {
		for (int j = 0; j < p; ++j) {
			int pack; cin >> pack;
			Bound bound (ceil(10 * pack, 11 * base[i]), floor(10 * pack, 9 * base[i]), i);
			if (bound.low <= bound.high) bounds.push_back(bound);
		}
	}
	sort(bounds.begin(), bounds.end(),
			[] (const Bound &a, const Bound &b) {
				return a.low < b.low;
			});
	vector<priority_queue<int, vector<int>, greater<int>>> q (n);
	int nonZero = 0;
	auto push = [&] (priority_queue<int, vector<int>, greater<int>> &x, int y) {
		if (x.empty()) ++nonZero;
		x.push(y);
	};
	auto pop = [&] (priority_queue<int, vector<int>, greater<int>> &x) {
		int res = x.top();
		x.pop();
		if (x.empty()) --nonZero;
		return res;
	};
	int res = 0;
	for (int i = 0; i < (int) bounds.size(); ) {
		int j = i;
		while (j < (int) bounds.size() && bounds[i].low == bounds[j].low) {
			push(q[bounds[j].id], bounds[j].high);
			++j;
		}
		while (nonZero == n) {
			bool ok = true;
			for (int k = 0; k < n; ++k) {
				while (!q[k].empty() && q[k].top() < bounds[i].low)
					pop(q[k]);
				if (q[k].empty()) {
					ok = false;
					break;
				} else {
					pop(q[k]);
				}
			}
			if (ok) ++res;
			else assert(nonZero != n);
		}
		i = j;
	}
	return res;
}

int main() {
	ios::sync_with_stdio(false);
	int nt; cin >> nt;
	for (int tc = 1; tc <= nt; ++tc)
		cout << "Case #" << tc << ": " << run() << '\n';
	return 0;
}
