#include <bits/stdc++.h>
using namespace std;
#define maxn 220
#define inf 2000000000000000
double d[maxn][maxn];
double a[maxn];
double sa[maxn];
double s[maxn], v[maxn];
double f[maxn];
int n, m;
int x, y;

int main()
{
	freopen("C-small.in","r",stdin);
	freopen("C-small.out","w",stdout);
	int Case;
	scanf("%d",&Case);
	for (int o=1;o<=Case;o++){
		scanf("%d%d",&n,&m);
		for (int i=1;i<=n;i++)
			scanf("%lf%lf",&s[i], &v[i]);
		for (int i=1;i<=n;i++)
			for (int j=1;j<=n;j++)
				scanf("%lf",&d[i][j]);
		for (int i=1;i<=m;i++)
			scanf("%d%d",&x,&y);
		memset(sa, 0, sizeof(sa));
		sa[1]=0;
		for (int i=1;i<n;i++){
			a[i]=d[i][i+1];
			sa[i+1]=sa[i]+a[i];
		}
		memset(f, 0, sizeof(f));
		f[1]=0;
		for (int i=2;i<=n;i++){
			f[i]=inf;
			for (int j=1;j<i;j++)
				if (sa[i]-sa[j]<=s[j])
					f[i]=min(f[i], f[j]+(sa[i]-sa[j])*1.0/v[j]);
		}
		printf("Case #%d: %.6f\n", o, f[n]);
	}
	return 0;
}