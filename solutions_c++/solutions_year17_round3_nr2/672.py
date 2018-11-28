#include <bits/stdc++.h>
using namespace std;
typedef long long LL;
#define maxn 1000

int f[maxn][maxn][2][2];
int AC, AJ;
int C[maxn],D[maxn],J[maxn],K[maxn];
int vis[2000];

int main() {
	freopen("B-large.in","r",stdin);
	freopen("B.out","w",stdout);
	int T = 0; scanf("%d",&T);
	for(int t = 1;t <= T;++ t) {
		memset(vis,0,sizeof(vis));
		scanf("%d%d",&AC,&AJ);
		for(int i = 1;i <= AC;++ i) {
			scanf("%d%d",&C[i],&D[i]);
			C[i] ++; //D[i] ++;
			for(int j = C[i];j <= D[i];++ j) vis[j] = 1;
		}
		for(int i = 1;i <= AJ;++ i) {
			scanf("%d%d",&J[i],&K[i]);
			J[i] ++; //K[i] ++;
			for(int j = J[i];j <= K[i];++ j) vis[j] = 2;
		}
		memset(f, 0x3f, sizeof(f));
		if(vis[1] != 1) f[1][0][0][0] = 0;
		if(vis[1] != 2) f[0][1][1][1] = 0;
		for(int ti = 2;ti <= 1440;++ ti) {
			for(int i = max(0,ti-720);i <= 720 && i <= ti;++ i) {
				for(int last = 0;last < 2;++ last) {
					if(vis[ti] == last+1) continue; 			
					int li = i,lj = ti-i;
					if(!last) li --; else lj --;
					if(li < 0 || lj < 0) continue;
					for(int k = 0;k < 2;++ k) 
						for(int l = 0;l < 2;++ l)
							f[i][ti-i][k][last] = min(f[i][ti-i][k][last],f[li][lj][k][l]+(last!=l));
				}
			}
		}
		int ans = min(f[720][720][1][1],min(f[720][720][0][0],min(f[720][720][1][0],f[720][720][0][1])+1));
		printf("Case #%d: %d\n",t,ans);
	}
	return 0;
}
