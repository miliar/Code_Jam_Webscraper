#include <cstdio>
#include <cstring>
#include <iostream>
#define mem(a,b) memset(a,b,sizeof(a))
using namespace std;
int a[103][103],N,b[103][103];
const int sz=410;
const int INF=1e9+9; 
const int MAXF=1e8;
struct EDG{int u,v,val;}edg[21800]; int fst[sz],nex[21800],en=1;
//isap
//����ͼ���ߺ���make_edg();
//����һ���ߵĻ�����Ϣ�걸����㡢�յ㡢������ ������edg�� 
//���ڽ�������ʽ�洢����˻�����fst[],nex[],�Լ��ܱ���en��
//Ҫ���Ѿ�������˫��ߣ��ұߵķ���Ϊ���ڵı�ţ����������1���õ���
//�����ܵ���tot��ԴΪS����ΪT��
//����MAXFΪ�����п��ܳ��ֵ�������������ڽ�ͼ����ʱʹ�ã���Ϊ�趨Ϊ�μ�INF����
//����INFΪһ����MAXF��Ҫ��ļ�Ϊ����ĳ����� 
//����sz�ȵ����Դ�isap�����ڵ����鶼�ǹ��ڵ�ġ�ȫ�ֵ�sz��isap�����ڲ���sz������ע�����֡� 
//isap()������������� 
int S,T;
int dis[sz],cur[sz],pre[sz],gap[sz];
void make_edg(int u,int v,int val)
{	en++; edg[en].u=u; edg[en].v=v; edg[en].val=val; nex[en]=fst[u]; fst[u]=en;
	en++; edg[en].u=v; edg[en].v=u; edg[en].val=0;   nex[en]=fst[v]; fst[v]=en;
}
void update(int &ans)
{	int x=INF;
	for(int v=T;v!=S;v=edg[pre[v]].u) if(x>edg[pre[v]].val) x=edg[pre[v]].val;
	for(int v=T;v!=S;v=edg[pre[v]].u){edg[pre[v]].val-=x; edg[pre[v]^1].val+=x;}
	ans+=x;
}
int isap(int tot)
{	memset(dis,0,sizeof(dis)); memset(cur,0,sizeof(cur)); memset(pre,0,sizeof(pre));
	memset(gap,0,sizeof(gap)); int sz=tot+3,ans=0; gap[0]=sz; //�˴�szΪ�ض���ĵ���+3���ֲ��ڸ�ȫ�ֵ�sz����û�й�ϵ 
	for(int u=S;dis[S]<sz;)
	{	int ok=0;
		if(u==T){update(ans); u=S;}
		for(int i=cur[u];i;i=nex[i]) if(edg[i].val&&dis[u]==dis[edg[i].v]+1)
		{
			ok=1; cur[u]=i; pre[edg[i].v]=i; u=edg[i].v; break;
		}
		if(ok==0)
		{	int k=sz-1; if(--gap[dis[u]]==0) break; //�ϲ� 
			for(int i=fst[u];i;i=nex[i]) if(edg[i].val>0&&k>dis[edg[i].v]) k=dis[edg[i].v];
			dis[u]=k+1; gap[dis[u]]++; cur[u]=fst[u];
			if(u!=S) u=edg[pre[u]].u;
		}
	}
	return ans;
}
//isap
short flagR[210],flagC[210];
void build1()
{	int i,j; S=N+N+1; T=N+N+2;
	mem(fst,0); en=1;
	mem(flagR,0); mem(flagC,0);
	for(i=1;i<=N;i++) for(j=1;j<=N;j++)
		if(a[i][j]==1||a[i][j]==3) flagR[i]=flagC[j]=1;
		else make_edg(i,N+j,1);
	for(i=1;i<=N;i++)
	{	if(!flagR[i]) make_edg(S,i,1);
		if(!flagC[i]) make_edg(N+i,T,1);
	}
}
void fill1()
{
	for(int i=2;i<=en;i++) if(edg[i].u<=N&&edg[i].v<=N+N&&edg[i].val==0) b[edg[i].u][edg[i].v-N]+=1;
}
void build2()
{	int i,j; S=401; T=402;
	mem(fst,0); en=1;
	mem(flagR,0); mem(flagC,0);
	for(i=1;i<=N;i++) for(j=1;j<=N;j++)
		if(a[i][j]==2||a[i][j]==3) flagR[i-j+N]=flagC[i+j]=1;
		else make_edg(i-j+N,i+j+200,1);
	for(i=1;i<=200;i++)
	{	if(!flagR[i]) make_edg(S,i,1);
		if(!flagC[i]) make_edg(200+i,T,1);
	}
}
void fill2()
{
	for(int i=2;i<=en;i++) if(edg[i].u<=200&&edg[i].v<=400&&edg[i].val==0)
		b[(edg[i].u+edg[i].v-N-200)/2][((edg[i].v-200)-(edg[i].u-N))/2]+=2;
}
int main()
{
//	freopen("D-large.in","r",stdin);
//	freopen("D-large.out","w",stdout);
	int cas; cin>>cas;
	for(int casi=1;casi<=cas;casi++)
	{	int M,i,j; cin>>N>>M;
		mem(a,0); mem(b,0);
		for(i=1;i<=M;i++)
		{	char ch[3]; int x,y;
			scanf("%s%d%d",ch,&x,&y);
			if(ch[0]=='x') a[x][y]=1;
			else if(ch[0]=='+') a[x][y]=2;
			else a[x][y]=3;
			b[x][y]=a[x][y];
		}
		build1(); isap(N+N+2); fill1();
		build2(); isap(402); fill2();
		int ans=0,ansk=0;
		for(i=1;i<=N;i++)
			for(j=1;j<=N;j++)
			{	if(b[i][j]==1) ans++;
				else if(b[i][j]==2) ans++;
				else if(b[i][j]==3) ans+=2;
				if(b[i][j]!=a[i][j]) ansk++;
			}
		printf("Case #%d: %d %d\n",casi,ans,ansk);
		for(i=1;i<=N;i++)
			for(j=1;j<=N;j++)
			{	if(b[i][j]!=a[i][j])
					if(b[i][j]==1) printf("x %d %d\n",i,j);
					else if(b[i][j]==2) printf("+ %d %d\n",i,j);
					else if(b[i][j]==3) printf("o %d %d\n",i,j);
			}
	}
	return 0;
}

