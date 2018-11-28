#include <bits/stdc++.h>
#define maxn 1555
#define inf 0x3f3f3f3f
using namespace std;
int n,m;
int a[maxn], f[maxn][maxn][3];

int dp(int st){
	for (int i=1;i<1440;i++){
		for (int j=0;j<=720;j++){
			f[i][j][0]=f[i][j][1]=inf;
			if (a[i]==0){
				if (j==0) continue;
				f[i][j][0]=min(f[i][j][0], f[i-1][j-1][1]+1);
				f[i][j][0]=min(f[i][j][0], f[i-1][j-1][0]);
			}
			else if (a[i]==1){
				f[i][j][1]=min(f[i][j][1], f[i-1][j][0]+1);
				f[i][j][1]=min(f[i][j][1], f[i-1][j][1]);
			}
			else{
				if (j>0){
					f[i][j][0]=min(f[i][j][0], f[i-1][j-1][1]+1);
					f[i][j][0]=min(f[i][j][0], f[i-1][j-1][0]);
				}
				f[i][j][1]=min(f[i][j][1], f[i-1][j][0]+1);
				f[i][j][1]=min(f[i][j][1], f[i-1][j][1]);
			}
		}
	}
	if (st==0)
		return min(f[1439][720][0], f[1439][720][1]+1);
	else
		return min(f[1439][720][0]+1, f[1439][720][1]);
}

int main()
{
	freopen("C-large.in","r",stdin);
	freopen("C-large.out","w",stdout);
	int Case;
	scanf("%d",&Case);
	for (int o=1;o<=Case;o++){
		scanf("%d%d",&n,&m);
		memset(a, -1, sizeof(a));
		int x,y;
		for (int i=1;i<=n;i++){
			scanf("%d%d",&x,&y);
			for (int j=x;j<y;j++)
				a[j]=0;
		}
		for (int i=1;i<=m;i++){
			scanf("%d%d",&x,&y);
			for (int j=x;j<y;j++)
				a[j]=1;
		}
		int ans=inf;
		if (a[0]==0){
			memset(f, 0x3f, sizeof(f));
			f[0][1][0]=0;
			ans=min(ans, dp(0));

		}
		else if (a[0]==1){
			memset(f, 0x3f, sizeof(f));
			f[0][0][1]=0;
			ans=min(ans, dp(1));
		}
		else{
			memset(f, 0x3f, sizeof(f));
			f[0][1][0]=0;
			ans=min(ans, dp(0));
			memset(f, 0x3f, sizeof(f));
			f[0][0][1]=0;
			ans=min(ans, dp(1));			
		}
		printf("Case #%d: %d\n",o, ans);
	}

	return 0;
}