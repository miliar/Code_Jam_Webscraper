//bzoj1823
#include<cstdio>
#include<iostream>
#include<cstring>
using namespace std;
#define N 2000
#define MIN(a,b) (((a)<(b))?(a):(b))
struct hh
{
	int next,v;
}edges[30000];
int T,n,m,dfn[N],low[N],stack[N],id[N],top,tot,cnt,point[N];
char c1,c2;
bool in[N];
char st[10][300];
int r,c;
inline void addedge(int u,int v)
{
	static int en(0);
	edges[++en].next=point[u];
	point[u]=en;
	edges[en].v=v;
//	printf("%d %d %d\n",en,u,v);
}
inline void tarjan(int x)
{
	low[x]=dfn[x]=++tot;in[x]=1;stack[top++]=x;
	for(int i=point[x];i;i=edges[i].next)
	if(!dfn[edges[i].v]){
		tarjan(edges[i].v);
		low[x]=MIN(low[x],low[edges[i].v]);
	}
	else if(in[edges[i].v])low[x]=MIN(low[x],dfn[edges[i].v]);
	if(dfn[x]==low[x])
	{
		int v;
		cnt++;
		do
		{
			v=stack[--top];
			in[v]=0;
			id[v]=cnt;
		}
		while(x!=v);
	}
}
int change(int x,int y)
{
  return (x-1)*c+y;
}
inline bool solve()
{
	tot=cnt=top=0;
	memset(dfn,0,sizeof(dfn));
	for(int i=2;i<=(n<<1^1);i++)
		if(!dfn[i])tarjan(i);
//	for (int i=2;i<=(n<<1^1);i++) printf("%d ",dfn[i]);printf("\n");
//	for (int i=2;i<=(n<<1^1);i++) printf("%d ",id[i]);printf("\n");
	for(int i=1;i<=n;i++)
		if(id[i<<1]==id[i<<1^1])return 0;
	return 1;
}
void print()
{
  for (int i=1;i<=r;i++)
  for (int j=1;j<=c;j++)
  if (st[i][j]=='|'||st[j]=='-')
  {
    if (id(change(i,j))==1) st[i][j]='|';
    else st[i][j]='-';
  }
  for (int i=1;i<=r;i++) printf("%s",st[i]+1);
}
int main()
{
		freopen("input.txt","r",stdin);
		freopen("std1823.out","w",stdout);
	scanf("%d",&T);
	for (int o=1;o<=T;o++)
	{
    scanf("%d%d",&r,&c);
		memset(point,0,sizeof(point));
		for (int i=1;i<=r;i++)
      scanf("%s",st[i]+1);
    for (int i=1;i<=r;i++)
      for (int j=1;j<=c;j++)
      if (st[i][j]=='#')
      {
        int k;int last=0;
        for (k=j+1;k<=c;k++)
          if (st[i][k]=='#') break;
        for (int l=j+1;l<k;l++)
          if (st[i][l]=='|'||st[i][l]=='-')
          if (last!=0)
          {addedge(change(i,l)*2,change(i,last)*2+1);
            addedge(change(i,l)*2+1,change(i,last)*2+1);
            last=l;
          }else last=l;
      }
      for (int j=1;j<=c;j++)
      for (int i=1;i<=r;i++)

        if (st[i][j]=='#')
        {
          int k;int last=0;
          for (k=j+1;k<=r;k++)
            if (st[k][j]=='#') break;
          for (int l=j+1;l<k;l++)
            if (st[l][j]=='|'||st[l][j]=='-')
            if (last!=0)
            {addedge(change(l,last)*2,change(l,j)*2+1);
              addedge(change(l,last)*2+1,change(l,j)*2+1);
              last=l;
            }else last=l;
        }
    if (solve())
    {
      printf("Case #%d: POSSIBLE\n",o);
    }
    else
    {printf("Case #%d: IMPOSSIBLE\n",o);print();}
	}
	return 0;
}
