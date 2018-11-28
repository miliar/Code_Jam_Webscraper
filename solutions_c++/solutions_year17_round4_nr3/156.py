#include<stdio.h>
#include<string.h>
#include<vector>
using namespace std;
int row,col;
char s[111][111];
const int dx[4]={-1,0,1,0};
const int dy[4]={0,-1,0,1};
int n;
vector<int> ctrl[111][111];
int rev(int x){
	return x >= n ? x - n : x + n;
}

#define ran 44444
namespace sat_2_solver{
	vector<int> e[ran],_e[ran];
	vector<int> _e2[ran];
	int n,m;
	int col[ran],to[ran],deg[ran],rv[ran];
	bool mark[ran];
	int ord[ran],t;
	int q[ran],op,cl;
	void init(int _n){
		n = _n;
		for(int i=0; i<2*n; i++){
			e[i].clear();
			_e[i].clear();
			_e2[i].clear();
		}
		memset(col,0,sizeof(col));
		m = 0;
		memset(to,0,sizeof(to));
		memset(deg,0,sizeof(deg));
		memset(rv,0,sizeof(rv));
		memset(mark,0,sizeof(mark));
		memset(ord,0,sizeof(ord));
		t = 0;
		memset(q,0,sizeof(q));
		op = cl = 0;
	}
	void dfs(int x){
		if(mark[x])return;
		mark[x] = true;
		for(vector<int>::iterator it=e[x].begin(); it!=e[x].end(); it++)
			dfs(*it);
		ord[t++] = x;
	}
	void _dfs(int x){
		if(!mark[x])return;
		mark[x] = false;
		for(vector<int>::iterator it=_e[x].begin(); it!=_e[x].end(); it++)
			_dfs(*it);
		to[x] = m;
	}
	bool solve(){
		t=0;
		for(int i=0; i<2*n; i++)
			_e[i].clear();
		for(int i=0; i<2*n; i++){
			for(vector<int>::iterator it=e[i].begin(); it!=e[i].end(); it++)
				_e[*it].push_back(i);
		}
		for(int i=0; i<2*n; i++){
			dfs(i);
		}
		m=0;
		while(t--){
			int x = ord[t];
			_dfs(x);
			m++;
		}
		for(int i=0; i<n; i++)
			if(to[i] == to[i+n])
				return false;
		for(int i=0; i<m; i++){
			_e2[i].clear();
			deg[i] = 0;
		}
		for(int i=0; i<2*n; i++){
			for(vector<int>::iterator it=e[i].begin(); it!=e[i].end(); it++){
				if(to[i] == to[*it])continue;
				_e2[to[*it]].push_back(to[i]);
				++deg[to[i]];
			}
			rv[to[i]] = to[i>=n?i-n:i+n];
		}
		op=cl=0;
		for(int i=0; i<m; i++){
			if(deg[i] == 0)
				q[op++] = i;
		}
		while(cl<op){
			int x = q[cl++];
			if(col[x] == 0){
				col[x] = 1;
				col[rv[x]] = -1;
			}
			for(vector<int>::iterator it=_e2[x].begin(); it!=_e2[x].end(); it++){
				int y=*it;
				if(--deg[y] == 0)
					q[op++] = y;
			}
		}
		return true;
	}
}

bool process(){
	sat_2_solver::init(n);
	int w = 0;
	for(int i=0; i<row; i++)for(int j=0; j<col; j++)ctrl[i][j].clear();

	for(int i=0; i<row; i++)
	for(int j=0; j<col; j++){
		if(s[i][j] != 'T')continue;
		bool hor = true, ver = true;
		for(int k=0; k<4; k++){
			int x = i, y = j;
			while(1){
				x += dx[k];
				y += dy[k];
				if(x >= 0 && x < row && y >= 0 && y < col){
					if(s[x][y] == 'T' || s[x][y] == '#')
						break;
				}else
					break;
			}
			if(x >= 0 && x < row && y >= 0 && y < col && s[x][y] == 'T'){
				if(k == 0 || k == 2)ver = false;else
					hor = false;
			}
		}
		if(!hor && !ver)return false;
		if(!hor && ver){
			sat_2_solver::e[rev(w)].push_back(w);
		}
		if(!ver && hor){
			sat_2_solver::e[w].push_back(rev(w));
		}
		for(int k=0; k<4; k++){
			if((k == 0 || k == 2) && !ver)continue;
			if((k == 1 || k == 3) && !hor)continue;
			int x = i, y = j;
			while(1){
				x += dx[k];
				y += dy[k];
				if(x >= 0 && x < row && y >= 0 && y < col){
					if(s[x][y] == 'T' || s[x][y] == '#')
						break;
					ctrl[x][y].push_back(w + (k==1||k==3?n:0));
				}else
					break;
			}
		}
		w++;
	}
	for(int i=0; i<row; i++)
	for(int j=0; j<col; j++){
		if(s[i][j] != 'n')continue;
		if(ctrl[i][j].size() == 1){
			int A = ctrl[i][j][0];
			sat_2_solver::e[rev(A)].push_back(A);
		}else
		if(ctrl[i][j].size() == 0){
			return false;
		}else{
			int A = ctrl[i][j][0], B = ctrl[i][j][1];
			sat_2_solver::e[rev(A)].push_back(B);
			sat_2_solver::e[rev(B)].push_back(A);
		}
	}
	w = 0;
	if(!sat_2_solver::solve())return false;
	for(int i=0; i<row; i++)
	for(int j=0; j<col; j++){
		if(s[i][j] != 'T'){
			if(s[i][j] == 'n')s[i][j] = '.';
			continue;
		}
		int u = sat_2_solver::col[sat_2_solver::to[w]];
		int l = sat_2_solver::col[sat_2_solver::to[w+n]];
		if(u == 1){
			s[i][j] = '|';
		}else{
			s[i][j] = '-';
		}
		w++;
	}
	return true;
}

int main(){
	int _;
	scanf("%d",&_);
	for(int T=1; T<=_; T++){

	scanf("%d%d",&row,&col);
	n=0;
	for(int i=0; i<row; i++){
		scanf("%s",s[i]);
		for(int j=0; j<col; j++)
			if(s[i][j] == '-' || s[i][j] == '|'){
				s[i][j] = 'T';
				n++;
			}
			else
			if(s[i][j] == '.')
				s[i][j] = 'n';
	}
	printf("Case #%d: ",T);

	if(!process()){
		puts("IMPOSSIBLE");
	}
	else{
		puts("POSSIBLE");
		for(int i=0; i<row; i++)
			puts(s[i]);
	}
	}
	return 0;
}
