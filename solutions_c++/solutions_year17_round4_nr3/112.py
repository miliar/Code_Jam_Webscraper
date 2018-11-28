#include <cstdlib>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <queue>
#include <cmath>
#include <stack>
#include <map>
#include <set>
#include <deque>
#include <cstring>
#include <functional>
#include <climits>
#include <list>
#include <ctime>
#include <complex>

#define F1(x,y,z) for(int x=(y);x<(z);x++)
#define F2(x,y,z) for(int x=(y);x<=(z);x++)
#define F3(x,y,z) for(int x=(y);x>(z);x--)
#define F4(x,y,z) for(int x=(y);x>=(z);x--)
#define mp make_pair
#define pb push_back
#define LL long long
#define co complex<double>
#define fi first
#define se second

#define MAX 100005
#define AMAX 1025*1005
#define MOD 1000000007

#define f(c,d) ((1<<(c))*(d))

using namespace std;

int t,n,m,di,tx,ty,id[55][55],ids,sat[205],vis[205];
char x[55][55];
int dx[]={0,0,1,-1};
int dy[]={1,-1,0,0};
bool ok,oo,vv[205];
vector<int> to[205],he[55][55],hee;

bool dfs1(int a){
	if(vis[a]==1||sat[a]==1)return 1;
	if(vis[a]==2||sat[a]==2)return 0;
	vis[a]=1;
	vis[a^1]=2;
	F1(b,0,to[a].size())if(!dfs1(to[a][b]))return 0;
	return 1;
}

void dfs2(int a){
	if(sat[a]==1)return;
	sat[a]=1;
	sat[a^1]=2;
	F1(b,0,to[a].size())dfs2(to[a][b]);
}

int main(){
	scanf("%d",&t);
	F2(a,1,t){
		F1(b,0,205)to[b].clear();
		memset(id,0,sizeof(id));
		ids=0;
		ok=1;
		scanf("%d%d",&n,&m);
		F1(b,0,n)scanf("%s",x[b]);
		F1(b,0,n)F1(c,0,m)he[b][c].clear();
		F1(b,0,n)F1(c,0,m)if(x[b][c]=='|'||x[b][c]=='-'){
			id[b][c]=++ids;
			F1(d,0,2){
				oo=1;
				F1(e,0,2)if(oo){
					di=d*2+e;
					tx=b+dx[di],ty=c+dy[di];
					while(1){
						if(tx<0||ty<0||tx>=n||ty>=m||x[tx][ty]=='#')break;
						if(x[tx][ty]=='|'||x[tx][ty]=='-'){
							oo=0;
							break;
						}
						if(x[tx][ty]=='/')di=3-di;
						else if(x[tx][ty]=='\\')di=(di+2)%4;
						else he[tx][ty].pb(ids*2+d);
						tx+=dx[di];
						ty+=dy[di];
					}
				}
				vv[ids*2+d]=oo;
				if(!oo)to[ids*2+d].pb(ids*2+(1-d));
			}
		}
		F1(b,0,n)F1(c,0,m)if(x[b][c]=='.'){
			hee.clear();
			F1(d,0,he[b][c].size())if(vv[he[b][c][d]])hee.pb(he[b][c][d]);
			if(hee.empty()){
				ok=0;
				break;
			}else if(hee.size()==1)to[hee[0]^1].pb(hee[0]);
			else{
				to[hee[0]^1].pb(hee[1]);
				to[hee[1]^1].pb(hee[0]);
			}
		}
		/*
		F2(b,1,ids)F1(c,0,2){
			printf("%d: ",b*2+c);
			F1(d,0,to[b*2+c].size())printf(" %d",to[b*2+c][d]);
			printf("\n");
		}
		*/
		memset(sat,0,sizeof(sat));
		if(ok)F2(b,1,ids){
			memset(vis,0,sizeof(vis));
			if(dfs1(b*2))dfs2(b*2);
			else{
				memset(vis,0,sizeof(vis));
				if(dfs1(b*2+1))dfs2(b*2+1);
				else{
					ok=0;
					break;
				}
			}
		}
		F1(b,0,n)F1(c,0,m)if(id[b][c]){
			if(sat[id[b][c]*2]==1)x[b][c]='-';
			else x[b][c]='|';
		}
		if(ok){
			printf("Case #%d: POSSIBLE\n",a);
			F1(b,0,n)printf("%s\n",x[b]);
		}else printf("Case #%d: IMPOSSIBLE\n",a);
	}
	return 0;
}
