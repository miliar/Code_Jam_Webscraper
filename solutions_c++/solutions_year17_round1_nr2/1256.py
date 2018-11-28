#include <bits/stdc++.h>
using namespace std;
#define maxn 102
#define xx first
#define yy second

typedef pair<int,int> pii;
pii s[maxn][maxn];
int g[maxn], p[maxn], x[maxn][maxn];
int n, m;

int main()
{
	freopen("B-small-attempt0.in","r",stdin);
	freopen("B-small.out","w",stdout);
	int Case;
	scanf("%d",&Case);
	for (int o=1;o<=Case;o++){
		scanf("%d%d",&n,&m);
		for (int i=1;i<=n;i++)
			scanf("%d",&g[i]);
		for (int i=1;i<=n;i++){
			for (int j=1;j<=m;j++)
				scanf("%d",&x[i][j]);
			sort(x[i]+1, x[i]+m+1);
		}
		for (int i=1;i<=n;i++){
			for (int j=1;j<=m;j++){
				s[i][j].xx=(int)ceil(x[i][j]*1.0/(1.1*g[i]));
				s[i][j].yy=(int)floor(x[i][j]*1.0/(0.9*g[i]));
				//cout<<s[i][j].xx<<' '<<s[i][j].yy<<endl;
			}
		}

		for (int i=1;i<=n;i++)
			p[i]=1;
		
		int flag=0, ans=0;
		while (!flag){
			int mx_l=0;
			for (int i=1;i<=n;i++)
				mx_l=max(mx_l, s[i][p[i]].xx);
			for (int i=1;i<=n;i++){
				while (p[i]<=m && s[i][p[i]].yy<mx_l)
					p[i]++;
				if (p[i]>m){
					flag=1;
					break;
				}
			}
			if (flag) break;
			ans++;
			for (int i=1;i<=n;i++){
				p[i]++;
				if (p[i]>m){
					flag=1;
					break;
				}
			}
		}
		printf("Case #%d: %d\n", o, ans);
	}

	return 0;
}