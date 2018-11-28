#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <set>
#include <utility>
#include <iomanip>
#include <map>
#include <unordered_map>
#include <string>
#define INF 1000000000
#define HAND_TYPE 1
#define TEST 10
#define SMALL 100
#define LARGE 1000
#define INPUT_SITUATION SMALL
#define MAKE_OUTFILE
using namespace std;
typedef long long s64;
typedef unsigned long long u64;
int T,ans;
bool xgrid[100][100], pgrid[100][100];
bool absval_comp(int a, int b) {
	return a*a > b*b;
}
int main() {
	if (INPUT_SITUATION == TEST) 
		freopen("test_input.txt","r",stdin);
	else if (INPUT_SITUATION == SMALL)
		freopen("D-small2.in","r",stdin);
	else if (INPUT_SITUATION == LARGE)
		freopen("D-large.in","r",stdin);
	#ifdef MAKE_OUTFILE
	freopen("output.txt","w",stdout);
	#endif
	int N,M,row,col,score;
	char c;
	bool found;
	vector<int> rchange,cchange;
	vector<int> mindiag;
	unordered_map<int, bool> majdiag;
	cin >> T;
	for (int cas=0; cas<T; cas++) {
		cin >> N >> M;
		for (int i=0; i<N; ++i)
			for (int j=0; j<N; ++j) {
				xgrid[i][j] = 0;
				pgrid[i][j] = 0;
			}
		for (int i=0; i<M; ++i) {
			cin >> c >> row >> col;
			row--; col--;
			switch (c) {
				case 'o':
					xgrid[row][col] = 1;
					pgrid[row][col] = 1;
					break;
				case '+':
					pgrid[row][col] = 1;
					break;
				case 'x':
					xgrid[row][col] = 1;
					break;
			}
		}
		rchange.clear();
		cchange.clear();
		mindiag.clear();
		majdiag.clear();
		for (int i=0; i<N; ++i) {
			found = 0;
			for (int j=0; j<N; ++j)
				found |= xgrid[i][j];
			if (!found) rchange.push_back(i);
			found = 0;
			for (int j=0; j<N; ++j)
				found |= xgrid[j][i];
			if (!found) cchange.push_back(i);
		}
		for (int i=0; i<rchange.size(); ++i)
			xgrid[rchange[i]][cchange[i]] = 1;
		if (!pgrid[0][0]) {
			pgrid[N-1][N-1] = 1;
			rchange.push_back(N-1);
			cchange.push_back(N-1);
		}
		if (!pgrid[0][N-1]) {
			pgrid[N-1][0] = 1;
			rchange.push_back(N-1);
			cchange.push_back(0);
		}
		for (int i=1; i<N-1; ++i) {
			pgrid[N-1][i] = 1;
			rchange.push_back(N-1);
			cchange.push_back(i);
			if (!pgrid[0][i]) {
				pgrid[0][i] = 1;
				rchange.push_back(0);
				cchange.push_back(i);
			}
		}
		/*
		for (int i=-N+1; i<N; ++i) {
			for (int j=0; j<N; ++j) {
				if (i+j < 0 || i+j >= N) continue;
				if (pgrid[i+j][j]) goto skip_mindiag;
			}
			mindiag.push_back(i);
			skip_mindiag:;
		}
		for (int i=0; i<N*2-1; ++i)
			majdiag[i] = true;
		for (int i=0; i<N; ++i) {
			for (int j=0; j<N; ++j) {
				if (pgrid[i][j]) 
					majdiag[i+j] = false;
			}
		}
		sort(mindiag.begin(), mindiag.end(), absval_comp);
		for (int i=0; i<mindiag.size(); ++i) {
			for (int j=0; j<N; ++j) {
				if (j-mindiag[i] < 0 || j-mindiag[i] >= N) continue;
				if (majdiag[2*j-mindiag[i]]) {
					pgrid[j-mindiag[i]][j] = true;
					rchange.push_back(j-mindiag[i]);
					cchange.push_back(j);
					majdiag[2*j-mindiag[i]] = false;
					break;
				}
			}
		}*/
		score = 0;
		for (int i=0; i<N; ++i)
			for (int j=0; j<N; ++j)
				score += pgrid[i][j]+xgrid[i][j];
		set<pair<int, int> > counted;
		set<int> duplind;
		int dupl=0;
		for (int i=0; i<rchange.size(); ++i) {
			if (counted.count(make_pair(rchange[i], cchange[i]))) {
				++dupl;
				duplind.insert(i);
			}
			counted.insert(make_pair(rchange[i], cchange[i]));
		}
		cout << "Case #" << cas+1 << ": " << score << ' ' << rchange.size()-dupl << '\n';
		for (int i=0; i<rchange.size(); ++i) {
			if (duplind.count(i)) continue;
			cout << ".+xo"[pgrid[rchange[i]][cchange[i]]+xgrid[rchange[i]][cchange[i]]*2]
					 << ' ' << rchange[i]+1 << ' ' << cchange[i]+1 << '\n';
		}
	}
	
	return 0;
}
