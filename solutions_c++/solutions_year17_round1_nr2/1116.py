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

const int maxn = 60;
int r[maxn];
int q[maxn][maxn];

bool compute(int ind,int i,int& h,int&l){
	h = floor(q[ind][i] / (0.9*r[ind]));
	l = ceil(q[ind][i] / (1.1*r[ind]));
	if (h >= l) return true;
	else return false;
}


int solve(int p){
	//cout << "---------" << endl;
	int source = 0;
	int sink = 1;
	G.clear();
	for (int i = 1; i <= p; i++){
		G.add_edge(source, 2 * i,1);
		G.add_edge(2 * i + 1, sink, 1);
	}
	for (int i = 1; i <= p; i++){
		for (int j = 1; j <= p; j++){
			int l1, h1, l2, h2;
			if (compute(0, i - 1, h1, l1) && compute(1, j - 1, h2, l2)){
				//cout <<i-1<<" "<< l1 << " " << h1 << " " <<j-1<<" "<< l2 << " " << h2 << endl;
				if (l2 <= h1 && l1 <= h2){
					//cout << "!!!!" << endl;
					G.add_edge(2 * i, 2 * j + 1, 1);
				}
			}
		}
	}
	return G.max_flow(source, sink);
}

int main(){
	ios_base::sync_with_stdio(false);
	int t;
	ifstream fin;
	fin.open("B-small.in");
	fin >> t;
	ofstream fout;
	fout.open("2.out");
	G = flow_graph(1000,1000);
	for (int ti = 1; ti <= t; ti++){
		fout << "Case #" << ti << ": ";

		int n, p;
		fin >> n >> p;
		for (int i = 0; i < n; i++) fin >> r[i];
		for (int i = 0; i < n; i++){
			for (int j = 0; j < p; j++){
				fin >> q[i][j];
			}
		}
		if (n == 1){
			int ans = 0;
			for (int i = 0; i < p; i++){
				int hi = floor(q[0][i] / (0.9*r[0]));
				int lo = ceil(q[0][i]/(1.1*r[0]));
				//cout << lo << " " << hi <<" "<< q[0][i] << endl;
				if (hi >= lo) ans++;
			}
			fout << ans << endl;
		}
		else{
			fout << solve(p) << endl;
		}
		
	}
	system("Pause");
	return 0;
}
