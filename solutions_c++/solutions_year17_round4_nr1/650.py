#include <bits/stdc++.h>

#define FI(i,a,b) for(int i=(a);i<=(b);i++)
#define FD(i,a,b) for(int i=(a);i>=(b);i--)

#define LL long long
#define Ldouble long double
#define PI 3.1415926535897932384626

#define PII pair<int,int>
#define PLL pair<LL,LL>
#define mp make_pair
#define fi first
#define se second

using namespace std;

void fileIO(char in_name[20], char out_name[20]){
	char name[20];
	sprintf(name, "%s.in", in_name);
	freopen(name, "r", stdin);
	sprintf(name, "%s.out", out_name);
	freopen(name, "w", stdout);
}

int t, n, gp, cnt[4];

int ans, dp[105][105][105][4];

int f(int a, int b, int c, int cur){
	if(a + b + c == 0) return dp[a][b][c][cur] = 0;
	else if(dp[a][b][c][cur] != -1) return dp[a][b][c][cur];
	int ret = 0;
	if(a > 0) ret = max(ret, f(a - 1, b, c, (cur + 1) % gp));
	if(b > 0) ret = max(ret, f(a, b - 1, c, (cur + 2) % gp));
	if(c > 0) ret = max(ret, f(a, b, c - 1, (cur + 3) % gp));
	return dp[a][b][c][cur] = ret + (cur == 0);
}

void solve(){
	FI(i, 0, cnt[1]) FI(j, 0, cnt[2]) FI(k, 0, cnt[3]){
		FI(l, 0, gp - 1) dp[i][j][k][l] = -1;
	}
	ans = cnt[0] + f(cnt[1], cnt[2], cnt[3], 0);
	printf("%d\n", ans);
}

int main(){
	fileIO("A-large", "A2");
	scanf("%d", &t);
	FI(i, 1, t){
		printf("Case #%d: ", i);
		scanf("%d %d", &n, &gp);
		FI(j, 0, 3) cnt[j] = 0;
		FI(j, 1, n){
			int x;
			scanf("%d", &x);
			cnt[x % gp]++;
		}
		solve();
	}
	return 0;
}

