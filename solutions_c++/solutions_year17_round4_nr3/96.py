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
const double EPS=1e-10;
const double PI=acos(-1.0);
int ABS(int a){return max(a,-a);}
long long ABS(long long a){return max(a,-a);}
char in[60][60];

vector<int>g[5100];
vector<int>rev[5100];
int v[5100]; // used twice
int num[5100]; // inverse of conv
int conv[5100]; // dfs order of i-th vertex. note that it's kaerigake ordered
int scc[5100]; // the index of scc containing i-th vertex
int fi[5100]; // the first element of each scc
int ss[5100]; // size of each scc
int cur;
void dfs(int a){
	for(int i=0;i<g[a].size();i++){
		if(v[g[a][i]])continue;
		v[g[a][i]]=1;
		dfs(g[a][i]);
	}
	conv[a]=cur;
	num[cur++]=a;
}
void dfs2(int a){
	scc[a]=cur;
	ss[cur]++;
	for(int i=0;i<rev[a].size();i++){
		if(v[rev[a][i]])continue;
		v[rev[a][i]]=1;
		dfs2(rev[a][i]);
	}
}
int H,W;
int dx[]={0,1,0,-1};
int dy[]={1,0,-1,0};

void ae(int a,int b){
	g[a].push_back(b);
	rev[b].push_back(a);
}
int vis[60][60][4];
int ser(int a,int b,int dir){
	vis[a][b][dir]=1;
	a+=dx[dir];
	b+=dy[dir];
	if(a<0||b<0||a>=H||b>=W||in[a][b]=='#')return -1;
	if(in[a][b]=='-'||in[a][b]=='|')return a*W+b;
	if(in[a][b]=='/')dir^=3;
	if(in[a][b]=='\\')dir^=1;
	if(vis[a][b][dir])return -1;
	return ser(a,b,dir);
}
void cls(){
	for(int i=0;i<H;i++)for(int j=0;j<W;j++)for(int k=0;k<4;k++)
		vis[i][j][k]=0;
}
int main(){
	int T;
	scanf("%d",&T);
	for(int t=1;t<=T;t++){
		int a,b;
		scanf("%d%d",&a,&b);
		H=a;W=b;
		for(int i=0;i<a;i++)scanf("%s",in[i]);
		int N=a*b;
		for(int i=0;i<5100;i++){
			g[i].clear();
			rev[i].clear();
			v[i]=num[i]=conv[i]=scc[i]=fi[i]=ss[i]=0;
		}
		cur=0;
		bool dame=false;
		for(int i=0;i<a;i++)for(int j=0;j<b;j++){
			if(in[i][j]=='.'){
				cls();
				int left=ser(i,j,2);cls();
				int right=ser(i,j,0);cls();
				int up=ser(i,j,3);cls();
				int down=ser(i,j,1);
				bool ok=false;
				if((~left&&~right)||(!~left&&!~right)){
					ok=true;
					if((~up&&~down)||(!~up&&!~down))dame=true;
					else{
						ae(max(up,down),N+max(up,down));
						if(~left)ae(left,N+left);
						if(~right)ae(right,N+right);
					}
				}
				if((~up&&~down)||(!~up&&!~down)){
					ok=true;
					if((~left&&~right)||(!~left&&!~right))dame=true;
					else {
						ae(N+max(left,right),max(left,right));
						if(~up)ae(N+up,up);
						if(~down)ae(N+down,down);
					}
				}
				if(!ok){
					ae(N+max(left,right),N+max(up,down));
					ae(max(up,down),max(left,right));
				}
			}else if(in[i][j]=='|'||in[i][j]=='-'){
				cls();
				int left=ser(i,j,2);cls();
				int right=ser(i,j,0);cls();
				int up=ser(i,j,3);cls();
				int down=ser(i,j,1);
				if(~left||~right){
					ae(i*b+j,N+i*b+j);
				}
				if(~up||~down){
					ae(N+i*b+j,i*b+j);
				}
			}
		}
		for(int i=0;i<N*2;i++){
			if(v[i])continue;
			v[i]=1;
			dfs(i);
		}
		cur=0;
		for(int i=0;i<N*2;i++)v[i]=0;
		for(int i=N*2-1;i>=0;i--){
			if(v[num[i]])continue;
			v[num[i]]=1;
			fi[cur]=num[i];
			dfs2(num[i]);
			cur++;
		}

		printf("Case #%d: ",t);
		for(int i=0;i<N;i++){
			if(scc[i]==scc[i+N])dame=true;
		}
		if(dame){printf("IMPOSSIBLE\n");continue;}
		else printf("POSSIBLE\n");
		for(int i=0;i<H;i++){
			for(int j=0;j<W;j++){
				if(in[i][j]=='|'||in[i][j]=='-'){
					if(scc[i*b+j]>scc[i*b+j+N])in[i][j]='-';
					else in[i][j]='|';
				}
			}
		}
		for(int i=0;i<H;i++)printf("%s\n",in[i]);
	}
}