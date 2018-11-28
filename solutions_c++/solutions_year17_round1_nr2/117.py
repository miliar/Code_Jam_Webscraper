#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <string>
#include <algorithm>
#include <map>
#include <set>
#include <queue>

using namespace std;

typedef long long ll;

const int MAXN = 55;
const int MAXP = 55;

int N, P;

ll R[MAXN];
ll Q[MAXN][MAXP];
int cur[MAXN];

int can(int ingred, ll q, ll num) {
	if (q * 10 < num * R[ingred] * 9) return -1; // too small
	if (q * 10 > num * R[ingred] * 11) return 1; // too big
	return 0;
}

int main() {
	int T;
	cin >> T;
	for (int t=1;t<=T;t++) {
		cin >> N >> P;
		for (int i=0;i<N;i++) cin>>R[i];
		for (int i=0;i<N;i++) {
			for(int j=0;j<P;j++) cin >> Q[i][j];
			sort(Q[i], Q[i]+P);
		}
		for (int i=0;i<N;i++) cur[i] = 0;
		int ans = 0;

		int c = 1;
		bool done = false;
		while (1) {
			if (c > 1000000) break;
			for (int i=0;i<N;i++) {
				while (cur[i] < P && can(i, Q[i][cur[i]], c) == -1) cur[i]++;
			}
			bool good = true;
			for (int i=0;i<N;i++) {
				if (cur[i] >= P) {
					done = true;
					break;
				}
				int x = can(i,Q[i][cur[i]],c);
				if (x != 0) {
					good = false;
					break;
				}
			}
			//printf("%d %d\n", c, ans);
			if (done) break;

			if (!good) c++;
			else {
				ans++;
				for (int i=0;i<N;i++) cur[i]++;
			}
		}

		printf("Case #%d: %d\n", t, ans);
		/*for (int i=0;i<N;i++) {
			for(int j=0;j<P;j++) printf("%lld ", Q[i][j]);
			printf("\n");
		}*/
	}
}