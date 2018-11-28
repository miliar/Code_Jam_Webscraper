#include <cstdio>
#include <iostream>
#include <cmath>
#include <algorithm>
#include <vector>
#include <queue>
#include <string>
#include <string.h>
#include <stdlib.h>

using namespace std;

int a[6];
bool f[105][105][105][105];

struct status {
	int hd, hk, ad, ak;
	long long int cnt;
};

status trans(int hd, int ad, int hk, int ak, long long int cnt) {
	status tmp;
	tmp.hd = hd;
	tmp.hk = hk;
	tmp.ad = ad;
	tmp.ak = ak;
	tmp.cnt = cnt;
	return tmp;
}

queue<status> q;

int main() {
	freopen("C-small-attempt0.in", "r", stdin);
	freopen("dragon.out", "w", stdout);
	int test; scanf("%d", &test);
	for(int t = 1; t <= test; t++) {
		printf("Case #%d: ", t);
		for(int i = 0; i < 6; i++) scanf("%d", &a[i]);
		for(int i = 0; i <= a[0]; i++) 
			for(int j = 1; j <= max(a[1], a[2]); j++)
				for(int k = 0; k <= a[2]; k++) 
					for(int l = 0; l <= a[3]; l++) f[i][j][k][l] = 0;
		while (!q.empty()) q.pop();
		q.push(trans(a[0], a[1], a[2], a[3], 0));
		f[a[0]][a[1]][a[2]][a[3]] = 1;
		long long int res = -1;
		while (!q.empty()) {
			status p = q.front();
			q.pop();
			// cout << p.hd << " " << p.ad << " " << p.hk << " " << p.ak << " " << p.cnt << endl;
			if (p.hd == 0) continue;
			int hd, hk, ad, ak;
			if (p.hd > 0 && p.hk == 0) {
				res = p.cnt;
				break;
			}
			if (p.hd < a[0]) {
				hd = p.hd; hk = p.hk; ad = p.ad; ak = p.ak;
				hd = max(0, a[0] - ak);
				if (!f[hd][ad][hk][ak]) {
					f[hd][ad][hk][ak] = 1;
					q.push(trans(hd, ad, hk, ak, p.cnt + 1));
				}
			}
			if (a[4] > 0 && p.ad < p.hk) {
				hd = p.hd; hk = p.hk; ad = p.ad; ak = p.ak;
				ad = min(a[2], ad + a[4]);
				hd = max(0, hd - ak);
				if (!f[hd][ad][hk][ak]) {
					f[hd][ad][hk][ak] = 1;
					q.push(trans(hd, ad, hk, ak, p.cnt + 1));
				}	
			}
			if (a[5] > 0 && p.ak > 0) {
				hd = p.hd; hk = p.hk; ad = p.ad; ak = p.ak;
				ak = max(0, ak - a[5]);
				hd = max(0, hd - ak);
				if (!f[hd][ad][hk][ak]) {
					f[hd][ad][hk][ak] = 1;
					q.push(trans(hd, ad, hk, ak, p.cnt + 1));
				}		
			}
			hd = p.hd; hk = p.hk; ad = p.ad; ak = p.ak;
			hk = max(0, hk - ad);
			if (hk > 0) hd = max(0, hd - ak);
			if (!f[hd][ad][hk][ak]) {
				f[hd][ad][hk][ak] = 1;
				q.push(trans(hd, ad, hk, ak, p.cnt + 1));
			}	
		}
		if (res == -1) printf("IMPOSSIBLE\n");
		else printf("%lld\n", res);
	}	
	fclose(stdin);
	fclose(stdout);
	return 0;
}