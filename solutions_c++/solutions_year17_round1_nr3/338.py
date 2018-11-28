#include <cstring>
#include <iostream>
#include <algorithm>
using namespace std;
const int nmax = 100 + 2;

//int hp[nmax][nmax][nmax];
int T, hd, ad, hk, ak, b, d;
int qt, qh;
int q[10000000][5];
bool v[nmax][nmax][nmax][nmax];
int ans;

void insert(int i, int hd, int ad, int hk, int ak)
{
	if (hd < 0) hd = 0;
	if (hk < 0) hk = 0;
	if (ak < 0) ak = 0;
	if (hd > 100) hd = 100;
	if (ad > 100) ad = 100;
	if (hd <= 0 && hk > 0) return;
	if (v[hd][ad][hk][ak]) {
		return;
	}
	v[hd][ad][hk][ak] = 1;
	//printf("%d %d %d %d %d\n", i, hd, ad, hk, ak);
	++qt;
	q[qt][0] = i;
	q[qt][1] = hd;
	q[qt][2] = ad;
	q[qt][3] = hk;
	q[qt][4] = ak;
}

void work(int i, int nhd, int ad, int nhk, int ak)
{
	if (ans != -1 && i >= ans) return;
	if (nhk <= 0) {
		ans = i;
		return;
	}
	if (nhd <= 0) return;
	if (d > 0 && ak > 0)
		insert(i + 1, nhd - (ak - d), ad, nhk, ak - d);
	if (b > 0 && ad < 100)
		insert(i + 1, nhd - ak, ad + b, nhk, ak);
	insert(i + 1, nhd - ak, ad, nhk - ad, ak);
	insert(i + 1, hd - ak, ad, nhk, ak);
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	scanf("%d", &T);
	for (int cases = 1; cases <= T; ++cases) {
		scanf("%d%d%d%d%d%d", &hd, &ad, &hk, &ak, &b, &d);
		ans = -1;
		memset(v, 0, sizeof(v));
		qt = 0;
		
		insert(0, hd, ad, hk, ak);
		for (int i = 1; i <= qt; ++i) {
			work(q[i][0], q[i][1], q[i][2], q[i][3], q[i][4]);
			if (ans != -1) break;
		}
		printf("Case #%d: ", cases);
		if (ans != -1)
			printf("%d\n", ans);
		else
			printf("IMPOSSIBLE\n");
	}
	return 0;
}
