#include<cstdio>
#include<algorithm>
#include<cstring>
using namespace std;

const int NMAX = 101;
short dp[NMAX][NMAX][NMAX][NMAX][4];

int N, P;
short back2(int p0, int p1, int p2, int p3, int cur){
	short &ret = dp[p0][p1][p2][p3][cur];
	if (ret >= 0) return ret;

	ret = 0;

	if (p0 && 0 < P){
		int left = (cur + 0) % P;
		short sub = back2(p0 - 1, p1, p2, p3, left);
		if (cur == 0) sub++;
		ret = max(ret, sub);
	}
	if (p1 && 1 < P){
		int left = (cur + 1) % P;
		short sub = back2(p0, p1 - 1, p2, p3, left);
		if (cur == 0) sub++;
		ret = max(ret, sub);
	}
	if (p2 && 2 < P){
		int left = (cur + 2) % P;
		short sub = back2(p0, p1, p2 - 1, p3, left);
		if (cur == 0) sub++;
		ret = max(ret, sub);
	}
	if (p3 && 3 < P){
		int left = (cur + 3) % P;
		short sub = back2(p0, p1, p2, p3 - 1, left);
		if (cur == 0) sub++;
		ret = max(ret, sub);
	}
	return ret;
}

int main(){
	freopen("large.in", "r", stdin);
	freopen("large.out", "w", stdout);

	int T; scanf("%d", &T);
	for (int tc = 1; tc <= T; tc++){
		scanf("%d%d", &N, &P);
		memset(dp, -1, sizeof(dp));
		int p0 = 0, p1 = 0, p2 = 0, p3 = 0;
		for (int i = 0; i < N; i++){
			int g; scanf("%d", &g);
			g %= P;
			if (g == 0) p0++;
			else if (g == 1) p1++;
			else if (g == 2) p2++;
			else if (g == 3) p3++;
		}

		printf("Case #%d: %d\n", tc, (int)back2(p0, p1, p2, p3, 0));
	}
}