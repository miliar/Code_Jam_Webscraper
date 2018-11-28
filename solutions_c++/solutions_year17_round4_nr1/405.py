#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

int gP[4];

bool used4[222][222][222];
int f4[222][222][222]; // f[1][2][3]
int left4[222][222][222];

bool used3[222][222];
int f3[222][222]; // f[1][2][3]
int left3[222][222];

int _f4(int i, int j, int k){

	if (i < 0 || j < 0 || k < 0)
		return 0;
	if (used4[i][j][k] == 1)
		return f4[i][j][k];
	int ans = 0;
	bool left = true;
	// 4 = 1+1+1+1
	//   = 2+1+1
	//   = 3+1
	//   = 2+2
	//   = 3+2+3
	//   = 3+3+3+3

	if (i >= 4) {
		int r = _f4(i-4,j,k) + 1;
		if (r > ans){
			ans = r;
			left = left4[i-4][j][k];
		}
	}
	if (j >= 2) {
		int r = _f4(i,j-2,k) + 1;
		if (r > ans){
			ans = r;
			left = left4[i][j-2][k];
		}
	}
	if (j >= 1 && i >= 2) {
		int r = _f4(i-2,j-1,k) + 1;
		if (r > ans){
			ans = r;
			left = left4[i-2][j-1][k];
		}
	}
	if (k >= 1 && i >= 1) {
		int r = _f4(i-1,j,k-1) + 1;
		if (r > ans){
			ans = r;
			left = left4[i-1][j][k-1];
		}
	}
	if (k >= 2 && j >= 1) {
		int r = _f4(i,j-1,k-2) + 1;
		if (r > ans){
			ans = r;
			left = left4[i][j-1][k-2];
		}
	}
	if (k>=4) {
		int r = _f4(i,j,k-4) + 1;
		if (r > ans){
			ans = r;
			left = left4[i][j][k-4];
		}
	}
	f4[i][j][k] = ans;
	used4[i][j][k] = true;
	left4[i][j][k] = left;
	return ans;
}

int _f3(int i, int j){
	if (i < 0 || j < 0)
		return 0;
	if (used3[i][j] == 1)
		return f3[i][j];
	int ans = 0;

	// 3 = 1+1+1
	// 3 = 1+2
	// 3 = 2+2+2
	bool left = true;
	if (i >= 3) {
		int r = _f3(i-3,j) + 1;
		if (r > ans){
			ans = r;
			left = left3[i-3][j];
		}
	}
	if (i >= 1 && j >= 1) {
		int r = _f3(i-1,j-1) + 1;
		if (r > ans){
			ans = r;
			left = left3[i-1][j-1];
		}
	}
	if (j >= 3) {
		int r = _f3(i,j-3) + 1;
		if (r > ans){
			ans = r;
			left = left3[i][j-3];
		}
	}
	f3[i][j] = ans;
	used3[i][j] = true;
	left3[i][j] = left;
	return ans;
}
void work(){
	memset(gP,0,sizeof(gP));

	int N, P; scanf("%d%d", &N, &P);
	int tot = 0;
	for (int i = 0; i < N; i++) {
		int g;
		scanf("%d", &g);
		g %= P;
		gP[g]++;
		if (g == 0) tot++;
	}
	// mods = 1,2,3,...,p-1
	// assert 1 ==> need (p-1)
	// f3(2, 1)
	if (P == 2){
		tot += gP[1]/2 + gP[1] % 2;
	} else if (P==4) {
		tot += _f4(gP[1], gP[2], gP[3]);
		tot += left4[gP[1]][gP[2]][gP[3]];
	}
	else if (P == 3) {
		tot += _f3(gP[1], gP[2]);
		tot += left3[gP[1]][gP[2]];
	}

	printf("%d\n", tot);
}

int main(){
	freopen("A.in", "r", stdin);
	memset(used4, 0, sizeof(used4));
	memset(f4,0,sizeof(f4));
	memset(used3, 0, sizeof(used3));
	memset(f3,0,sizeof(f3));
	f4[0][0][0] = 0;
	used4[0][0][0] = 1;
	left4[0][0][0] = 0;
	f3[0][0] = 0;
	used3[0][0] = 1;
	left3[0][0] = 0;
	int Tc; scanf("%d", &Tc);
	for (int T = 1; T <= Tc; T++){
		printf("Case #%d: ", T);
		work();
	}
}