#include<bits/stdc++.h>
using namespace std;
#define pb push_back
#define mkp make_pair
#define fi first
#define se second
#define ll long long
#define M 1000000007
#define all(a) a.begin(), a.end()

int f[110][110][110], g[110][110];
int cnt[5];

inline void ckmin(int &a, int b){
	if(a > b) a = b;
}

int n, p;

int main(){
	freopen("A-large.in", "r", stdin);
	freopen("x.out", "w", stdout);
	int T, ca = 0;
	
	memset(f, 127, sizeof(f));
	f[0][0][0] = 0;
	for(int i = 0; i <= 100; ++i)
		for(int j = 0; j <= 100; ++j)
			for(int k = 0; k <= 100; ++k){
				if(f[i][j][k] > 1e9) continue;
				int l = (i + j * 2 + k * 3) % 4;
				ckmin(f[i + 1][j][k], f[i][j][k] + (l > 0));
				ckmin(f[i][j + 1][k], f[i][j][k] + (l > 0));
				ckmin(f[i][j][k + 1], f[i][j][k] + (l > 0));
			}

	memset(g, 127, sizeof(g));
	g[0][0] = 0;
	for(int i = 0; i <= 100; ++i)
		for(int j = 0; j <= 100; ++j){
			if(g[i][j] > 1e9) continue;
			int l = (i + j * 2) % 3;
			ckmin(g[i + 1][j], g[i][j] + (l > 0));
			ckmin(g[i][j + 1], g[i][j] + (l > 0));
		}

	scanf("%d", &T);
	while(T--){
		printf("Case #%d: ", ++ca);
		scanf("%d%d", &n, &p);
		cnt[1] = cnt[2] = cnt[3] = 0;
		int x;
		for(int i = 1; i <= n; ++i){
			scanf("%d", &x);
			cnt[x % p]++;
		}
		if(p == 2) printf("%d\n", n - cnt[1] / 2);
		else if(p == 3){
			printf("%d\n", n - g[cnt[1]][cnt[2]]);
		}else{
			printf("%d\n", n - f[cnt[1]][cnt[2]][cnt[3]]);
		}
	}
	return 0;
}
