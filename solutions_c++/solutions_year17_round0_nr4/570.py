#include<stdio.h>
#include<math.h>
#include<algorithm>
#include<queue>
#include<deque>
#include<string>
#include<string.h>
#include<vector>
#include<set>
#include<map>
#include<stdlib.h>
#include<cassert>
using namespace std;
const long long mod=1000000007;
const long long inf=mod*mod;
const long long d2=500000004;

const int D_MAX_V=2002;
const int D_v_size=2002;
struct D_wolf{
	int t,c,r;
	D_wolf(){t=c=r=0;}
	D_wolf(int t1,int c1,int r1){
		t=t1;c=c1;r=r1;
	}
};
vector<D_wolf>D_G[D_MAX_V];
int D_level[D_MAX_V];
int D_iter[D_MAX_V];

void add_edge(int from,int to,int cap){
	D_G[from].push_back(D_wolf(to,cap,D_G[to].size()));
	D_G[to].push_back(D_wolf(from,0,D_G[from].size()-1));
}
void D_bfs(int s){
	for(int i=0;i<D_v_size;i++)D_level[i]=-1;
	queue<int> Q;
	D_level[s]=0;
	Q.push(s);
	while(Q.size()){
		int v=Q.front();
		Q.pop();
		for(int i=0;i<D_G[v].size();i++){
			if(D_G[v][i].c>0&&D_level[D_G[v][i].t]<0){
				D_level[D_G[v][i].t]=D_level[v]+1;
				Q.push(D_G[v][i].t);
			}
		}
	}
}
int D_dfs(int v,int t,int f){
	if(v==t)return f;
	for(;D_iter[v]<D_G[v].size();D_iter[v]++){
		int i=D_iter[v];
		if(D_G[v][i].c>0&&D_level[v]<D_level[D_G[v][i].t]){
			int d=D_dfs(D_G[v][i].t,t,min(f,D_G[v][i].c));
			if(d>0){
				D_G[v][i].c-=d;
				D_G[D_G[v][i].t][D_G[v][i].r].c+=d;
				return d;
			}
		}
	}
	return 0;
}
int max_flow(int s,int t){
	int flow=0;
	for(;;){
		D_bfs(s);
		if(D_level[t]<0)return flow;
		for(int i=0;i<D_v_size;i++)D_iter[i]=0;
		int f;
		while((f=D_dfs(s,t,99999999))>0){flow+=f;}
	}
	return 0;
}
char str[110][110];
int ind[210][210];
int ans[110][110];
char in[2];
int uc[210];
int ur[210];
int main(){
	int T;scanf("%d",&T);
	for(int t=1;t<=T;t++){
		int a,b;scanf("%d%d",&a,&b);
		for(int i=0;i<a;i++)for(int j=0;j<a;j++)str[i][j]='.';
		for(int i=0;i<a;i++)for(int j=0;j<a;j++)ans[i][j]=0;
		for(int i=0;i<a;i++)str[i][a]=0;
		for(int i=0;i<b;i++){
			int p,q;
			scanf("%s%d%d",in,&p,&q);
			p--;q--;
			str[p][q]=in[0];
		}
		for(int i=0;i<D_MAX_V;i++){
			D_G[i].clear();
			D_level[i]=D_iter[i]=0;
		}
		int st=a*2;
		int go=a*2+1;
		for(int i=0;i<a;i++){
			add_edge(st,i,1);
			add_edge(i+a,go,1);
		}
		for(int i=0;i<a;i++)for(int j=0;j<a;j++)ind[i][j]=-1;
		for(int i=0;i<a;i++)uc[i]=ur[i]=0;
		for(int i=0;i<a;i++){
			for(int j=0;j<a;j++){
				if(str[i][j]=='x'||str[i][j]=='o')ur[i]=uc[j]=1;
			}
		}
		for(int i=0;i<a;i++)for(int j=0;j<a;j++){
			if(ur[i]||uc[j])continue;
			add_edge(i,j+a,1);
			ind[i][j]=D_G[i].size()-1;
		}
		max_flow(st,go);
		for(int i=0;i<a;i++)for(int j=0;j<a;j++){
			if(~ind[i][j]&&D_G[i][ind[i][j]].c==0){
				ans[i][j]++;
			}
		}

		for(int i=0;i<D_MAX_V;i++){
			D_G[i].clear();
			D_level[i]=D_iter[i]=0;
		}
		st=a*4;
		go=a*4+1;
		for(int i=0;i<2*a;i++){
			add_edge(st,i,1);
			add_edge(i+a*2,go,1);
		}
		for(int i=0;i<2*a;i++)for(int j=0;j<2*a;j++)ind[i][j]=-1;
		for(int i=0;i<2*a;i++)uc[i]=ur[i]=0;
		for(int i=0;i<a;i++){
			for(int j=0;j<a;j++){
				if(str[i][j]=='+'||str[i][j]=='o')ur[i+j]=uc[a+(i-j)]=1;
			}
		}
		for(int i=0;i<a;i++)for(int j=0;j<a;j++){
			if(ur[i+j]||uc[a+(i-j)])continue;
			add_edge(i+j,a*2+a+(i-j),1);
			ind[i][j]=D_G[i+j].size()-1;
		}
		max_flow(st,go);
		for(int i=0;i<a;i++)for(int j=0;j<a;j++){
			if(~ind[i][j]&&D_G[i+j][ind[i][j]].c==0){
				ans[i][j]+=2;
			}
		}
		int ret=0;
		int sz=0;
		for(int i=0;i<a;i++)for(int j=0;j<a;j++){
			if(str[i][j]=='o')ret+=2;
			if(str[i][j]=='x'||str[i][j]=='+')ret++;
			ret+=__builtin_popcount(ans[i][j]);
			if(ans[i][j])sz++;
		}
		printf("Case #%d: %d %d\n",t,ret,sz);
		for(int i=0;i<a;i++)for(int j=0;j<a;j++){
			if(ans[i][j]){
				if(ans[i][j]==3||(ans[i][j]==2&&str[i][j]=='x')||(ans[i][j]==1&&str[i][j]=='+'))printf("o");
				else if(str[i][j]=='.'&&ans[i][j]==1)printf("x");
				else printf("+");
				printf(" %d %d\n",i+1,j+1);
			}
		}
	}
}