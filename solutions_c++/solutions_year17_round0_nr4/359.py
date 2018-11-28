#include <iostream>
#include <fstream>
#include <stdio.h>

#include <string>
#include <map>
#include <utility>
#include <algorithm>

#include <vector>

using namespace std;
 
class KuhnImplementation
{
public:
	int n, k;
	vector < vector<int> > g;
	vector<int> pairs_of_right, pairs_of_left;
	vector<bool> used;
 
 
	bool kuhn (int v) 
	{
		if (used[v])  return false;
		used[v] = true;
		for (int i = 0; i < g[v].size(); ++i) 
		{
			int to = g[v][i]-n;
			if (pairs_of_right[to] == -1 || kuhn (pairs_of_right[to])) 
			{
				pairs_of_right[to] = v;
				pairs_of_left[v] = to;
				return true;
			}
		}
		return false;
	}
 
	vector<pair<int, int> > find_max_matching(vector<vector<int> > &_g, int _n, int _k) 
	{
		g = _g;
		//g[i] is a list of adjacent vertices to vertex i, where i is from left patr and g[i][j] is from right part
		n = _n;
		//n is number of vertices in left part of graph
		k = _k;
		//k is number of vertices in right part of graph
 
		pairs_of_right = vector<int> (k, -1);
		pairs_of_left = vector<int> (n, -1);
		//pairs_of_right[i] is a neighbor of vertex i from right part, on marked edge
		//pairs_of_left[i]  is a neighbor of vertex i from left part, on marked edge
		used = vector<bool> (n, false);
 
 
		bool path_found;
		do {
			fill(used.begin(), used.end(), false);
			path_found = false;
			//remember to start only from free vertices which are not visited yet
			for (int i = 0; i < n; ++i)
				if (pairs_of_left[i] < 0 && !used[i])
					path_found |= kuhn (i);
		} while (path_found);
 
 
		vector<pair<int, int> > res;
		for(int i = 0; i < k; i++)
			if(pairs_of_right[i] != -1)
				res.push_back(make_pair(pairs_of_right[i], i+n));
 
		return res;
	}
};


int main() {
	int t;
	cin >> t;
	for (int i0 = 0; i0 < t; ++i0) {
		int n, m;
		cin >> n >> m;
		vector<vector<char>> board(n), res(n);
		

		for (int i = 0; i < n; ++i) {
			board[i].resize(n, '.');
			res[i].resize(n, '.');
		};

		int y = 0;
		for (int i = 0; i < m; ++i) {
			char ch;
			int r, c;
			cin >> ch >> r >> c;
			board[r-1][c-1] = ch;
			if (ch == 'o') y+=2;
			else y += 1;
		};
		


		vector<int> count_row(n), count_col(n), count_diag(n*2-1), count_diag2(n*2-1);
		for (int i = 0; i < n; ++i)	
			for (int j = 0; j < n; ++j) {
				int d = 0;
				if (board[i][j] == 'x' || board[i][j] == 'o') d = 1;
				count_row[i] += d;
				count_col[j] += d;
			};

		vector<vector<int>> g1(2*n);
		for (int i = 0; i < n; ++i)
			for (int j = 0; j < n; ++j) {
				if ((board[i][j] == '.' || board[i][j] == '+' ) && count_row[i] == 0 && count_col[j] == 0) {
					g1[i].push_back(n+j);
				};
			};

		int ans = 0;
		KuhnImplementation solver1;
		auto m1 = solver1.find_max_matching(g1, n, n);
		for (auto p : m1) {
			int i = p.first;
			int j = p.second-n;
			res[i][j] = 'x';
			y++;
		}

		ans += m1.size();

		for (int i = 0; i < n; ++i)
			for (int j = 0; j < n; ++j) {
				int d = 0;
				if (board[i][j] == '+' || board[i][j] == 'o') d = 1;
				count_diag[i-j+n-1] += d;
				count_diag2[i+j] += d;
			};


		vector<vector<int>> g2(4*n-2);
		for (int i = 0; i < n; ++i)
			for (int j = 0; j < n; ++j)
				if ((board[i][j] == '.' || board[i][j] == 'x' ) && count_diag[i-j+n-1] == 0 && count_diag2[i+j] == 0 ) {
					g2[i-j+n-1].push_back(i+j+2*n-1);
				};

		KuhnImplementation solver2;
		auto m2 = solver2.find_max_matching(g2, n*2-1, n*2-1);
		ans += m2.size();
		for (auto p : m2) {
			int a = p.first-(n-1);
			int b = p.second-(n*2-1);
			int i = (a+b)/2;
			int j = (b-a)/2;
			if (res[i][j] == '.')
				res[i][j] = '+';
			else
				res[i][j] = 'o';			
			y++;
		}

		int z =0;
		for (int i = 0; i < n; ++i)
			for (int j = 0; j < n; ++j) 
				if (res[i][j] != '.') {
					z++;	
				};


		printf("Case #%d: %d %d\n", i0+1, y, z);
		for (int i = 0; i < n; ++i)
			for (int j = 0; j < n; ++j) 
				if (res[i][j] != '.') {
					if (board[i][j] != '.') 
						printf("o %d %d\n", i+1, j+1);
					else
						printf("%c %d %d\n", res[i][j], i+1, j+1);
				}
	};
};