#include <bits/stdc++.h>

using namespace std;

int T, N, P, G, S, res, a[5], zero[5];

struct Node {
	int a[5], l;
	Node(int *b, int r) {
		for(int i = 1; i < P; i ++) {
			a[i] = b[i];
		}
		l = r;
	}
	bool operator < (const Node &b) const {
		if(l != b.l) return l < b.l;
		for(int i = 1; i < P; i ++) {
			if(a[i] != b.a[i]) return a[i] < b.a[i];
		}
		return 0;
	}
};

map <Node, int> dp;

int DP(Node cur) {
	if(dp.count(cur)) {
		return dp[cur];
	}
	int best = 0;
	for(int i = 1; i < P; i ++) {
		Node tmp = cur;
		if(cur.a[i] < a[i]) {
			tmp.a[i] ++;
			tmp.l = (tmp.l-i+P) % P;
			if(tmp.l == 0) {
				best = max(best, DP(tmp)+1);
			} else {
				best = max(best, DP(tmp));
			}
		}
	}
	return dp[cur] = best;
}

int main() {
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	cin >> T;
	for(int cas = 1; cas <= T; cas ++) {
		cin >> N >> P;
		
		S = 0;
		memset(a, 0, sizeof(a));
		for(int i = 0; i < N; i ++) {
			cin >> G;
			S = (S+G) % P;
			a[G % P] ++;
		}
		
		dp.clear();
		dp[Node(a, 0)] = a[0];
		res = DP(Node(zero, S));
		cout << "Case #" << cas << ": " << res << endl;
	}

	return 0;
}

