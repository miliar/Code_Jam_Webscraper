#include <cstdio>
#include <cstring>
#include <cmath>
#include <iostream>
#include <cstdlib>
#include <queue>
#include <map>
#include <stack>
#include <set>
#define maxn 1009
#define maxm 100000
using namespace std;
int n, C, m;
char s[maxn][maxn];
int L1[maxn][maxn], R1[maxn][maxn],L2[maxn][maxn], R2[maxn][maxn];
bool vis[maxn][maxn];
bool ed[maxn][maxn];
bool beamer(int x, int y){
	return s[x][y] == '|' || s[x][y] == '-';
}
void solve(int x, int y){
	//cout << x << " " << y << endl;
	bool f1 = 0, f2 = 0;
	int l1, r1, l2, r2;
	for(l1 = y; l1 >= 0; l1--){
		if(s[x][l1] == '#')
			break;
		if(beamer(x, l1) && l1 != y)
			f1 = 1;
	}
	l1++;
	for(r1 = y; r1 < m; r1++){
		if(s[x][r1] == '#')
			break;
		if(beamer(x, r1) && r1 != y)
			f1 = 1;
	}
	r1--;
	for(l2 = x; l2 >= 0; l2--){
		if(s[l2][y] == '#')
			break;
		if(beamer(l2, y) && l2 != x)
			f2 = 1;
	}
	l2++;
	for(r2 = x; r2 < n; r2++){
		if(s[r2][y] == '#')
			break;
		if(beamer(r2, y) && r2 != x)
			f2 = 1;
	}
	r2--;
	L1[x][y] = l1;
	R1[x][y] = r1;
	L2[x][y] = l2;
	R2[x][y] = r2;
	if(l1 == r1 && l2 == r2)
		ed[x][y] = 1;
	else if(f1){
		s[x][y] = '|';
		ed[x][y] = 1;
	}
	else if(f2){
		s[x][y] = '-';
		ed[x][y] = 1;
	}
	else if(l1 == r1){
		s[x][y] = '|';
		ed[x][y] = 1;
	}
	else if(l2 == r2){
		s[x][y] = '-';
		ed[x][y] = 1;
	}
}

bool bea(int x, int y){
	return s[x][y] == '.' && vis[x][y] == 0;
}
void doit(int x, int y){
	bool f1 = 0, f2 = 0;
	int l1, r1, l2, r2;
	for(l1 = y; l1 >= 0; l1--){
		if(s[x][l1] == '#')
			break;
		if(bea(x, l1) && l1 != y)
			f1 = 1;
	}
	l1++;
	for(r1 = y; r1 < m; r1++){
		if(s[x][r1] == '#')
			break;
		if(bea(x, r1) && r1 != y)
			f1 = 1;
	}
	r1--;
	for(l2 = x; l2 >= 0; l2--){
		if(s[l2][y] == '#')
			break;
		if(bea(l2, y) && l2 != x)
			f2 = 1;
	}
	l2++;
	for(r2 = x; r2 < n; r2++){
		if(s[r2][y] == '#')
			break;
		if(bea(r2, y) && r2 != x)
			f2 = 1;
	}
	r2--;
	L1[x][y] = l1;
	R1[x][y] = r1;
	L2[x][y] = l2;
	R2[x][y] = r2;
	if(f1)
		s[x][y] = '-';
	else
		s[x][y] = '|';
}
void setvis(){
	memset(vis, 0, sizeof(vis));
	for(int i = 0; i < n; i++){
		for(int j = 0; j < m; j++){
			if(!ed[i][j])
				continue;
			if(s[i][j] == '|'){
				for(int k = L2[i][j]; k <= R2[i][j]; k++)
					if(k != i)
						vis[k][j] = 1;
			}
			if(s[i][j] == '-'){
				for(int k = L1[i][j]; k <= R1[i][j]; k++)
					if(k != j)
						vis[i][k] = 1;
			}
		}
	}
}

bool check(){
	memset(vis, 0, sizeof(vis));
	for(int i = 0; i < n; i++){
		for(int j = 0; j < m; j++){
			if(s[i][j] == '|'){
				for(int k = L2[i][j]; k <= R2[i][j]; k++)
					if(k != i)
						vis[k][j] = 1;
			}
			if(s[i][j] == '-'){
				for(int k = L1[i][j]; k <= R1[i][j]; k++)
					if(k != j)
						vis[i][k] = 1;
			}
		}
	}
	for(int i = 0; i < n; i++){
		for(int j = 0; j < m; j++){
			if(vis[i][j]){
				if(beamer(i ,j))
					return 0;
			}
			else{
				if(s[i][j] == '.')
					return 0;
			}
		}
	}
	return 1;
}
int main(){
	freopen("/Users/fengweiming/ProgramContest/GoogleCodeJam2017/Round2/A.in", "r", stdin);
	freopen("/Users/fengweiming/ProgramContest/GoogleCodeJam2017/Round2/A.out", "w", stdout);
	int tt, cot = 1;
	cin >> tt;
	while(tt--){
		memset(ed, 0, sizeof(ed));
		bool ok = 1;
		cin >> n >> m;
		for(int i = 0; i < n; i++)
			scanf("%s", s[i]);
		for(int i = 0; i < n; i++){
			for(int j = 0; j < m; j++){
				if(s[i][j] == '|' || s[i][j] == '-'){
					solve(i, j);
				}
			}
		}
		setvis();
		for(int i = 0; i < n; i++){
			for(int j = 0; j < m; j++){
				if(s[i][j] == '|' || s[i][j] == '-'){
					if(ed[i][j] == 0)
						doit(i, j);
				}
			}
		}
		//cout << ok << endl;
		if(!check())ok = 0;
		if(ok){
			printf("Case #%d: POSSIBLE\n", cot++);
			for(int i = 0; i < n; i++)
				puts(s[i]);
		}
		else{
			printf("Case #%d: IMPOSSIBLE\n", cot++);
		}
	}
	return 0;
}