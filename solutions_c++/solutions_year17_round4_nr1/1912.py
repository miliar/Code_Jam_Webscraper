#include <bits/stdc++.h>
using namespace std;

const int N = 1e2 + 5;

#define st first
#define nd second

typedef pair<int,int> pun;
typedef long long ll;

int dp[5][5][N][N][N];

const int M = 100;

int policz(int p, int sum, int i, int j, int k) {
	return (sum+p-1)/p;
}

int test() {
	int n, p;
	scanf("%d%d", &n, &p);
	int ile[4];
	int sum = 0;
	ile[0] = ile[1] = ile[2] = ile[3] = 0;
	for (int i = 0; i < n; i ++) {
		int a;
		scanf("%d", &a);
		ile[a % p] ++;
		sum += a % p;
	}
//	printf("dp %d 0 %d %d %d\n", p, ile[1], ile[2], ile[3], dp[p][0][ile[1]][ile[2]][ile[3]]);
	return n -  dp[p][0][ile[1]][ile[2]][ile[3]];
}

void print_test() {
	auto v = test();
	printf("%d", v);
}

int jeden3(int x) {
	return x - (x+2)/3;
}

int dwa3(int x) {
	if (x >= 3) return dwa3(x % 3) + x/3;
	return 0;
}

int licz(int p, int left, int i, int j, int k) {
	if (p == 2) {
		if (left == 1 && i > 0) return licz(p, 0, i-1, j, k) + 1;
		return i / 2;
	}
	if (p == 3) {
		if (min(i, j) > 0) return min(i, j) + licz(p, left, i - min(i,j), j - min(i,j), k);
		if (left == 1 && i > 0) return licz(p, 0, i-1, j, k) + 1;
		if (left == 1 && j == 1) return 0;
		if (left == 1 && j > 0) return licz(p, 2, 0, j - 1, k);
		if (left == 2 && j > 0) return licz(p, 0, i, j - 1, k) + 1;
		if (left == 2 && i > 0) return licz(p, 1, i - 1, j, k) + 1;
		return jeden3(i) + dwa3(j);
	}
}

int main() {
	for (int p = 2; p <= 4; p ++)
		for (int i = 0; i <= M; i ++) {
			for (int j = 0; j <= M; j ++) {
				for (int k = 0; k <= M; k ++) {
					for (int left = 0; left < p; left ++) 
				{
					dp[p][left][i][j][k] = i + j + k;
					if (i + j + k == 0) {
						dp[p][left][i][j][k] = 0;
					}
					//zjedz nowa czekoladke
					if (left == 0) {
					if (i > 0) {
						dp[p][left][i][j][k] = min(dp[p][left][i][j][k], dp[p][p - 1][i-1][j][k]);
					}
					if (p > 2 && j > 0) {
						dp[p][left][i][j][k] = min(dp[p][left][i][j][k], dp[p][p - 2][i][j-1][k]);
					}
					if (p > 3 && k > 0) {
						dp[p][left][i][j][k] = min(dp[p][left][i][j][k], dp[p][p - 3][i][j][k-1]);
					}
					}
					else { 
						if (i > 0) {
						dp[p][left][i][j][k] = min(dp[p][left][i][j][k], dp[p][(left + p - 1)%p][i-1][j][k] + 1);
					}
					if (p > 2 && j > 0) {
						dp[p][left][i][j][k] = min(dp[p][left][i][j][k], dp[p][(left + p - 2)%p][i][j-1][k] + 1);
					}
					if (p > 3 && k > 0) {
						dp[p][left][i][j][k] = min(dp[p][left][i][j][k], dp[p][(left - p - 3)%p][i][j][k-1] + 1);
					}
					}
//					if (k == 0)
//					printf("d %d %d %d %d %d -- %d\n", p, left, i, j, k, dp[p][left][i][j][k]);
				}
			}
		}
	}
	int t;
	scanf("%d",&t);
	for (int i=1;i<=t;i++) {
		printf("Case #%d: ",i);
		print_test();
		printf("\n");
	}
}
