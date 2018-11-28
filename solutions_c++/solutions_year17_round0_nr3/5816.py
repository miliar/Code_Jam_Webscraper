#include <bits/stdc++.h>

using namespace std;

typedef pair<int, int> pii;

class Comp {
private:
public:
	const bool operator () (const pii &X, const pii &Y) const {
		int len1 = X.second-X.first, len2 = Y.second-Y.first;
		if (len1 != len2) return len1 < len2;
		return X > Y;
	}
};

int n, k;
priority_queue<pii, vector<pii>, Comp> PQ;

int main() {
	freopen("C-small-1-attempt0.in", "r", stdin);
	freopen("C-small-1-attempt0.out", "w", stdout);
	int nTests;
	cin >> nTests;
	for (int test = 1; test <= nTests; ++test) {
		cin >> n >> k;
		while (!PQ.empty()) PQ.pop();
		PQ.push(make_pair(1, n));
		int res1, res2;
		while (k--) {
			pii u = PQ.top();
			PQ.pop();
			int mid = (u.first+u.second)/2;
			res1 = mid-u.first;
			res2 = u.second-mid;
			if (u.first < mid) PQ.push(make_pair(u.first, mid-1));
			if (mid < u.second) PQ.push(make_pair(mid+1, u.second));
		}
		printf("Case #%d: %d %d\n", test, max(res1, res2), min(res1, res2));
	}
	return 0;
}