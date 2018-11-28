#include <stdio.h>
#include <algorithm>
#include <vector>
#include <queue>
#include <stack>
#include <set>
#include <map>
using namespace std;

vector<int> Graph[6060],Reverse[6060];
stack<int> Stack,End;
queue<int> Queue;

int V,Chk[6060],Group[6060],Res[6060],Cnt;

int Not(int x){ return (x + V) % (2 * V); }

void in(int x, int y)
{
	Graph[Not(x)].push_back(y);
	Graph[Not(y)].push_back(x);
	Reverse[y].push_back(Not(x));
	Reverse[x].push_back(Not(y));
}

void dfs()
{
	for (int k=0;k<V*2;k++) Chk[k] = 0;
	for (int k=0;k<V*2;k++) if (Chk[k] == 0){
		Stack.push(k); while (!Stack.empty()){
			int x = Stack.top(); Chk[x] = 1;

			int i = 0;
			for (auto &y : Graph[x]){
				if (Chk[y] == 0){
					Stack.push(y); break;
				}
				i++;
			}

			if (i == Graph[x].size()){
				End.push(x); Stack.pop();
			}
		}
	}
}

void bfs()
{
	for (int i=0;i<V*2;i++) Res[i] = 2;
	while (!End.empty()){
		int k = End.top(); End.pop();
		if (Chk[k] != 1) continue;
		Cnt++;

		Queue.push(k); Chk[k] = 2;
		while (!Queue.empty()){
			int x = Queue.front(); Queue.pop(); Group[x] = Cnt;
			if (Res[x] == 2){
				Res[x] = 0; Res[Not(x)] = 1;
			}

			for (auto &y : Reverse[x]){
				if (Chk[y] == 1){
					Queue.push(y); Chk[y] = 2;
				}
			}
		}
	}
}

void proc()
{
	for (int i=0;i<6060;i++){
		Graph[i].clear();
		Reverse[i].clear();
	}

	char S[55][55];
	int N,M;
	scanf ("%d %d",&N,&M);
	for (int i=0;i<N;i++) scanf ("%s",S[i]);

	vector<pair<int, int> > pos;
	int dx[4] = {0,1,0,-1};
	int dy[4] = {1,0,-1,0};
	
	int u[55][55][4], C[55][55];
	for (int i=0;i<N;i++) for (int j=0;j<M;j++) for (int k=0;k<4;k++) u[i][j][k] = -1;

	V = 0;
	for (int i=0;i<N;i++) for (int j=0;j<M;j++) if (S[i][j] == '|' || S[i][j] == '-') C[i][j] = V++;

	for (int i=0;i<N;i++) for (int j=0;j<M;j++) if (S[i][j] == '|' || S[i][j] == '-'){
		int c = pos.size(); pos.push_back({i,j});

		for (int k=0;k<4;k++){
			int x = i, y = j, d = k;
			while (1){
				x += dx[d], y += dy[d];
				if (x == i && y == j){
					puts("IMPOSSIBLE"); return;
				}
				if (x < 0 || x >= N || y < 0 || y >= M) break;
				if (S[x][y] == '|' || S[x][y] == '-' || S[x][y] == '#') break;
				if (k % 2) u[x][y][k] = Not(c);
				else u[x][y][k] = c;
				if (S[x][y] == '\\') d ^= 1;
				if (S[x][y] == '/') d ^= 3;
			}
		}
	}
	for (int i=0;i<N;i++) for (int j=0;j<M;j++) if (S[i][j] == '.'){
		int g[2] = {0,};
		for (int k=0;k<2;k++){
			if (u[i][j][k] != -1 && u[i][j][k+2] != -1){
				in(Not(u[i][j][k]), Not(u[i][j][k]));
				in(Not(u[i][j][k+2]), Not(u[i][j][k+2]));
				g[k] = 1;
			}
		}
		if (g[0] && g[1]){puts("IMPOSSIBLE"); return;}
		if (g[0]){
			int b = u[i][j][1] == -1 ? u[i][j][3] : u[i][j][1];
			if (b == -1){puts("IMPOSSIBLE"); return;}
			in(b,b);
		}
		if (g[1]){
			int a = u[i][j][0] == -1 ? u[i][j][2] : u[i][j][0];
			if (a == -1){puts("IMPOSSIBLE"); return;}
			in(a,a);
		}
		if (!g[0] && !g[1]){
			int a = u[i][j][0] == -1 ? u[i][j][2] : u[i][j][0];
			int b = u[i][j][1] == -1 ? u[i][j][3] : u[i][j][1];
			if (a == -1 && b == -1){puts("IMPOSSIBLE"); return;}
			else if (a == -1) in(b,b);
			else if (b == -1) in(a,a);
			else in(a,b);
		}
	}
	for (int i=0;i<N;i++) for (int j=0;j<M;j++) if (S[i][j] == '\\'){
		for (int k=0;k<4;k+=2){
			if (u[i][j][k] != -1 && u[i][j][k^3] != -1){
				in(Not(u[i][j][k]), Not(u[i][j][k]));
				in(Not(u[i][j][k^3]), Not(u[i][j][k^3]));
			}
		}
	}
	for (int i=0;i<N;i++) for (int j=0;j<M;j++) if (S[i][j] == '/'){
		for (int k=0;k<4;k+=2){
			if (u[i][j][k] != -1 && u[i][j][k^1] != -1){
				in(Not(u[i][j][k]), Not(u[i][j][k]));
				in(Not(u[i][j][k^1]), Not(u[i][j][k^1]));
			}
		}
	}
	for (int i=0;i<N;i++) for (int j=0;j<M;j++) if (S[i][j] == '|' || S[i][j] == '-'){
		if (i + 1 < N && (S[i+1][j] == '|' || S[i+1][j] == '-')){
			in(C[i][j],C[i][j]);
			in(C[i+1][j],C[i+1][j]);
		}
		if (j + 1 < M && (S[i][j+1] == '|' || S[i][j+1] == '-')){
			in(C[i][j]+V,C[i][j]+V);
			in(C[i][j+1]+V,C[i][j+1]+V);
		}
	}

	dfs(); bfs();

	for (int i=0;i<V;i++){
		if (Group[i] == Group[i+V]){puts("IMPOSSIBLE"); return;}
		int x = pos[i].first, y = pos[i].second;
		if (Res[i]) S[x][y] = '-';
		else S[x][y] = '|';
	}

	puts("POSSIBLE");
	for (int i=0;i<N;i++) puts(S[i]);
}

int main()
{
	freopen ("input.txt","r",stdin);
	freopen ("output.txt","w",stdout);

	int Test; scanf ("%d",&Test); for (int Case=1;Case<=Test;Case++){
		printf ("Case #%d: ",Case);
		proc();
	}

	return 0;
}