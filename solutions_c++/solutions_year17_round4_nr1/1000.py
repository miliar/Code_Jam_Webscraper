#include <bits/stdc++.h>
using namespace std;

const int INF = 1000000;

int N;
int P;

int modCnt[5];

int dp2[5][105];
int dp3[5][105][105];
int dp4[5][105][105][105];


// P = 2
int dfs2(int m, int a) {
	if (a > modCnt[1]) {
		return -INF;
	}
	if (dp2[m][a] != -1) {
		return dp2[m][a];
	}
	int x = dfs2((m-1+P)%P, a+1) + ((m==1) ? 1 : 0);
	int ans = x;
	dp2[m][a] = ans;
	return ans;
}

int solve2() {
	int a = modCnt[1];
	dp2[0][a] = modCnt[0];
	
	int m = (a) % P;
	
	return dfs2(m, 0);
}

// P = 3
int dfs3(int m, int a, int b) {
	//cout << "dfs3 " << m << " " << a << " " << b << endl;
	if (a > modCnt[1] || b > modCnt[2]) {
		return -INF;
	}
	if (dp3[m][a][b] != -1) {
		return dp3[m][a][b];
	}
	int x = dfs3((m-1+P)%P, a+1, b) + ((m==1) ? 1 : 0);
	int y = dfs3((m-2+P)%P, a, b+1) + ((m==2) ? 1 : 0);
	int ans = max(x, y);
	dp3[m][a][b] = ans;
	return ans;
}

int solve3() {
	int a = modCnt[1];
	int b = modCnt[2];
	dp3[0][a][b] = modCnt[0];
	
	int m = (a+2*b) % P;
	
	return dfs3(m, 0, 0);
}

// P = 4
int dfs4(int m, int a, int b, int c) {
	if (a > modCnt[1] || b > modCnt[2] || c > modCnt[3]) {
		return -INF;
	}
	if (dp4[m][a][b][c] != -1) {
		return dp4[m][a][b][c];
	}
	int x = dfs4((m-1+P)%P, a+1, b, c) + ((m==1) ? 1 : 0);
	int y = dfs4((m-2+P)%P, a, b+1, c) + ((m==2) ? 1 : 0);
	int z = dfs4((m-3+P)%P, a, b, c+1) + ((m==3) ? 1 : 0);
	int ans = max(x, max(y,z));
	dp4[m][a][b][c] = ans;
	return ans;
}

int solve4() {
	int a = modCnt[1];
	int b = modCnt[2];
	int c = modCnt[3];
	dp4[0][a][b][c] = modCnt[0];
	//dp[1][a][b][c] = -INF;
	//dp[2][a][b][c] = -INF;
	//dp[3][a][b][c] = -INF;
	
	int m = (a+2*b+3*c) % P;
	
	return dfs4(m, 0, 0, 0);
	
}

void init() {
	for (int p = 0; p < 4; p++) {
		for (int i = 0; i < 105; i++) {
			for (int j = 0; j < 105; j++) {
				for (int k = 0; k < 105; k++) {
					dp2[p][i] = -1;
					dp3[p][i][j] = -1;
					dp4[p][i][j][k] = -1;
				}
			}
		}
	}
}

int main() {
	int ncases;
	cin >> ncases;
	for (int icase = 1; icase <= ncases; icase++) {
		cin >> N >> P;
		
		//cout << "P = " << P << endl;
		
		for (int i = 0; i < P; i++) {
			modCnt[i] = 0;
		}
		
		for (int i = 0; i < N; i++) {
			int g;
			cin >> g;
			modCnt[g%P]++;
		}
		
		init();
		
		int ans;
		if (P == 2) {
			ans = solve2();
		} else if (P == 3) {
			ans = solve3();
		} else {
			assert(P == 4);
			ans = solve4();
		}
		cout << "Case #" << icase << ": " << ans << endl;
	}
	return 0;
}
