#include <cmath>
#include <cstdio>
#include <cstring>
#include <vector>
#include <algorithm>

using namespace std;

typedef vector<int> vi;

#define pb push_back

bool g1[210],g2[210],g3[210],g4[210];
bool base[210][210][2],ans[210][210][2],v[210];
int pre[210],a[210],b[210],d[10010][2];
char c[10010];
vi e[210];

bool dfs(int k)
{
	for (vi::iterator p=e[k].begin();p!=e[k].end();p++)
		if (!v[*p])
		{
			v[*p]=1;
			if (pre[*p]==0||dfs(pre[*p]))
			{
				pre[*p]=k;return 1;
			}
		}
	return 0;
}

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int test;scanf("%d",&test);
	for (int T=1;T<=test;T++)
	{
		int n,m;scanf("%d%d",&n,&m);
		memset(g1,0,sizeof(g1));
		memset(g2,0,sizeof(g2));
		memset(g3,0,sizeof(g3));
		memset(g4,0,sizeof(g4));
		memset(base,0,sizeof(base));
		int w=0;
		for (int i=1;i<=m;i++)
		{
			char ch;
			for (ch=getchar();ch!='o'&&ch!='+'&&ch!='x';) ch=getchar();
			int x,y;scanf("%d%d",&x,&y);
			if (ch!='+') {base[x][y][0]=1;g1[x]=1;g2[y]=1;}
			if (ch!='x') {base[x][y][1]=1;g3[x+y-1]=1;g4[x-y+n]=1;}
		}
		for (int i=1;i<=n;i++)
			for (int j=1;j<=n;j++)
				for (int k=0;k<2;k++)
					ans[i][j][k]=base[i][j][k];
		int l1=0;for (int i=1;i<=n;i++) if (!g1[i]) a[++l1]=i;
		int l2=0;for (int i=1;i<=n;i++) if (!g2[i]) b[++l2]=i;
		for (int i=1;i<=min(l1,l2);i++) ans[a[i]][b[i]][0]=1;
		for (int i=1;i<2*n;i++) e[i].clear();
		for (int i=1;i<=n;i++)
			for (int j=1;j<=n;j++)
				if (g3[i+j-1]==0&&g4[i-j+n]==0) e[i+j-1].pb(i-j+n);
		memset(pre,0,sizeof(pre));
		for (int i=1;i<2*n;i++)
		{
			memset(v,0,sizeof(v));
			dfs(i);
		}
		for (int i=1;i<2*n;i++) if (pre[i]) ans[(i+pre[i]-n+1)/2][(pre[i]-i+1+n)/2][1]=1;
		int l0=0;
		for (int i=1;i<=n;i++)
			for (int j=1;j<=n;j++)
				if (ans[i][j][0]>base[i][j][0]||ans[i][j][1]>base[i][j][1])
				{
					d[++l0][0]=i;d[l0][1]=j;
					if (ans[i][j][0]&&ans[i][j][1]) c[l0]='o'; else if (ans[i][j][0]) c[l0]='x'; else c[l0]='+';
				}
		for (int i=1;i<=n;i++)
			for (int j=1;j<=n;j++)
				w+=ans[i][j][0]+ans[i][j][1];
		printf("Case #%d: %d %d\n",T,w,l0);
		for (int i=1;i<=l0;i++) printf("%c %d %d\n",c[i],d[i][0],d[i][1]);
	}
	return 0;
}

