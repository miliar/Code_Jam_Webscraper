#include"stdafx.h"
#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include<assert.h>
#include<ctime>
#include<queue>
#include<fstream>
#include<string>
using namespace std;

const int maxn = 110;
bool row[maxn];
bool col[maxn];
bool diag[3 * maxn];
bool antidiag[3 * maxn];
int mat[maxn][maxn];
int newmat[maxn][maxn];

struct flow_graph{
	int MAX_V, E, s, t, head, tail;
	int *cap, *to, *next, *last, *dist, *q, *now;
	int * ori;
	bool* visited;

	flow_graph(){}

	flow_graph(int V, int MAX_E){
		MAX_V = V; E = 0;
		cap = new int[2 * MAX_E], to = new int[2 * MAX_E], next = new int[2 * MAX_E];
		last = new int[MAX_V], q = new int[MAX_V], dist = new int[MAX_V], now = new int[MAX_V];
		visited = new bool[MAX_V];
		ori = new int[2 * MAX_E];
		fill(last, last + MAX_V, -1);
	}

	void clear(){
		fill(last, last + MAX_V, -1);
		E = 0;
	}
	void clear_flow(){
		for (int i = 0; i<E; i++) cap[i] = ori[i];
	}
	void print(){
		for (int i = 0; i<E; i++) cout << i << " " << to[i] << " " << cap[i] << " " << next[i] << endl;
		// for(int i=1;i<=MAX_V+1)
	}
	void add_edge(int u, int v, int uv, int vu = 0){
		ori[E] = uv, to[E] = v, cap[E] = uv, next[E] = last[u]; last[u] = E++;
		ori[E] = vu, to[E] = u, cap[E] = vu, next[E] = last[v]; last[v] = E++;
	}

	void checkCapacity(int n){
		//row:1,...,n;
		//col:n+1,...,2n
		//diag:2n+2,...,4n
		//antidiag:4n+1,...,6n-1

		//check rows
		for (int r = 1; r <= n; r++){
			for (int e = last[r]; e != -1; e = next[e]){
				int c = to[e];
				if (c > 2 * n || c < n + 1) continue;
				if (cap[e] == 0) {
					newmat[r][c-n] += 2;
				}
			}
		}
		//check diagonals
		for (int d = 2 * n + 2; d <= 4 * n; d++){
			for (int e = last[d]; e != -1; e = next[e]){
				int a = to[e];
				if (a > 6 * n-1 || a < 4*n + 1) continue;
				if (cap[e] == 0){
					int dia = d - 2 * n;
					int anti = a - 5 * n;
					int r = (dia + anti) / 2;
					int c = (dia - anti) / 2;
					newmat[r][c] += 1;
				}

			}
		}
	}

	bool bfs(){
		fill(dist, dist + MAX_V, -1);
		fill(visited, visited + MAX_V, false);
		head = tail = 0;

		q[tail] = t; ++tail;
		dist[t] = 0;
		visited[t] = true;
		while (head<tail){
			int v = q[head]; ++head;

			for (int e = last[v]; e != -1; e = next[e]){
				if (cap[e ^ 1]>0 && dist[to[e]] == -1){
					q[tail] = to[e]; ++tail;
					dist[to[e]] = dist[v] + 1;
					visited[to[e]] = true;
				}
			}
		}

		return dist[s] != -1;
	}

	int dfs(int v, int f){
		if (v == t) return f;

		for (int &e = now[v]; e != -1; e = next[e]){
			if (cap[e]>0 && dist[to[e]] == dist[v] - 1){
				int ret = dfs(to[e], min(f, cap[e]));

				if (ret>0){
					cap[e] -= ret;
					cap[e ^ 1] += ret;
					return ret;
				}
			}
		}

		return 0;
	}

	long long max_flow(int source, int sink){
		s = source; t = sink;
		long long f = 0;
		int x;

		while (bfs()){

			for (int i = 0; i<MAX_V; ++i) now[i] = last[i];

			while (true){
				x = dfs(s, INT_MAX);
				if (x == 0) break;
				f += x;
			}
		}

		return f;
	}
}G;


void build_graph(int n){
	G.clear();
	//row:1,...,n;
	//col:n+1,...,2n
	for (int r = 1; r <= n; r++){
		if (row[r]) continue;
		for (int c = 1; c <= n; c++){
			if (col[c])continue;
			G.add_edge(r, c + n, 1);
		}
	}
	//diag:2n+2,...,4n
	//antidiag:4n+1,...,6n-1
	for (int dia = 2; dia <= 2 * n; dia++){
		if (diag[dia])continue;
		for (int anti = 1 - n; anti <= n - 1; anti++){
			if (antidiag[anti + n]) continue;
			if ((dia + anti) % 2 != 0) continue;
			int r = (dia + anti) / 2;
			int c = (dia - anti) / 2;
			if (r <= 0 || r > n) continue;
			if (c <= 0 || c > n) continue;
			G.add_edge(dia + 2 * n, anti + 5 * n, 1);
		}
	}
	int source = 0;
	int sink = 6 * n;
	for (int i = 1; i <= n; i++){
		G.add_edge(source, i,1);
		G.add_edge(i + n, sink,1);
	}
	for (int i = 2; i <= 2 * n; i++){
		G.add_edge(source, 2 * n + i, 1);
		G.add_edge(4 * n - 1 + i, sink, 1);
	}
}

ifstream fin;
ofstream fout;

vector<pair<char, pair<int, int>>> vp;
void solve(int n,int a){
	int source = 0;
	int sink = 6 * n;
	build_graph(n);
	int ans = G.max_flow(source, sink);
	vp.clear();
	G.checkCapacity(n);
	for (int r = 1; r <= n; r++){
		for (int c = 1; c <= n; c++){
			if (newmat[r][c]!=0){
				//cout << r << " " << c << " " << newmat[r][c] << endl;
				char a;
				if (newmat[r][c]+mat[r][c] == 3) a = 'o';
				else if (newmat[r][c] + mat[r][c] == 2) a = 'x';
				else a = '+';
				vp.push_back(make_pair(a, make_pair(r, c)));
			}
		}
	}
	//cout << ans << " " << a << endl;
	fout << ans+a << " " << vp.size() << endl;
	for (int i = 0; i < vp.size(); i++){
		fout << vp[i].first << " " << vp[i].second.first << " " << vp[i].second.second << endl;
	}
}
int main(){
	ios_base::sync_with_stdio(false);
	int t;

	fin.open("D-large.in");
	fin >> t;
	
	fout.open("4-1.out");
	G = flow_graph(700, 50000);
	for (int ti = 1; ti <= t; ti++){
		fout << "Case #" << ti << ": ";
		int n, m;
		fin >> n >> m;
		fill(row, row + n + 1, false);
		fill(col, col + n + 1, false);
		fill(diag, diag + 2 * n + 5, false);
		fill(antidiag, antidiag + 2 * n + 5, false);
		for (int i = 1; i <= n; i++){
			fill(mat[i], mat[i] + n + 1, 0);
			fill(newmat[i], newmat[i] + n + 1, 0);
		}

		int ans = 0;
		for (int i = 0; i < m; i++){
			char a;
			int r, c;
			fin >>a>> r >> c;
			if (a == '+') mat[r][c] = 1;
			else if (a == 'x') mat[r][c] = 2;
			else mat[r][c] = 3;
			if (a != '+'){
				row[r] = col[c] = true;
			}
			if (a != 'x'){
				diag[r + c] = antidiag[r - c + n] = true;
			}
			if (a == 'o') ans += 2;
			else ans++;
		}
		solve(n,ans);
		
	}
	system("Pause");
	return 0;
}
