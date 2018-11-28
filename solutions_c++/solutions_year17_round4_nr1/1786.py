#include <iostream>
#include <cstdlib>
#include <cstring>
#include <algorithm>
#include <cmath>
using namespace std;
int f[101][101][101][4];
int cnt[4];
int T,n,p;
int a[111];
int main(){
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	scanf("%d",&T);
	for (int tt = 1; tt <= T; tt++){
		scanf("%d %d ",&n,&p);
		memset(cnt, 0, sizeof(cnt));
		for (int i = 1; i <= n; i++)
			scanf("%d", &a[i]);
		for (int i = 1; i <= n; i++)
			cnt[a[i] % p]++;
		memset(f,0,sizeof(f));
		f[0][0][0][0] = cnt[0];
		for (int nn = 1; nn <= n - cnt[0]; nn++){
			for (int i = 0;i <= nn; i++){
				if (i > cnt[1]) break;
				for (int j = 0; i + j <= nn; j++){
					int k = nn - i - j;
					//cerr << "!" << i << " " << j << " " << k << " " << endl;
					//if (j > cnt[2]) break;
					//if (k > cnt[3]) continue;
					for (int l = 0; l < 4; l++){
						//cerr << i << " " << j << " " << k << " " << l << endl; 
						//if (i == 1 && j == 0 && k == 0 && l == 1) cerr << "ok" << endl;
						if (i - 1 >= 0){
							f[i][j][k][l] = max(f[i][j][k][l], f[i - 1][j][k][(l-1+p)%p] + ((l - 1 + p)%p == 0));
						}
						if (j - 1 >= 0){
							f[i][j][k][l] = max(f[i][j][k][l], f[i][j-1][k][(l - 2 + p)%p] + ((l - 2 + p)% p == 0));
						}
						if (k - 1 >= 0){
							f[i][j][k][l] = max(f[i][j][k][l], f[i][j][k - 1][(l - 3 + p)%p] + ((l - 3 + p)  == 0));
						}
					}
				}
			}
		}
		//		cout << f[1][0][0][1] << endl;
		int ans = 0;
		for (int i = 0; i < 4; i++)
			ans = max(ans, f[cnt[1]][cnt[2]][cnt[3]][i]);
		printf("Case #%d: %d\n",tt,ans);
	}
	return 0;
}
