#include<bits/stdc++.h>
using namespace std;
#define pb push_back
#define mkp make_pair
#define fi first
#define se second
#define ll long long
#define M 1000000007
#define all(a) a.begin(), a.end()

int T, n, m;
int t[24 * 60 + 10];
int f[24 * 60 + 10][12 * 60 + 10][2];

int work(int bg){
	memset(f, 127, sizeof(f));
	if(bg == 0) f[1][1][0] = t[1] & 1 ? 0 : 1e9;
	else f[1][0][1] = t[1] & 2 ? 0 : 1e9;
	for(int i = 2; i <= 24 * 60; ++i)
		for(int j = 0; j <= min(i, 12 * 60); ++j)
			for(int k = 0; k < 2; ++k){
				if(f[i - 1][j][k] >= 1e9) continue;
				for(int l = 0; l < 2; ++l)
					if(t[i] & (1 << l)){
						if(l == 0)
							f[i][j + 1][l] = min(f[i][j + 1][l], f[i - 1][j][k] + (k != l));
						else
							f[i][j][l] = min(f[i][j][l], f[i - 1][j][k] + (k != l));
					}
			}
	return min(f[24 * 60][12 * 60][0] + (bg == 1), f[24 * 60][12 * 60][1] + (bg == 0));
}

int main(){
	freopen("B-large.in", "r", stdin);
	freopen("x.out", "w", stdout);
	int T, ca = 0;
	scanf("%d", &T);
	while(T--){
		scanf("%d%d", &n, &m);
		for(int i = 1; i <= 24 * 60; ++i) t[i] = 3;
		int l, r;
		for(int i = 1; i <= n; ++i){
			scanf("%d%d", &l, &r);
			for(int j = l + 1; j <= r; ++j) t[j] ^= 1;
		}
		for(int i = 1; i <= m; ++i){
			scanf("%d%d", &l, &r);
			for(int j = l + 1; j <= r; ++j) t[j] ^= 2;
		}
		
		printf("Case #%d: %d\n", ++ca, min(work(0), work(1)));
	}
	return 0;
}
