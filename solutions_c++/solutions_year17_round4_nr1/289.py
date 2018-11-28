#include <bits/stdc++.h>
using namespace std;

int Test, N, P, ans;
int B[5];
int f[110][110][110][4];

int work(int x, int y, int z, int p){
	if (f[x][y][z][p] != -1)
		return f[x][y][z][p];
	f[x][y][z][p] = 0;
	int res;
	if (x){
		res = work(x - 1, y, z, (p - 1 + 4) % 4) + (!p);
		f[x][y][z][p] = max(f[x][y][z][p], res);
	}
	if (y){
		res = work(x, y - 1, z, (p - 2 + 4) % 4) + (!p);
		f[x][y][z][p] = max(f[x][y][z][p], res);
	}
	if (z){
		res = work(x, y, z - 1, (p - 3 + 4) % 4) + (!p);
		f[x][y][z][p] = max(f[x][y][z][p], res);
	}
	return f[x][y][z][p];
}

int main(){
//	freopen("A-large.in", "r", stdin);
//	freopen("A-large.out", "w", stdout);
	memset(f, 255, sizeof(f));
	scanf("%d", &Test);
	for (int tt = 1; tt <= Test; tt++){
		scanf("%d%d", &N, &P);
		memset(B, 0, sizeof(B));
		for (int i = 1; i <= N; i++){
			int x;
			scanf("%d", &x);
			B[x % P]++;
		}
		ans = 0;
		ans += B[0];
		B[0] = 0;
		if (P == 2){
			ans += (B[1] + 1) / 2;
			B[1] = 0;
		}
		else if (P == 3){
			int t = min(B[1], B[2]);
			ans += t;
			B[1] -= t;
			B[2] -= t;
			ans += (B[1] + 2) / 3;
			B[1] = 0;
			ans += (B[2] + 2) / 3;
			B[2] = 0;
		}
		else
			ans += work(B[1], B[2], B[3], 0);
		printf("Case #%d: %d\n", tt, ans);
	}
}
