#include <bits/stdc++.h>
#define pb push_back
#define ep emplace_back
#define mt make_tuple
using namespace std;

int T;
long long n, k;

struct cmp {
	bool operator()(const tuple<long long, long long> &a, const tuple<long long, long long> &b) const {
		long long la, ra, lb, rb, ma, mb;
		tie(la, ra) = a;
		tie(lb, rb) = b;
		ma = la + ra >> 1;
		mb = lb + rb >> 1;
		if (min(ma - la, ra - ma) == min(mb - lb, rb - mb)) return max(ma - la, ra - ma) < max(mb - lb, rb - mb);
		return min(ma - la, ra - ma) < min(mb - lb, rb - mb);
	}
};

int main() {
	cin >> T;
	for (int tc = 0; tc < T; tc++) {
		cin >> n >> k;
		priority_queue<tuple<long long, long long>, vector<tuple<long long, long long>>, cmp> q;
		long long sz = 0;
		q.push(mt(0, n - 1));
		cout << "Case #" << tc + 1 << ": ";
		while (!q.empty()) {
			auto ft = q.top(); q.pop();
			sz++;
			long long l, r;
			tie(l, r) = ft;
			long long m = l + r >> 1;
			if (k == sz) {
				cout << max(m - l, r - m) << " " << min(m - l, r - m) << endl;
				break;
			}
			if (l <= m - 1) q.push(mt(l, m - 1));
			q.push(mt(m + 1, r));
		}
	}
	return 0;
}