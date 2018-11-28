#include<stdio.h>
#include<memory.h>
#include<algorithm>
#include<vector>
using namespace std;

int R, C; char mp[55][55];
int bin[55][55], bcn, occ[3000][2];
int lcn, las[3000][2];

int jang=0, chk, xx[4]={-1,1,0,0}, yy[4]={0,0,-1,1};
int mir1[4]={3,2,1,0}, mir2[4]={2,3,0,1};
void bfs(int x, int y, int dir, int typ){ // UDLR
	if(chk>1)return;
	if(x<0 || y<0 || x>=R || y>=C) return;
	if(mp[x][y]=='#')return;
	if(mp[x][y]=='.') occ[bin[x][y]][dir/2] = typ;
	if(mp[x][y]=='-' || mp[x][y]=='|'){
		if(las[typ/2][0] == x && las[typ/2][1] == y){
			if(chk){ chk=2; return; }
			chk=1;
		}
		else jang++;
	}
	if(mp[x][y]=='/') dir=mir1[dir];
	if(mp[x][y]=='\\') dir=mir2[dir];
	bfs(x+xx[dir], y+yy[dir], dir, typ);
}

vector<int> con[3030], crv[3030];
void make_edge(int s, int e){
	con[s].push_back(e); crv[e].push_back(s);
//	printf("%d(%d) -> %d(%d)\n", s/2, s%2, e/2, e%2);
}

int chk2[3030], ord[3030], ocn, col[3030], ccn, TF[3030];
vector<int> cc[3030];
void dfs1(int ix){
	if(chk2[ix])return;
	chk2[ix]=1;
	for(int i=0; i<con[ix].size(); i++) dfs1(con[ix][i]);
	ord[ocn++]=ix;
}
void dfs2(int ix){
	if(col[ix])return;
	col[ix]=ccn; cc[ccn].push_back(ix);
	for(int i=0; i<crv[ix].size(); i++) dfs2(crv[ix][i]);
}

void test(int tn){
	scanf("%d%d\n", &R, &C);
	bcn=lcn=0; memset(occ, 0, sizeof(occ));
	for(int i=0; i<R; i++)gets(mp[i]);
	printf("Case #%d: ", tn);

	for(int i=0; i<3000; i++)con[i].clear(), cc[i].clear(), crv[i].clear();

	for(int i=0; i<R; i++){
		for(int j=0; j<C; j++){
			if(mp[i][j]=='.') bin[i][j]=++bcn;
		}
	}
	for(int i=0; i<R; i++){
		for(int j=0; j<C; j++){
			if(mp[i][j]=='-' || mp[i][j]=='|'){
				lcn++;
				las[lcn][0]=i, las[lcn][1]=j;
				jang=0;
				chk=0, bfs(i, j, 0, 2*lcn), chk=0, bfs(i, j, 1, 2*lcn); // 2i : UD
				if(jang) make_edge(2*lcn, 2*lcn+1); // lcn->~lcn
				if(chk==2){ puts("IMPOSSIBLE"); return; }
				jang=0;
				chk=0, bfs(i, j, 2, 2*lcn+1), chk=0, bfs(i, j, 3, 2*lcn+1); // 2i+1 : LR
				if(jang) make_edge(2*lcn+1, 2*lcn); // ~lcn->lcn
				if(chk==2){ puts("IMPOSSIBLE"); return; }
			}
		}
	}
	for(int i=1; i<=bcn; i++){
		if(occ[i][0]==0) swap(occ[i][0], occ[i][1]);
		if(occ[i][0]==0) { puts("IMPOSSIBLE"); return; }
		if(occ[i][1]==0) make_edge(occ[i][0]^1, occ[i][0]); // ~a->a
		else make_edge(occ[i][0]^1, occ[i][1]), make_edge(occ[i][1]^1, occ[i][0]); // ~a->b, ~b->a
	}

	// SCC
	memset(chk2, 0, sizeof(chk2)), memset(col, 0, sizeof(col));
	memset(TF, -1, sizeof(TF));
	ccn=ocn=0;
	for(int i=2; i<=2*lcn+1; i++) dfs1(i);
	for(int i=ocn-1; i>=0; i--){
		if(col[ord[i]]) continue;
		ccn++;
		dfs2(ord[i]);
	}
	for(int i=ocn-1; i>=0; i--){
		int c = col[ord[i]];
		if(TF[c]<0){
			TF[c]=0;
			for(int j=0; j<cc[c].size(); j++){
				int s=cc[c][j];
				if(TF[col[s^1]] == 0){ TF[c]=1; break; }
			}
		}
		if(!TF[c])continue;
		for(int j=0; j<cc[c].size(); j++){
			int s=cc[c][j];
			for(int k=0; k<con[s].size(); k++){
				int e=con[s][k];
				TF[col[e]]=1;
			}
		}
	}
	for(int i=1; i<=lcn; i++){
//		printf("[%d %d] ", col[i*2], col[i*2+1]);
		if(TF[col[i*2]] == TF[col[i*2+1]]){ puts("IMPOSSIBLE"); return; }
		if(TF[col[i*2]]) mp[las[i][0]][las[i][1]] = '|';
		else mp[las[i][0]][las[i][1]] = '-';
	}
	puts("POSSIBLE");
	for(int i=0; i<R; i++)puts(mp[i]);
}

int main(){
//	freopen("input.txt","r",stdin), freopen("output.txt","w",stdout);
	freopen("C-small-attempt2.in","r",stdin), freopen("output.txt","w",stdout);
	int t, i;
	scanf("%d", &t);
	for(int i=1; i<=t; i++) test(i);
	return 0;
}
