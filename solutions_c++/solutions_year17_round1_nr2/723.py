#include <bits/stdc++.h>

using namespace std;

int T, N, P;
int R[100], Q[100][100], vis[100][100];
priority_queue <int, vector<int>, greater<int> > q;

struct Node {
	int l, r;
	Node(int _l = 0, int _r = 0) {
		l = _l, r = _r;
	}
	int contains(int x) {
		return l <= x && x <= r;
	}
	bool operator < (const Node &b) const {
		return l < b.l || (l == b.l && r < b.r);
	}
} nd[100][100];

int main() {
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	cin >> T;
	for(int cas = 1; cas <= T; cas ++) {
		
		cin >> N >> P;
		for(int i = 0; i < N; i ++) {
			cin >> R[i];
		}
		for(int i = 0; i < N; i ++) {
			for(int j = 0; j < P; j ++) {
				cin >> Q[i][j];
			}
		}

		for(int j = 0; j < P; j ++) {
			for(int i = 0; i < N; i ++) {
				int r = floor(10.0*Q[i][j] / (9*R[i]));
				int l = ceil(10.0*Q[i][j] / (11*R[i]));
				if(l > r) {
					nd[i][j] = Node(-1, -1);
				} else {
					nd[i][j] = Node(l, r);
				}
			}
		}
		for(int i = 0; i < N; i ++) sort(nd[i], nd[i]+P);
		/*
		for(int i = 0; i < N; i ++) {
			for(int j = 0; j < P; j ++) cout << "(" << nd[i][j].l << "," << nd[i][j].r <<  ")";
			cout << endl;
		}
		*/
		int res = 0;
		memset(vis, 0, sizeof(vis));
		for(int i = 0; i < N; i ++) {
			for(int j = 0; j < P; j ++) {
				if(nd[i][j].l != -1) {
					q.push(nd[i][j].l);
				}
			}
		}
		while(!q.empty()) {
			int x = q.top(); q.pop();
			int ok = 1;
			for(int i = 0; i < N; i ++) {
				int exists = 0;
				for(int j = 0; j < P; j ++) {
					if(!vis[i][j] && nd[i][j].contains(x)) {
						exists = 1;
						break;
					}	
				}
				if(!exists) {
					ok = 0;
				}
			}
			
			if(!ok) continue;
			for(int i = 0; i < N; i ++) {
				for(int j = 0; j < P; j ++) {
					if(!vis[i][j] && nd[i][j].contains(x)) {
						vis[i][j] = 1;
						break;
					}	
				}
			}
			res ++;
		}
		cout << "Case #" << cas << ": " << res << endl;
	}
	
	return 0;
}

