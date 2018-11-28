#include <bits/stdc++.h>
using namespace std;
typedef long long LL;
const double pi = 3.141592653589F;
#define maxn 1010
struct node {
	LL R, H; LL S; 
}d[maxn];
int k = 0,n = 0;
inline bool cmp(const node &a,const node &b) {
	return a.R > b.R;
}
LL f[maxn][maxn];
int main() {
	freopen("A-large.in","r",stdin);
	freopen("A.out","w",stdout);
	int T = 0; scanf("%d",&T);
	for(int t = 1;t <= T;++ t) {
		scanf("%d%d",&n,&k);
		for(int i = 1;i <= n;++ i) {
			scanf("%lld%lld",&d[i].R,&d[i].H);
			d[i].S = d[i].R * d[i].H * 2LL;
		}
		sort(d+1, d+n+1, cmp);
		memset(f,0,sizeof(f));
		for(int i = 1;i <= n;++ i) {
			f[i][1] = max(f[i-1][1], d[i].S+d[i].R*d[i].R);
			for(int j = 2;j <= k;++ j) {
				if(f[i-1][j] != 0)
					f[i][j] = max(f[i-1][j], f[i][j]);
				if(f[i-1][j-1] != 0)
					f[i][j] = max(f[i-1][j-1]+d[i].S, f[i][j]); 
			}
		}
		//cout << f[n][k] << endl;
		printf("Case #%d: %.12lf\n",t,1.0F*pi*f[n][k]);
	}
	return 0;
} 
