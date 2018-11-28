#include<stdio.h>
#include<string.h>
#include<math.h>
#include<iostream>
#include<algorithm>
#include<vector>
#include<map>
#include<string>
#include<set>
#include<sstream>
using namespace std;
typedef long long lld;
#define mp make_pair
#define X first
#define Y second
#define pb push_back
#define mp make_pair
#define eps 1e-8
#define pi acos(-1.0)
char str[110];
int save[110][110];
int ans[110][110];
bool g[410][410];
bool canx[410];
bool cany[410];
int nnn;
int linky[410];
bool marky[410];
bool find(int x)
{
	for(int y=0;y<nnn;y++)
		if(g[x][y] && !marky[y])
		{
			marky[y]=true;
			if(linky[y] == -1 || find(linky[y]))
			{
				linky[y]=x;
				return true;
			}
		}
	return false;
}
int r[210][210];
int c[210][210];
map<int,int>fx,fy,backfx,backfy;
map<int,int>::iterator ll;
pair<char,pair<int,int> >pp[100010];
int qq;
char ccc[110]={' ','x','+','o'};
int main()
{
	freopen("D-small-attempt0.in","r",stdin);
	freopen("out.txt","w",stdout);
	int cas;
	scanf("%d",&cas);
	for(int cc=1;cc<=cas;cc++)
	{
		int n,m;
		scanf("%d %d",&n,&m);
		memset(save,0,sizeof(save));
		for(int i=0;i<m;i++)
		{
			scanf("%s",str);
			int x,y;
			scanf("%d %d",&x,&y);
			x--;
			y--;
			if(str[0] == 'x')
				save[x][y]=1;
			if(str[0] == '+')
				save[x][y]=2;
			if(str[0] == 'o')
				save[x][y]=3;
		}
		for(int i=0;i<n;i++)
			for(int j=0;j<n;j++)
				ans[i][j]=save[i][j];
		memset(canx,true,sizeof(canx));
		memset(cany,true,sizeof(cany));
		for(int i=0;i<n;i++)
			for(int j=0;j<n;j++)
				if(save[i][j]&1)
				{
					canx[i]=false;
					cany[j]=false;
				}
		for(int i=0;i<n;i++)
			for(int j=0;j<n;j++)
			{
				if(!(save[i][j]&1) && canx[i] && cany[j])
					g[i][j]=true;
				else
					g[i][j]=false;
			}
		nnn=n;
		memset(linky,-1,sizeof(linky));
		for(int i=0;i<nnn;i++)
		{
			memset(marky,false,sizeof(marky));
			find(i);
		}
		for(int y=0;y<n;y++)
			if(linky[y] != -1)
			{
				int x=linky[y];
				ans[x][y]|=1;
			}
		fx.clear();
		fy.clear();
		backfx.clear();
		backfy.clear();
		for(int i=0;i<n;i++)
			for(int j=0;j<n;j++)
				fx[i+j]=1,fy[i-j]=1;
		int T=0;
		for(ll=fx.begin();ll!=fx.end();ll++)
		{
			ll->Y=T++;
			backfx[ll->Y]=ll->X;
		}
		T=0;
		for(ll=fy.begin();ll!=fy.end();ll++)
		{
			ll->Y=T++;
			backfy[ll->Y]=ll->X;
		}
		for(int i=0;i<n;i++)
			for(int j=0;j<n;j++)
				r[i][j]=fx[i+j],c[i][j]=fy[i-j];
		memset(canx,true,sizeof(canx));
		memset(cany,true,sizeof(cany));
		for(int i=0;i<n;i++)
			for(int j=0;j<n;j++)
				if(save[i][j]&2)
				{
					canx[r[i][j]]=false;
					cany[c[i][j]]=false;
				}
		memset(g,false,sizeof(g));
		for(int i=0;i<n;i++)
			for(int j=0;j<n;j++)
			{
				if(!(save[i][j]&2) && canx[r[i][j]] && cany[c[i][j]])
					g[r[i][j]][c[i][j]]=true;
				else
					g[r[i][j]][c[i][j]]=false;
			}
		nnn=T;
//		for(int i=0;i<nnn;i++)
//			for(int j=0;j<nnn;j++)
//				if(g[i][j])
//					printf("---%d %d\n",i,j);
		memset(linky,-1,sizeof(linky));
		for(int i=0;i<nnn;i++)
		{
			memset(marky,false,sizeof(marky));
			find(i);
		}
		for(int y=0;y<nnn;y++)
			if(linky[y] != -1)
			{
				int x=linky[y];
				int xx=backfx[x];
				int yy=backfy[y];
				int i=(xx+yy)/2;
				int j=(xx-yy)/2;
				ans[i][j]|=2;
//				printf("***%d %d %d %d\n",x,y,xx,yy);
			}
//		printf("\n");
//		for(int i=0;i<n;i++)
//		{
//			for(int j=0;j<n;j++)
//				printf("%d ",save[i][j]);
//			printf("\n");
//		}
//		printf("\n");
//		for(int i=0;i<n;i++)
//		{
//			for(int j=0;j<n;j++)
//				printf("%d ",ans[i][j]);
//			printf("\n");
//		}
//		printf("\n");
		int out=0;
		for(int i=0;i<n;i++)
			for(int j=0;j<n;j++)
			{
				if(ans[i][j]&1)
					out++;
				if(ans[i][j]&2)
					out++;
			}
		qq=0;
		for(int i=0;i<n;i++)
			for(int j=0;j<n;j++)
				if(save[i][j] != ans[i][j])
					pp[qq++]=mp(ccc[ans[i][j]],mp(i+1,j+1));
		printf("Case #%d: %d %d\n",cc,out,qq);
		for(int i=0;i<qq;i++)
			printf("%c %d %d\n",pp[i].X,pp[i].Y.X,pp[i].Y.Y);
	}
	return 0;
}
/*
3
2 0
1 1
o 1 1
3 4
+ 2 3
+ 2 1
x 3 1
+ 2 2

1
2 0

 */
