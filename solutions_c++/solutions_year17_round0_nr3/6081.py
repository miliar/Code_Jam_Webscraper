#include <bits/stdc++.h>
using namespace std;

#define pb push_back
#define mp make_pair

typedef long long ll;
typedef pair<int, int> pii;

struct cmp {
	bool operator()(pii a, pii b) {
		if (a.second - a.first != b.second - b.first)
			return a.second - a.first > b.second - b.first;
		return a.first < b.first;
	}
};

int T, n, k;
set<pii, cmp> q;

void load() {
	cin >> n >> k;
}

void solve(int tc) {
	cout << "Case #" << tc << ": ";
	q.insert(mp(1, n));
	for (int i = 1; i < k; ++i) {
		pii val = *q.begin();
		q.erase(q.begin());
		int l = val.first;
		int r = val.second;
		int mid = (l + r) / 2;
		if (l == mid && r == mid) {
		} else if (l == mid) {
			q.insert(mp(l + 1, r));
		} else if (r == mid) {
			q.insert(mp(l, r - 1));
		} else {
			q.insert(mp(l, mid - 1));
			q.insert(mp(mid + 1, r));
		}
	}
	pii val = *q.begin();
	int l = val.first;
	int r = val.second;
	r -= l; l = 0;
	cout << l + r - (l + r) / 2 << ' ' << (l + r) / 2 << '\n';
}

void clear() {
	q.clear();
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	cin >> T;
	for (int tc = 1; tc <= T; ++tc) {
		clog << tc << "/" << T << endl;
		load();
		solve(tc);
		clear();
	}
	return 0;
}
