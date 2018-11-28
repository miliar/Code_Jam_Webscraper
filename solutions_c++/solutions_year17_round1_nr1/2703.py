#include <cstdio>
#include <cstring>
#include <cmath>
#include <iostream>
#include <cstdlib>
#include <iostream>
#include <queue>
#define maxn 50
using namespace std;
const int INF = 1e7;
char s[50][50];
int n ,m;
int L[maxn], R[maxn], U[maxn], D[maxn];
int dx[]={0,0,1,-1};
int dy[]={1,-1,0,0};
void pant(){
	for(int x = 0; x < 26; x++){
		if(L[x] > R[x])
			continue;
		for(int i = U[x]; i <= D[x]; i++)
			for(int j = L[x]; j <= R[x]; j++)
				s[i][j] = 'A' + x;
	}
}
bool in(int x, int y){
	return 0 <= x && x < n && 0 <= y && y < m;
}

bool checkcol(int c, int x, int y){
	for(int i = x; i <= y; i++)
		if(s[i][c] != '?')
			return 0;
	return 1;
}

bool checkrow(int c, int x, int y){
	for(int i = x; i <= y; i++)
		if(s[c][i] != '?')
			return 0;
	return 1;
}

void bfs(){
	queue<pair<int,int> > Q;
	for(int i = 0 ; i <n ; i++)
		for(int j = 0; j <m; j++)
			if(s[i][j] != '?')
				Q.push(make_pair(i,j));
	while(!Q.empty()){
		int x = Q.front().first;
		int y = Q.front().second;
		Q.pop();
		int cur = s[x][y] - 'A';
		for(int i = 0 ; i < 2; i++){
			int nx = x + dx[i];
			int ny = y + dy[i];
			if(!in(nx, ny))
				continue;
			if(s[nx][ny] != '?')
				continue;
			if(checkcol(ny, U[cur], D[cur])){
				for(int j = U[cur]; j <= D[cur]; j++){
					s[j][ny] = cur + 'A';
					Q.push(make_pair(j, ny));}
				R[cur] = max(R[cur], ny);
				L[cur] = min(L[cur], ny);
			}
		}
		for(int i = 2 ; i < 4; i++){
			int nx = x + dx[i];
			int ny = y + dy[i];
			if(!in(nx, ny))
				continue;
			if(s[nx][ny] != '?')
				continue;
			if(checkrow(nx, L[cur], R[cur])){
				for(int j = L[cur]; j <= R[cur]; j++){
					s[nx][j] = cur + 'A';
					Q.push(make_pair(nx, j));}
				U[cur] = min(U[cur], nx);
				D[cur] = max(D[cur], nx);
			}
		}
	}
}
int main(){
	freopen("/Users/fengweiming/ProgramContest/GoogleCodeJam2017/Round1A/A.in", "r", stdin);
	freopen("/Users/fengweiming/ProgramContest/GoogleCodeJam2017/Round1A/A.out", "w", stdout);
	int tt, cot = 1;
	scanf("%d", &tt);
	while(tt--){
		scanf("%d%d", &n , &m);
		for(int i = 0; i < n; i++)
			scanf("%s", s[i]);
			
		for(int i= 0 ; i< maxn;i++){
			L[i] = INF;
			R[i] = -INF;
			U[i] = INF;
			D[i] = -INF;
		}
		
		for(int i = 0; i <n ; i++){
			for(int j = 0; j <m ;j++){
				if(s[i][j] == '?')
					continue;
				else{
					int x = s[i][j] - 'A';
					L[x] = min(L[x], j);
					R[x] = max(R[x], j);
					U[x] = min(U[x], i);
					D[x] = max(D[x], i);
				}
			}
		}
		pant();
		bfs();
		printf("Case #%d:\n", cot++);
		for(int i = 0 ; i <n ;i++)
			puts(s[i]);
	}
	return 0;
}
