#ifndef _HEAD_H_
#define _HEAD_H_
#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <stack>
#include <queue>

#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <climits>
#include <cctype>

#define rep(i, n) for (int i=0; i<(n); ++i)
#define repf(i, a, b) for (int i=(a); i<=(b); ++i)
#define repd(i, a, b) for (int i=(a); i>=(b); --i)
#define sz(a) ((int)(a).size())
#define SQR(x) ((x)*(x))

using namespace std;

template <class T> void checkmin(T &a, T b){ if (b<a) a=b; }
#endif
bool isEmpty(vector<vector<char>> &cake, int i, int x, int y){
	for (int j=x; j<=y; ++j)
		if (isalpha(cake[i][j]))
			return false;				

	return true;
}

int main(){
	int ts;	
	cin>>ts;
	for (int te=1; te<=ts; ++te){
		int n, m;
		cin >> n >> m;
		vector<vector<char>> cake(n, vector<char>(m, '?'));
		for (int i=0; i<n; ++i)
			for (int j=0; j<m; ++j){
				char c = getchar();
				while (!(c=='?' || isalpha(c)))
					c = getchar();
				cake[i][j] = c;
			}

		vector<bool> visited(26, false);
		for (int i=0; i<n; ++i)
			for (int j=0; j<m; ++j)
				if (isalpha(cake[i][j]) && !visited[cake[i][j] - 'A']){
					visited[cake[i][j]-'A'] = true;
					int x = j;
					int y = j;
					while (x-1 >= 0 && cake[i][x-1] == '?')
						-- x;
					while (y+1 < m && cake[i][y+1] == '?')
						++ y;

					int s = i;
					int t = i;
					while (s-1 >= 0 && isEmpty(cake, s-1, x, y))
						-- s;
					while (t+1 < n && isEmpty(cake, t+1, x, y))
						++ t;

					for (int ii=s; ii<=t; ++ii)
						for (int jj=x; jj<=y; ++jj)
							cake[ii][jj] = cake[i][j];
				}
		printf("Case #%d:\n", te);

		for (int i=0; i<n; ++i){
			for (int j=0; j<m; ++j){
				putchar(cake[i][j]);
			}
			puts("");
		}


	}
	return 0;
}
