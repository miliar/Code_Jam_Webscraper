#include <bits/stdc++.h>
#define endl '\n'
using namespace std;
typedef long long ll;
typedef long double ld;
typedef complex<ld> pt;
const int MOD = 1e9 + 7;
const int INF = 1e9;

template <class T> struct comp {
	bool operator() (const vector<int> &a, const vector<int> &b) const {
		if (a[0] == b[0])
			return a[1] > b[1];
		return a[0] < b[0];
	}
	typedef bool result_type;
};

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	int T; cin >> T;
	for (int t = 1; t <= T; t++) {
		int N, K; cin >> N >> K;
		priority_queue<vector<int>, vector<vector<int>>, comp<vector<int>>> pq; //{r - l, l, r}
		pq.push({N, 0, N});
		int curMin = (N-1) / 2, curMax = N / 2;
		for (int i = 0; i < K; i++) {
			vector<int> cur = pq.top(); pq.pop();
			int l1 = cur[1], r1 = (cur[1] + cur[2] - 1) / 2;
			int l2 = (cur[1] + cur[2] - 1) / 2 + 1, r2 = cur[2];
	//		cout << l1 << " " << r1 << " " << l2 << " " << r2 << endl;
			curMin = (cur[2] - cur[1] - 1) / 2;
			curMax = (cur[2] - cur[1]) / 2;
			pq.push({r1 - l1, l1, r1});
			pq.push({r2 - l2, l2, r2});
		}
		cout << "Case #" << t << ": " << curMax << " " << curMin << endl;
	}
	return 0;
}