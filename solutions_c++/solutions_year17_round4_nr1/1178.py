#include <bits/stdc++.h>
using namespace std;

short f[101][101][101][101];
int m[4];
int a,b,c,d;
int n, p;

short cal(int i, int j, int k, int t){
	//cout << i << " " << j << " " << k << " " << t << " ";	
	
	if (i < 0 || j < 0 || k < 0 || t < 0)
		return -1;
	
	if (i == 0 && j == 0 && k == 0 && t == 0)
		return 0;
	
	if (f[i][j][k][t] >= 0)
		return f[i][j][k][t];
	
	int cur = i*0 + j*1 + k*2 + t*3;
	cur = cur % p;
	
	int ii = 0, jj = 0, kk = 0, tt = 0;
	if (cur == 0) ii = 1;
	else if (cur == 1) jj = 1;
	else if (cur == 2) kk = 1;
	else tt = 1;
	
	
	f[i][j][k][t] = max(
		cal(i, j, k, t-1) + tt, max(
		cal(i, j, k-1, t) + kk, max(
		cal(i, j-1, k, t) + jj ,
		cal(i-1, j, k, t) + ii
	)));
	
	//cout << i << " " << j << " " << k << " " << t << " " << f[i][j][k][t] << endl;
	return (short) f[i][j][k][t];
		
}

void solve(){
	memset(m, 0, sizeof m);
	scanf("%d",&n);
	scanf("%d",&p);
	
	for(int i = 0; i < n; ++i){
		int g; scanf("%d",&g);
		g = g%p;
		m[g]++;
	}
	
	a = m[0], b = m[1], c = m[2], d = m[3];
	
	for(int i = 0; i <= a; ++i)
		for(int j = 0; j <= b; ++j)
			for(int k = 0; k <= c; ++k)
				for(int t = 0; t <= d; ++t)
					f[i][j][k][t] = -1;
				
	
	int result = cal(a, b, c, d);
	printf("%d\n", result);
	
}

int main(){
	freopen("file.out","w",stdout);
	
	int test; scanf("%d",&test);	
	for(int t = 1; t <= test; ++t){
		printf("Case #%d: ", t);
		solve();
	}
	
}