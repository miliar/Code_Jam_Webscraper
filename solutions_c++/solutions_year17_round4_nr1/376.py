#include <cstdio>
#include <cmath>
#include <cstring>
#include <algorithm>
#include <iostream>
#define DO long double
#define REP(i,n) for (int i=1;i<=n;++i)
using namespace std;

int T,n,p,x,ans;
int a[10];
int f[110][110][110];

void relax(int &a, int b) {
	if (b>a) a=b;
}

int main() {
	freopen("1.in","r",stdin);
	freopen("1.out","w",stdout);
	scanf("%d",&T);
	REP(T_T,T) {
		printf("Case #%d: ", T_T);
		scanf("%d %d", &n, &p);
		memset(a,0,sizeof(a));
		REP(i,n) {
			scanf("%d",&x);
			++a[x%p];
		}
		ans=0;

		ans+=a[0];
		
		if (p==2) {
			ans+=a[1]/2;
			ans+=a[1]%2;
		}
		if (p==3) {
			int tmp=min(a[1],a[2]);
			ans+=tmp;
			a[1]-=tmp;
			a[2]-=tmp;
			ans+=a[1]/3+a[2]/3;
			ans+=min(max(a[1]%3,a[2]%3),1);
		}
		if (p==4) {
			memset(f,0,sizeof(f));
			f[0][0][0]=0;
			for (int i=0;i<=a[1];++i)
				for (int j=0;j<=a[2];++j)
					for (int k=0;k<=a[3];++k) {
						// 1111 112 13 22 233 3333
						relax(f[i+4][j][k],f[i][j][k]+1);
						relax(f[i+2][j+1][k],f[i][j][k]+1);
						relax(f[i+1][j][k+1],f[i][j][k]+1);
						relax(f[i][j+2][k],f[i][j][k]+1);
						relax(f[i][j+1][k+2],f[i][j][k]+1);
						relax(f[i][j][k+4],f[i][j][k]+1);
					}
			int tmp=0;
			for (int i=0;i<=a[1];++i)
				for (int j=0;j<=a[2];++j)
					for (int k=0;k<=a[3];++k)
						if (i<a[1] || j<a[2] || k<a[3])
							relax(tmp, f[i][j][k]+1);
						else
							relax(tmp, f[i][j][k]);
			ans+=tmp;
		}

		printf("%d\n",ans);
	}
	return 0;
}