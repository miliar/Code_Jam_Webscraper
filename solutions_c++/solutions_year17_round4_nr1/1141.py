#include <cstdio>
#include <algorithm>
#include <cstring>

using namespace std;

int cho[105], r[5], n, p;
int dp[105][105][105][105];

int f(int rm, int r0, int r1, int r2, int r3) {
	if(r0 == 0 and r1 == 0 and r2 == 0 and r3 == 0) return 0;
	int &ret = dp[r0][r1][r2][r3];
	if(ret >= 0) return ret;
	ret = rm == 0? 1: 0;
	int t = 0;
	if(r0) t = max(t, f(rm, r0 - 1, r1, r2, r3));
	if(r1) t = max(t, f((rm + p - 1) % p, r0, r1 - 1, r2, r3));
	if(r2) t = max(t, f((rm + p - 2) % p, r0, r1, r2 - 1, r3));
	if(r3) t = max(t, f((rm + p - 3) % p, r0, r1, r2, r3 - 1));
	ret += t;
	return ret;
}

void sol() {
	memset(r, 0, sizeof r);
	memset(dp, -1, sizeof dp);
	scanf("%d%d", &n, &p);
	for(int i = 0;i < n;i++) scanf("%d", &cho[i]), r[cho[i] % p]++;
	printf("%d\n", f(0, r[0], r[1], r[2], r[3]));
}

int main() {
	int t; scanf("%d", &t);
	for(int i = 1;i <= t;i++) printf("Case #%d: ", i), sol();
}
