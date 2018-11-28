#include <iostream>
#include <algorithm>
#include <queue>
#include <vector>
#include <cstring>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <map>
#include <stack>
#include <cassert>

using namespace std;

void solve(vector<string> & mat, int R, int C) {
	for (int i = 0 ; i < R ; ++i) {
		for (int j = 1 ; j < C ; ++j) {
			if (mat[i][j] == '?')
				mat[i][j] = mat[i][j-1];
		}
		for (int j = C-1 ; j --> 0; ) {
			if (mat[i][j] == '?')
				mat[i][j] = mat[i][j+1];
		}
	}
	for (int i = 1 ; i < R ; ++i) {
		if (mat[i][0] == '?')
			mat[i] = mat[i-1];
	}
	for (int i = R-1 ; i --> 0 ;) {
		if (mat[i][0] == '?')
			mat[i] = mat[i+1];
	}
}

int main(){
	int tcase;
	cin >> tcase;

	int R, C;
	vector<string> mat;
	for(size_t casen = 0; casen < tcase; ++casen)
	{
		cin >> R >> C;
		mat.resize(R);
		for (int i = 0 ; i < R ; ++i) {
			cin >> mat[i];
		}
		
		cout << "Case #" << casen + 1 << ": " << std::endl;
		solve(mat, R, C);
		for (int i = 0 ; i < R ; ++i)
			std::cout << mat[i] << std::endl;
	}
	

	return 0;
}
