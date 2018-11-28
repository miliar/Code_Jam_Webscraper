#include<bits/stdc++.h>
#define rep(i,n)for(int i=0;i<(n);i++)
using namespace std;

int main() {
	int T; scanf("%d", &T);
	for (int Case = 1; Case <= T; Case++) {
		int n, r, o, y, g, b, v;
		cin >> n >> r >> o >> y >> g >> b >> v;
		vector<int>q;
		if (r < y) {
			int a = r + y;
			rep(i, a) {
				if (i % 2 == 1) {
					if (r) {
						r--; q.push_back(0);
					}
					else {
						y--; q.push_back(1);
					}
				}
				else {
					if (y) {
						y--; q.push_back(1);
					}
					else {
						r--; q.push_back(0);
					}
				}
			}
		}
		else {
			int a = r + y;
			rep(i, a) {
				if (i % 2 == 0) {
					if (r) {
						r--; q.push_back(0);
					}
					else {
						y--; q.push_back(1);
					}
				}
				else {
					if (y) {
						y--; q.push_back(1);
					}
					else {
						r--; q.push_back(0);
					}
				}
			}
		}
		bool flag = 0;
		if (q.size()&&q.front() == q.back() && b) {
			q.push_back(2); b--; flag = 1;
		}
		for (int i = q.size() - 1 - flag; i >= 0 && b; i--) {
			q.insert(q.begin() + i, 2); b--;
		}
		if (b) {
			printf("Case #%d: IMPOSSIBLE\n", Case);
			goto g;
		}
		rep(i, q.size()) {
			if (q[i] == q[(i + 1) % q.size()]) {
				printf("Case #%d: IMPOSSIBLE\n", Case);
				goto g;
			}
		}
		printf("Case #%d: ", Case);
		rep(i, q.size()) {
			if (q[i] == 0)printf("R");
			else if (q[i] == 1)printf("Y");
			else printf("B");
		}
		printf("\n");
	g:;
	}
}