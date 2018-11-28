#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <memory.h>
#include <math.h>
#include <assert.h>
#include <queue>
#include <map>
#include <set>
#include <string>
#include <algorithm>
#include <iostream>
#include <functional>
#include <vector>
#include <stack>
#include <deque>

using namespace std;
typedef long long ll;
typedef pair<int, int> Pi;

#define Fi first
#define Se second
#define pb(x) push_back(x)
#define sz(x) (int)x.size()
#define rep(i, n) for(int i=0;i<n;i++)
#define repp(i, n) for(int i=1;i<=n;i++)
#define all(x) x.begin(), x.end()

#define ABS(x) (((x) > 0 ) ? (x) : (-(x)))
#define MAX2(x, y) (((x) > (y)) ? (x) : (y))
#define MIN2(x, y) (((x) < (y)) ? (x) : (y))

#define MAX3(x, y, z) ( (x) > (y)  ? ( (x) > (z) ? (x) : (z)  ) : ( (y) > (z) ? (y) : (z) )  )
#define MIN3(x, y, z) ( (x) < (y)  ? ( (x) < (z) ? (x) : (z)  ) : ( (y) < (z) ? (y) : (z) )  )
#define MID3(val1,val2,val3) MAX2(MIN2(MAX2(val1,val2),val3),MIN2(val1,val2))
#define geti1(X) scanf("%d",&X)
#define geti2(X,Y) scanf("%d%d",&X,&Y)
#define geti3(X,Y,Z) scanf("%d%d%d",&X,&Y,&Z)
#define geti4(X,Y,Z,W) scanf("%d%d%d%d",&X,&Y,&Z,&W)

#define GET_MACRO(_1,_2,_3,_4,NAME,...) NAME
#define geti(...) GET_MACRO(__VA_ARGS__, geti4, geti3, geti2, geti1) (__VA_ARGS__)
#define INF 987654321
#define IINF 4321987654321
#include <time.h>
int tc;int N,C,M,P;
char p[1050][1050];
bool inbound(int y, int x){
	if( y < 1 || x < 1 || y > N || x > M ) return false;
	return true;
}
map<Pi,int> mp; Pi pos[1050];
int fix[1050];
int xx[4] = {1,-1,0,0}, yy[4] = {0,0,1,-1}; vector<Pi> cand[150][150];
bool done[150][150];
bool chkdfs(int y, int x, int dir){
	if( !inbound(y,x) ) return true;
	if( p[y][x] == '|' || p[y][x] == '-' ) return false;
	if( p[y][x] == '#' ) return true;
	if( p[y][x] == '/' ){
		if( dir == 0 ) return chkdfs(y-1,x,3);
		if( dir == 1 ) return chkdfs(y+1,x,2);
		if( dir == 2 ) return chkdfs(y,x+1,0);
		if( dir == 3 ) return chkdfs(y,x-1,1);
	}
	if( p[y][x] == 92 ){
		if( dir == 0 ) return chkdfs(y+1,x,2);
		if( dir == 1 ) return chkdfs(y-1,x,3);
		if( dir == 2 ) return chkdfs(y,x-1,1);
		if( dir == 3 ) return chkdfs(y,x+1,0);
	}
	if( p[y][x] == '.' ){
		int ny = y + yy[dir]; int nx = x + xx[dir];
		return chkdfs(ny,nx,dir);
	}
}

Pi dfs(int y, int x, int dir){
	if( !inbound(y,x) ) return {-1,-1};
	if( p[y][x] == '|' || p[y][x] == '-' ){
		int c = mp[{y,x}];
		if( dir == 0 || dir == 1 ) return {c,1};
		if( dir == 2 || dir == 3 ) return {c,2};
	}
	if( p[y][x] == '#' ) return {-1,1};
	if( p[y][x] == '/' ){
		if( dir == 0 ) return dfs(y-1,x,3);
		if( dir == 1 ) return dfs(y+1,x,2);
		if( dir == 2 ) return dfs(y,x+1,0);
		if( dir == 3 ) return dfs(y,x-1,1);
	}
	if( p[y][x] == 92 ){
		if( dir == 0 ) return dfs(y+1,x,2);
		if( dir == 1 ) return dfs(y-1,x,3);
		if( dir == 2 ) return dfs(y,x-1,1);
		if( dir == 3 ) return dfs(y,x+1,0);
	}
	if( p[y][x] == '.' ){
		int ny = y + yy[dir]; int nx = x + xx[dir];
		return dfs(ny,nx,dir);
	}
}

void solve(){
	
	geti(N,M); 
	mp.clear();
	memset(p,0,sizeof p); memset(done,0,sizeof done);
	rep(i,1050) {
		pos[i] = {0,0};
		fix[i] = false;
	}
	rep(i,150) rep(j,150) cand[i][j].clear();
	repp(i,N) scanf("%s",p[i]+1);
	int cnt = 1;
	repp(i,N) repp(j,M){
		if( p[i][j] == '|' || p[i][j] =='-' ){
			pos[cnt] = {i,j};
			mp[{i,j}] = cnt; cnt ++;
		}
	}

	for(int i=1;i<=cnt;i++){
		int y = pos[i].Fi; int x = pos[i].Se;
		bool xp = chkdfs(y,x+1,0) & chkdfs(y,x-1,1);
		bool yp = chkdfs(y-1,x,3) & chkdfs(y+1,x,2);
		if( xp && yp ){
			fix[i] = 0;
		}
		else if( xp ){
			fix[i] = 1;
		}
		else if( yp ){
			fix[i] = 2;
		}
		else{
			printf("IMPOSSIBLE\n"); return;
		}
	}

	repp(i,N){
		repp(j,M)if(p[i][j]=='.'){
			rep(k,4){
				Pi res = dfs(i,j,k); if( res.Fi == -1 || res.Se == -1 ) continue;
				if( fix[res.Fi] != 0 && fix[res.Fi] != res.Se ) continue;
				if( fix[res.Fi] != 0 && fix[res.Fi] == res.Se ){
					done[i][j] = true; continue;
				}
				//printf("%d %d %d %d\n",i,j,res.Fi,res.Se);
				cand[i][j].push_back(res);
			}
		}
	}

	repp(i,N) repp(j,M)if(p[i][j]=='.' && done[i][j] == false){
		if( cand[i][j].size() == 0 ){
			printf("IMPOSSIBLE\n"); return;
		}
		if( cand[i][j].size() == 1 ){
			auto e = cand[i][j][0];
			if( fix[e.Fi] != 0 && fix[e.Fi] != e.Se ) continue;
			fix[e.Fi] = e.Se; done[i][j] = true; continue;
		}
		for(auto e : cand[i][j] ){
			if( fix[e.Fi] == e.Se ){
				done[i][j] = true; continue;
			}
		}
	}


	bool done1 = false;
	/*
	for(auto e : cand[1][1]){
		printf("%d %d %d\n",e.Fi,e.Se,fix[e.Fi]);
		printf("%d %d\n",pos[e.Fi].Fi, pos[e.Fi].Se);
	}
	*/
	done1 = true;
	repp(i,cnt) if( fix[i] == 0 ) fix[i] = 1;
	repp(i,N) repp(j,M)if(p[i][j]=='.' && done[i][j] == false){
		bool chk = false;
		for(auto e : cand[i][j] ){
			if( fix[e.Fi] == e.Se ){
				chk = true;
			}
		}
		done1 &= chk;
	}

	if( !done1 ) {
		printf("IMPOSSIBLE\n"); return;
	}
	printf("POSSIBLE\n");
	repp(i,N){
		repp(j,M){
			if( p[i][j] != '|' && p[i][j] != '-' ) printf("%c",p[i][j]);
			else{
				if( fix[mp[{i,j}]] == 1 ) printf("%c",'-');
				else printf("%c",'|');
			}
		}
		printf("\n");
	}
}

int main(){
	//freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	geti(tc);
	repp(t,tc){
		printf("Case #%d: ",t);
		solve();
	}
}
