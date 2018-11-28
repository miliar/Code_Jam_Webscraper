#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<algorithm>
#include<iostream>
using namespace std;
template<class T> inline bool ten(T &x,const T &y){return y<x?x=y,1:0;}
template<class T> inline bool rel(T &x,const T &y){return x<y?x=y,1:0;}
int R,C,D;
char s[55][55];
int n,IMP;
int I[55][55];

const int dx[4]={0,1, 0,-1};
const int dy[4]={1,0,-1, 0};

int go[55][55][4],dr[55][55][4],rdr;
int vis[55][55][4],vi;

#define next next_
const int maxn=5555;
int head[maxn],adj[maxn*maxn],next[maxn*maxn],tot;

void addedge(int u,int v)
{//cout<<u<<' '<<v<<endl;
tot++;adj[tot]=v;next[tot]=head[u];head[u]=tot;}

int shot(int x,int y,int d)
{
	if(vis[x][y][d]==vi)return -1;
	vis[x][y][d]=vi;
	if(s[x][y]=='#'){rdr=d;return 0;}
	if(s[x][y]=='-'){rdr=d;return I[x][y];}
	if(s[x][y]=='.'){return shot(x+dx[d],y+dy[d],d);}
	if(s[x][y]=='/'){return shot(x+dx[d^3],y+dy[d^3],d^3);}
	if(s[x][y]=='\\'){return shot(x+dx[d^1],y+dy[d^1],d^1);}
}

void init()
{
	memset(head,0,sizeof(head));tot=1;
	memset(go,0,sizeof(go));
	for(int i=1;i<=R;i++)
		for(int j=1;j<=C;j++)
			for(int k=0;k<4;k++)
			{
				vi++;
				go[i][j][k]=shot(i,j,k);
				dr[i][j][k]=rdr;
				if(go[i][j][k]==-1){IMP=1;return;}
			}
	int t,w,u,v,p,q,u_,v_;
	for(int i=1;i<=R;i++)
		for(int j=1;j<=C;j++)
			if(s[i][j]=='-')
			{
				if(go[i+dx[0]][j+dy[0]][0]||go[i+dx[2]][j+dy[2]][2])addedge(I[i][j],I[i][j]+D);
				if(go[i+dx[1]][j+dy[1]][1]||go[i+dx[3]][j+dy[3]][3])addedge(I[i][j]+D,I[i][j]);
			}
			else if(s[i][j]=='.')
			{
				if((go[i][j][0]==0)==(go[i][j][2]==0))
				{
					if(go[i][j][1]&&go[i][j][3]){IMP=1;return;}
					if(go[i][j][1])t=go[i][j][1],w=dr[i][j][1];
					else if(go[i][j][3])t=go[i][j][3],w=dr[i][j][3];
					else {IMP=1;return;}
					if((w&1)==0)addedge(t+D,t);
					else addedge(t,t+D);
				}
				else if((go[i][j][1]==0)==(go[i][j][3]==0))
				{
					if(go[i][j][0]&&go[i][j][2]){IMP=1;return;}
					if(go[i][j][0])t=go[i][j][0],w=dr[i][j][0];
					else if(go[i][j][2])t=go[i][j][2],w=dr[i][j][2];
					else {IMP=1;return;}
					if((w&1)==0)addedge(t+D,t);
					else addedge(t,t+D);
				}
				else
				{
					if(go[i][j][0])u=go[i][j][0],p=dr[i][j][0];
					else u=go[i][j][2],p=dr[i][j][2];
					if(go[i][j][1])v=go[i][j][1],q=dr[i][j][1];
					else v=go[i][j][3],q=dr[i][j][3];
					u_=u+D;
					v_=v+D;
					if((p&1))swap(u,u_);
					if((q&1))swap(v,v_);
					addedge(u_,v);
					addedge(v_,u);
				}
			}
}

int dfn[maxn],low[maxn],st[maxn],ins[maxn],top,cur[maxn],idx,cnt;
int tim[maxn],tmc;

void tarjan(int x)
{
	dfn[x]=low[x]=++idx;
	st[++top]=x;
	ins[x]=top;
	for(int i=head[x];i;i=next[i])
		if(!dfn[adj[i]])
		{
			tarjan(adj[i]);
			low[x]=min(low[x],low[adj[i]]);
		}
		else if(ins[adj[i]])
			low[x]=min(low[x],dfn[adj[i]]);
	if(low[x]>=dfn[x])
	{
		int tmp=ins[x]-1;
		cnt++;
		while(top>tmp)
		{
			cur[st[top]]=cnt;
			ins[st[top]]=0;
			tim[st[top]]=++tmc;
			top--;
		}
	}
}

int ans[maxn];

void work()
{
	if(IMP){return;}
	idx=cnt=tmc=0;
	memset(dfn,0,sizeof(dfn));
	memset(ins,0,sizeof(ins));
	for(int i=1;i<=n;i++)
		if(dfn[i]==0)
			tarjan(i);
	for(int i=1;i<=D;i++)
		if(cur[i]==cur[i+D])
		{IMP=1;return;}
		else
		{
			if(tim[i]<tim[i+D])ans[i]=0;
			else ans[i]=1;
		}
	cout<<"POSSIBLE"<<endl;
	for(int i=1;i<=R;i++)
	{
		for(int j=1;j<=C;j++)
		{
			if(s[i][j]=='-'&&ans[I[i][j]])s[i][j]='|';
			putchar(s[i][j]);
		}
		puts("");
	}
}

int main()
{
	freopen("C-small-attempt0.in","r",stdin);
	freopen("C-small-attempt0.out","w",stdout);
	int T=0;cin>>T;
	for(int qi=1;qi<=T;qi++)
	{
		printf("Case #%d: ",qi);
		scanf("%d%d\n",&R,&C);
		n=0;
		memset(s,'#',sizeof(s));
		for(int i=1;i<=R;i++)
		{
			scanf("%s",s[i]+1);
			s[i][0]=s[i][C+1]='#'; 
			for(int j=1;j<=C;j++)
				if(s[i][j]=='|'||s[i][j]=='-')
					s[i][j]='-',I[i][j]=++n;
				else
					I[i][j]=0;
		}
		D=n;n*=2;IMP=0;
		init();
		work();
		if(IMP)cout<<"IMPOSSIBLE"<<endl;
	}
	return 0;
}

